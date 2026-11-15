#!/usr/bin/env python3
"""Índice derivado de las fuentes de knowledge/raw/ (sin dependencias).

Genera `knowledge/sources.md` a partir del frontmatter de cada fuente, para
responder de un vistazo «¿ya digerí este PDF?». El archivo generado nunca se
edita a mano: se regenera con:

    python knowledge/tools/wiki_sources.py build
    python knowledge/tools/wiki_sources.py check   # avisa si está desactualizado

`check` sale con código 1 si el contenido de `knowledge/sources.md` no
coincide con el de `raw/` (la línea de fecha no cuenta).
"""
import argparse
import re
import sys
from datetime import date
from pathlib import Path
from typing import Optional, Union

ROOT = Path(__file__).resolve().parent.parent  # carpeta knowledge/
RAW = ROOT / "raw"
WIKI = ROOT / "wiki"
OUT = ROOT / "sources.md"

# Frontmatter plano: `clave: valor`. Las listas van en una línea: [a, b, c].
_FM = re.compile(r"^---\r?\n(.*?)\r?\n---", re.S)


def frontmatter(path: Path) -> dict:
    """Campos del frontmatter de un markdown. Vacío si no tiene."""
    try:
        text = Path(path).read_text(encoding="utf-8-sig")
    except (UnicodeDecodeError, OSError) as exc:
        print(f"aviso: no se pudo leer {path}: {exc}", file=sys.stderr)
        return {}
    m = _FM.match(text)
    if not m:
        return {}
    out = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        key, raw = line.split(":", 1)
        key = key.strip()
        if key:
            out[key] = _valor(raw)
    return out


def _valor(raw: str) -> Union[list, bool, str]:
    v = raw.strip()
    if v.startswith("[") and v.endswith("]"):
        interior = v[1:-1].strip()
        if not interior:
            return []
        return [x.strip().strip("\"'") for x in interior.split(",")]
    if v.lower() in ("true", "false"):
        return v.lower() == "true"
    return v.strip("\"'")


def collect(raw: Path = RAW) -> list:
    """Una fila por fuente, ordenada por título."""
    rows = []
    for p in sorted(Path(raw).rglob("*.md")):
        fm = frontmatter(p)
        rel = p.relative_to(raw)
        folder = rel.parts[0] if len(rel.parts) > 1 else "(raíz)"
        tags = fm.get("tags") or []
        if isinstance(tags, str):  # `tags: rebt` sin corchetes
            tags = [tags]
        rows.append(
            {
                "path": str(rel),
                "folder": folder,
                "title": fm.get("title") or p.stem,
                "source": str(fm.get("source") or ""),
                "date": str(fm.get("date") or ""),
                "tags": tags,
                "compiled": bool(fm.get("compiled")),
            }
        )
    rows.sort(key=lambda r: (r["title"].lower(), r["path"]))
    return rows


def citations(wiki: Path = WIKI) -> dict:
    """Ruta de fuente (relativa a raw/) -> artículos que la citan, ordenados."""
    out: dict = {}
    for p in sorted(Path(wiki).rglob("*.md")):
        if p.name == "_index.md":
            continue
        fuentes = frontmatter(p).get("sources") or []
        if isinstance(fuentes, str):  # `sources: ruta.md` sin corchetes
            fuentes = [fuentes]
        for src in fuentes:
            out.setdefault(str(src), []).append(p.stem)
    for src in out:
        out[src].sort()
    return out


def _fila(r: dict, cites: dict) -> str:
    tags = ", ".join(r["tags"]) if r["tags"] else "—"
    origen = r["source"] or "—"
    citan = cites.get(r["path"], [])
    citan_txt = ", ".join(citan) if citan else "—"
    fecha = r["date"] or "—"
    estado = "compilada" if r["compiled"] else "pendiente"
    return (
        f"| {r['title']} | {fecha} | {origen} | {tags} "
        f"| {estado} | {citan_txt} |"
    )


def render(rows: list, cites: dict, hoy: str) -> str:
    total = len(rows)
    n_comp = sum(1 for r in rows if r["compiled"])
    n_pend = total - n_comp
    plural = "fuente" if total == 1 else "fuentes"
    comp = "1 compilada" if n_comp == 1 else f"{n_comp} compiladas"
    pend = "1 pendiente" if n_pend == 1 else f"{n_pend} pendientes"

    out = [
        "# Fuentes procesadas",
        "",
        "> **Archivo generado** por `python knowledge/tools/wiki_sources.py`.",
        "> **No lo edites a mano**: se regenera desde el frontmatter de `knowledge/raw/`.",
        "",
        f"Actualizado: {hoy}.",
        "",
        f"**{total} {plural}** en total — {comp}, {pend}.",
        "",
        "Para comprobar si un PDF ya está digerido, buscá acá por título u origen",
        "(`Ctrl+F`) o en `knowledge/raw/` con tu herramienta de búsqueda nativa.",
        "",
        "## Pendientes de compilar",
        "",
    ]

    pendientes = [r for r in rows if not r["compiled"]]
    if not pendientes:
        out.append("Ninguna.")
    else:
        for r in pendientes:
            out.append(f"- **{r['title']}** (`raw/{r['path']}`)")

    for folder in sorted({r["folder"] for r in rows}):
        sub = [r for r in rows if r["folder"] == folder]
        out += [
            "",
            f"## {folder} ({len(sub)})",
            "",
            "| Título | Fecha | Origen | Tags | Estado | Artículos que la citan |",
            "|---|---|---|---|---|---|",
        ]
        out += [_fila(r, cites) for r in sub]

    return "\n".join(out) + "\n"


def build(root: Path = ROOT, hoy: Optional[str] = None) -> str:
    root = Path(root)
    hoy = hoy or date.today().isoformat()
    return render(collect(root / "raw"), citations(root / "wiki"), hoy)


def _sin_fecha(texto: str) -> str:
    """Texto sin la línea 'Actualizado: ...', para comparar contenido real."""
    return re.sub(r"^Actualizado: .*$", "", texto, flags=re.M)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("build", help="regenera knowledge/sources.md")
    sub.add_parser(
        "check",
        help="sale con 1 si el contenido de knowledge/sources.md no coincide con raw/",
    )
    args = ap.parse_args(argv)

    texto = build()
    if args.cmd == "build":
        OUT.write_text(texto, encoding="utf-8")
        n_lineas = len(texto.splitlines())
        try:
            nombre = OUT.relative_to(ROOT.parent)
        except ValueError:  # OUT reubicado (tests)
            nombre = OUT
        print(f"Generado {nombre} con {n_lineas} líneas")
        return 0

    actual = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
    if _sin_fecha(actual) == _sin_fecha(texto):
        print("knowledge/sources.md está al día")
        return 0
    print(
        "knowledge/sources.md está desactualizado: "
        "corré `python knowledge/tools/wiki_sources.py build`"
    )
    return 1


if __name__ == "__main__":
    sys.exit(main())
