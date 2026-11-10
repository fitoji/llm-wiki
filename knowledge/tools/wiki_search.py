#!/usr/bin/env python3
"""Búsqueda de texto completo sobre la wiki (SQLite FTS5, sin dependencias).

Uso:
    python knowledge/tools/wiki_search.py index
    python knowledge/tools/wiki_search.py search "capability overhang" [-n 10]
"""
import argparse
import re
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # carpeta knowledge/
WIKI = ROOT / "wiki"
DB = ROOT / "tools" / "wiki_index.sqlite"


def parse(path: Path):
    text = path.read_text(encoding="utf-8")
    title = path.stem
    body = text
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
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
    for p in sorted(WIKI.rglob("*.md")):
        if p.name == "_index.md":
            continue
        title, body = parse(p)
        con.execute(
            "INSERT INTO docs(path, title, body) VALUES (?, ?, ?)",
            (str(p.relative_to(ROOT)), title, body),
        )
        n += 1
    con.commit()
    con.close()
    print(f"Indexados {n} artículos en {DB.name}")


def search(query: str, limit: int):
    if not DB.exists():
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
