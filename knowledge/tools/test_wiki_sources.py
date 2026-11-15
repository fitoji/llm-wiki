#!/usr/bin/env python3
"""Tests para wiki_sources.py — stdlib unittest, sin red."""
import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))
import wiki_sources as ws


def escribir(path: Path, front: str, cuerpo: str = "Cuerpo.\n"):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"---\n{front}\n---\n\n{cuerpo}", encoding="utf-8")


class TestFrontmatter(unittest.TestCase):
    def test_lee_todos_los_campos(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "f.md"
            escribir(
                p,
                "title: Título de prueba\n"
                "source: https://ejemplo.org/doc\n"
                "author: Autor\n"
                "date: 2026-01-02\n"
                "tags: [rebt, prueba]\n"
                "compiled: false",
            )
            fm = ws.frontmatter(p)
        self.assertEqual(fm["title"], "Título de prueba")
        self.assertEqual(fm["source"], "https://ejemplo.org/doc")
        self.assertEqual(fm["author"], "Autor")
        self.assertEqual(fm["date"], "2026-01-02")
        self.assertEqual(fm["tags"], ["rebt", "prueba"])
        self.assertIs(fm["compiled"], False)

    def test_compiled_verdadero_y_listas(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "f.md"
            escribir(p, "title: X\ntags: [a]\ncompiled: true")
            fm = ws.frontmatter(p)
        self.assertIs(fm["compiled"], True)
        self.assertEqual(fm["tags"], ["a"])

    def test_sin_frontmatter_no_explota(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "f.md"
            p.write_text("Solo texto.\n", encoding="utf-8")
            self.assertEqual(ws.frontmatter(p), {})

    def test_tolera_crlf_y_bom(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "f.md"
            p.write_text(
                "\ufeff---\r\ntitle: Con BOM\r\ncompiled: false\r\n---\r\n",
                encoding="utf-8",
            )
            fm = ws.frontmatter(p)
        self.assertEqual(fm["title"], "Con BOM")
        self.assertIs(fm["compiled"], False)

    def test_avisa_en_stderr_si_no_se_puede_leer(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "f.md"
            p.write_bytes(b"\xff\xfe\x00no-utf8")
            err = io.StringIO()
            with contextlib.redirect_stderr(err):
                fm = ws.frontmatter(p)
        self.assertEqual(fm, {})
        self.assertIn("aviso", err.getvalue())
        self.assertIn("f.md", err.getvalue())


class TestCollect(unittest.TestCase):
    def _raw(self, tmp: str) -> Path:
        raw = Path(tmp) / "raw"
        escribir(
            raw / "papers" / "b-doc.md",
            "title: Beta doc\nsource: https://b\ncompiled: true",
        )
        escribir(
            raw / "articles" / "a-pag.md",
            "title: Alfa página\nsource: https://a\ncompiled: false",
        )
        return raw

    def test_recorre_subcarpetas_y_ordena_por_titulo(self):
        with tempfile.TemporaryDirectory() as tmp:
            rows = ws.collect(self._raw(tmp))
        self.assertEqual([r["title"] for r in rows], ["Alfa página", "Beta doc"])
        self.assertEqual(rows[0]["folder"], "articles")
        self.assertEqual(rows[1]["folder"], "papers")

    def test_ruta_relativa_a_raw_para_cruzar_con_citations(self):
        with tempfile.TemporaryDirectory() as tmp:
            rows = ws.collect(self._raw(tmp))
        self.assertEqual(
            sorted(r["path"] for r in rows),
            ["articles/a-pag.md", "papers/b-doc.md"],
        )

    def test_estado_compilada_o_pendiente(self):
        with tempfile.TemporaryDirectory() as tmp:
            rows = ws.collect(self._raw(tmp))
        self.assertIs(rows[0]["compiled"], False)
        self.assertIs(rows[1]["compiled"], True)


class TestCitations(unittest.TestCase):
    def test_mapea_fuente_a_articulos_que_la_citan(self):
        with tempfile.TemporaryDirectory() as tmp:
            wiki = Path(tmp) / "wiki" / "concepts"
            escribir(
                wiki / "articulo-uno.md",
                "title: Uno\nsources: [papers/x.md, papers/y.md]",
            )
            escribir(
                wiki / "articulo-dos.md",
                "title: Dos\nsources: [papers/x.md]",
            )
            cites = ws.citations(Path(tmp) / "wiki")
        self.assertEqual(cites["papers/x.md"], ["articulo-dos", "articulo-uno"])
        self.assertEqual(cites["papers/y.md"], ["articulo-uno"])

    def test_sources_sin_corchetes_no_itera_por_caracter(self):
        with tempfile.TemporaryDirectory() as tmp:
            wiki = Path(tmp) / "wiki" / "concepts"
            escribir(wiki / "articulo.md", "title: A\nsources: papers/x.md")
            cites = ws.citations(Path(tmp) / "wiki")
        self.assertEqual(cites, {"papers/x.md": ["articulo"]})


class TestRender(unittest.TestCase):
    FILA = {
        "path": "papers/doc.md",
        "folder": "papers",
        "title": "Documento de prueba",
        "source": "https://ejemplo.org/doc",
        "date": "2026-01-02",
        "tags": ["rebt"],
        "compiled": True,
    }

    def test_cabecera_declara_que_es_generado(self):
        out = ws.render([dict(self.FILA)], {}, "2026-11-14")
        self.assertIn("generado", out.lower())
        self.assertIn("wiki_sources.py", out)
        self.assertIn("No lo edites a mano", out)

    def test_cabecera_no_sugiere_wiki_search_para_fuentes(self):
        # wiki_search indexa la wiki, no raw/: la cabecera no debe contradecir
        # la tabla de herramientas de AGENTS.md.
        out = ws.render([dict(self.FILA)], {}, "2026-11-14")
        self.assertNotIn("wiki_search", out)

    def test_cuenta_fuente_y_pendientes(self):
        out = ws.render([dict(self.FILA)], {}, "2026-11-14")
        self.assertIn("**1 fuente**", out)
        self.assertIn("1 compilada", out)
        self.assertIn("0 pendientes", out)

    def test_fila_con_titulo_fecha_y_estado(self):
        out = ws.render([dict(self.FILA)], {}, "2026-11-14")
        self.assertIn("Documento de prueba", out)
        self.assertIn("2026-01-02", out)
        self.assertIn("https://ejemplo.org/doc", out)
        self.assertIn("rebt", out)
        self.assertIn("compilada", out)

    def test_fila_deriva_estado_de_compiled(self):
        # estado se deriva de compiled en el render: una sola fuente de verdad.
        out = ws.render([dict(self.FILA, compiled=False)], {}, "2026-11-14")
        fila = [
            l for l in out.splitlines()
            if l.startswith("| Documento de prueba")
        ][0]
        self.assertIn("| pendiente |", fila)
        self.assertNotIn("| compilada |", fila)

    def test_lista_los_pendientes_por_separado(self):
        out = ws.render([dict(self.FILA, compiled=False)], {}, "2026-11-14")
        self.assertIn("## Pendientes de compilar", out)
        self.assertIn("Documento de prueba", out.split("## Pendientes de compilar")[1])

    def test_sin_pendientes_lo_dice(self):
        out = ws.render([dict(self.FILA)], {}, "2026-11-14")
        self.assertIn("Ninguna", out.split("## Pendientes de compilar")[1])

    def test_muestra_que_articulos_citan_la_fuente(self):
        out = ws.render(
            [dict(self.FILA)], {"papers/doc.md": ["otro-articulo"]}, "2026-11-14"
        )
        self.assertIn("otro-articulo", out)

    def test_agrupa_por_carpeta(self):
        otra = dict(self.FILA, path="articles/p.md", folder="articles", title="Zeta")
        out = ws.render([dict(self.FILA), otra], {}, "2026-11-14")
        self.assertIn("papers", out)
        self.assertIn("articles", out)


class TestBuild(unittest.TestCase):
    def test_genera_el_archivo_completo(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            escribir(
                root / "raw" / "papers" / "doc.md",
                "title: Doc único\nsource: https://u\ncompiled: true",
            )
            escribir(
                root / "wiki" / "concepts" / "art.md",
                "title: Art\nsources: [papers/doc.md]",
            )
            out = ws.build(root, hoy="2026-11-14")
        self.assertIn("Doc único", out)
        self.assertIn("art", out)
        self.assertIn("**1 fuente**", out)


class TestMain(unittest.TestCase):
    """Contrato de la CLI: exit 0/1 y escritura del archivo generado."""

    def test_build_escribe_el_archivo_y_sale_cero(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "sources.md"
            with mock.patch.object(ws, "OUT", out), contextlib.redirect_stdout(
                io.StringIO()
            ):
                rc = ws.main(["build"])
            self.assertEqual(rc, 0)
            self.assertIn("# Fuentes procesadas", out.read_text(encoding="utf-8"))

    def test_check_sale_cero_recien_generado(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "sources.md"
            with mock.patch.object(ws, "OUT", out), contextlib.redirect_stdout(
                io.StringIO()
            ):
                self.assertEqual(ws.main(["build"]), 0)
                self.assertEqual(ws.main(["check"]), 0)

    def test_check_sale_uno_si_falta_el_archivo(self):
        with tempfile.TemporaryDirectory() as tmp:
            with mock.patch.object(ws, "OUT", Path(tmp) / "falta.md"), \
                    contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(ws.main(["check"]), 1)

    def test_check_sale_uno_si_el_contenido_cambio(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "sources.md"
            out.write_text("contenido que no corresponde\n", encoding="utf-8")
            with mock.patch.object(ws, "OUT", out), contextlib.redirect_stdout(
                io.StringIO()
            ):
                self.assertEqual(ws.main(["check"]), 1)

    def test_check_no_depende_del_dia(self):
        # El archivo se generó otro día; el contenido es idéntico salvo la
        # línea de fecha. check debe salir 0: solo el contenido manda.
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "sources.md"
            out.write_text(ws.build(hoy="2020-01-01"), encoding="utf-8")
            with mock.patch.object(ws, "OUT", out), contextlib.redirect_stdout(
                io.StringIO()
            ):
                self.assertEqual(ws.main(["check"]), 0)

    def test_mensaje_de_error_trae_el_comando_completo(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = Path(tmp) / "sources.md"
            out.write_text("basura\n", encoding="utf-8")
            buf = io.StringIO()
            with mock.patch.object(ws, "OUT", out), contextlib.redirect_stdout(buf):
                ws.main(["check"])
        self.assertIn("python knowledge/tools/wiki_sources.py build", buf.getvalue())


if __name__ == "__main__":
    unittest.main()
