#!/usr/bin/env python3
"""Tests para wiki_sources.py — stdlib unittest, sin red."""
import sys
import tempfile
import unittest
from pathlib import Path

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
                "﻿---\r\ntitle: Con BOM\r\ncompiled: false\r\n---\r\n",
                encoding="utf-8",
            )
            fm = ws.frontmatter(p)
        self.assertEqual(fm["title"], "Con BOM")
        self.assertIs(fm["compiled"], False)


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
        estados = {r["title"]: r["estado"] for r in rows}
        self.assertEqual(estados["Alfa página"], "pendiente")
        self.assertEqual(estados["Beta doc"], "compilada")


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


class TestRender(unittest.TestCase):
    FILA = {
        "path": "papers/doc.md",
        "folder": "papers",
        "title": "Documento de prueba",
        "source": "https://ejemplo.org/doc",
        "author": "Autor",
        "date": "2026-01-02",
        "tags": ["rebt"],
        "compiled": True,
        "estado": "compilada",
    }

    def test_cabecera_declara_que_es_generado(self):
        out = ws.render([dict(self.FILA)], {}, "2026-11-14")
        self.assertIn("generado", out.lower())
        self.assertIn("wiki_sources.py", out)
        self.assertIn("No lo edites a mano", out)

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

    def test_lista_los_pendientes_por_sepado(self):
        fila = dict(self.FILA, compiled=False, estado="pendiente")
        out = ws.render([fila], {}, "2026-11-14")
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


if __name__ == "__main__":
    unittest.main()
