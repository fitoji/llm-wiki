#!/usr/bin/env python3
"""Búsqueda de texto completo sobre la wiki (SQLite FTS5, sin dependencias).

Uso:
    python knowledge/tools/wiki_search.py index
    python knowledge/tools/wiki_search.py search "capability overhang" [-n 10]

`search` reconstruye el índice por su cuenta si no existe o si algún artículo
cambió desde la última indexación. Los archivos que no sean UTF-8 se omiten con
un aviso en lugar de abortar la indexación completa.
"""
import argparse
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # carpeta knowledge/
WIKI = ROOT / "wiki"
DB = ROOT / "tools" / "wiki_index.sqlite"


def articles():
    """Artículos indexables de la wiki, en orden estable."""
    return sorted(p for p in WIKI.rglob("*.md") if p.name != "_index.md")


def parse(path: Path):
    # utf-8-sig tolera BOM; el regex tolera CRLF y ausencia de salto final.
    text = path.read_text(encoding="utf-8-sig")
    title = path.stem
    body = text
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n?(.*)$", text, re.S)
    if m:
        front, body = m.group(1), m.group(2)
        t = re.search(r"^title:\s*(.+)$", front, re.M)
        if t:
            title = t.group(1).strip().strip("\"'")
    return title, body


def build_index():
    DB.parent.mkdir(parents=True, exist_ok=True)
    if DB.exists():
        DB.unlink()
    con = sqlite3.connect(DB)
    con.execute(
        "CREATE VIRTUAL TABLE docs USING fts5(path, title, body, tokenize='unicode61 remove_diacritics 2')"
    )
    n = 0
    skipped = []
    for p in articles():
        try:
            title, body = parse(p)
        except (UnicodeDecodeError, OSError) as exc:
            skipped.append(f"{p.relative_to(ROOT)} ({exc.__class__.__name__})")
            continue
        con.execute(
            "INSERT INTO docs(path, title, body) VALUES (?, ?, ?)",
            (str(p.relative_to(ROOT)), title, body),
        )
        n += 1
    con.commit()
    con.close()
    if skipped:
        print("Aviso: se omitieron archivos ilegibles (guardalos como UTF-8):")
        for s in skipped:
            print(f"  - {s}")
    print(f"Indexados {n} artículos en {DB.name}")


def stale() -> bool:
    """True si falta el índice o si algún artículo es más nuevo que el índice."""
    if not DB.exists():
        return True
    db_mtime = DB.stat().st_mtime
    return any(p.stat().st_mtime > db_mtime for p in articles())


def search(query: str, limit: int):
    if stale():
        build_index()
    con = sqlite3.connect(DB)
    # Cada palabra entre comillas para evitar errores de sintaxis FTS
    terms = " ".join(f'"{w}"' for w in re.findall(r"\w+", query))
    if not terms:
        print("Consulta vacía")
        return
    rows = con.execute(
        "SELECT path, title, snippet(docs, 2, '[', ']', '…', 12) "
        "FROM docs WHERE docs MATCH ? ORDER BY rank LIMIT ?",
        (terms, limit),
    ).fetchall()
    con.close()
    if not rows:
        print("Sin resultados")
        return
    for path, title, snip in rows:
        print(f"{path}  —  {title}\n    {snip.strip()}\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("index", help="(re)construye el índice")
    s = sub.add_parser("search", help="busca en la wiki")
    s.add_argument("query")
    s.add_argument("-n", type=int, default=10, help="máximo de resultados")
    args = ap.parse_args()
    if args.cmd == "index":
        build_index()
    else:
        search(args.query, args.n)


if __name__ == "__main__":
    sys.exit(main())
