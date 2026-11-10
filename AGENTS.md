# Wiki personal mantenida por LLM

Este vault contiene una base de conocimiento al estilo "LLM wiki" de Karpathy.
Tú (el agente) mantienes la wiki. El usuario solo aporta fuentes y hace preguntas.

## Estructura

```
knowledge/
  raw/              <- fuentes en bruto. SOLO LECTURA (excepto el campo `compiled`)
    articles/
    transcripts/
    papers/
  wiki/             <- tú escribes aquí
    concepts/       <- ideas, técnicas, marcos de trabajo
    people/         <- personas
    tools/          <- herramientas, productos, librerías
    _index.md       <- índice maestro
  output/           <- respuestas a consultas que merece la pena conservar
  tools/
    wiki_search.py  <- búsqueda de texto completo (SQLite FTS5)
```

## Reglas generales

1. Nunca modifiques el contenido de `knowledge/raw/`. Lo único que puedes cambiar es `compiled: false` -> `compiled: true` en el frontmatter.
2. Escribe los artículos de la wiki en español, aunque la fuente esté en otro idioma. Mantén en el idioma original los nombres propios y términos técnicos.
3. Antes de crear un artículo nuevo, comprueba si ya existe uno sobre el mismo tema (mira `_index.md` y busca con `grep -ril`). Si existe, ACTUALIZALO en lugar de duplicarlo.
4. No inventes datos. Todo lo que escribas debe poder apoyarse en una fuente de `raw/`. Si algo no está claro en la fuente, no lo afirmes.
5. Cada afirmación importante debe poder rastrearse: lista las fuentes en el frontmatter (`sources`).
6. Los nombres de archivo van en minúsculas, con guiones y sin acentos: `capability-overhang.md`, `amol-avasari.md`.
7. Enlaza con la sintaxis de Obsidian: `[[nombre-del-archivo]]` (sin extensión).

## Formato de un artículo de la wiki

```markdown
---
title: Título legible
type: concept | person | tool
tags: [etiqueta1, etiqueta2]
sources: [articles/archivo-fuente.md]
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# Título legible

Resumen en 2-3 frases.

## Puntos clave
- ...
- ...

## Detalles
Explicación más extensa, con enlaces a otros artículos: [[otro-concepto]].

## Relacionado
- [[articulo-1]]
- [[articulo-2]]
```

## Formato de una fuente en raw/

```markdown
---
title: Título de la fuente
source: URL o referencia
author: Autor
date: YYYY-MM-DD
tags: []
compiled: false
---

(contenido original)
```

## Formato de `_index.md`

Una lista agrupada por tipo, un artículo por línea:

```markdown
# Índice de la wiki

## Concepts
- [[nombre]] — descripción de una línea

## People
- [[nombre]] — descripción de una línea

## Tools
- [[nombre]] — descripción de una línea
```

## Comandos disponibles

- `/ingest <url o ruta>`: guarda una fuente nueva en `raw/` con su frontmatter.
- `/wiki-compile`: convierte las fuentes con `compiled: false` en artículos de la wiki.
- `/wiki-lint`: revisa la salud de la wiki y escribe un informe.
- Búsqueda: `python knowledge/tools/wiki_search.py search "consulta"`.

## Responder preguntas

Cuando el usuario pregunte algo sobre su conocimiento:
1. Lee `knowledge/wiki/_index.md`.
2. Busca con `wiki_search.py` y lee los artículos relevantes.
3. Responde citando los artículos con `[[enlaces]]`.
4. Si la respuesta es valiosa, ofrece guardarla en `knowledge/output/` o convertirla en un artículo.
5. Si la wiki no tiene la información, dilo claramente; no la inventes.
