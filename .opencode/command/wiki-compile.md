---
description: Compila las fuentes nuevas de raw/ en artículos de la wiki
---

Sigue estos pasos EN ORDEN. Las reglas completas están en AGENTS.md.

## 1. Encontrar fuentes pendientes

Busca los archivos de `knowledge/raw/` (recursivamente) cuyo frontmatter contenga `compiled: false`:

```
grep -rl "compiled: false" knowledge/raw
```

Si no hay ninguno, responde "No hay fuentes pendientes" y termina.
Si hay varios, procésalos de uno en uno.

## 2. Para cada fuente

a. Lee la fuente completa.

b. Extrae:
   - Conceptos o ideas importantes (-> `wiki/concepts/`)
   - Personas relevantes (-> `wiki/people/`)
   - Herramientas o productos (-> `wiki/tools/`)
   Prioriza calidad: entre 3 y 8 artículos por fuente es lo normal. No crees artículos para menciones triviales.

c. Lee `knowledge/wiki/_index.md` para ver qué ya existe.

d. Para cada elemento extraído:
   - Si YA existe un artículo: léelo y actualízalo añadiendo la información nueva, la fuente en `sources`, y la fecha en `updated`. No borres información previa.
   - Si NO existe: créalo con el formato de AGENTS.md.

e. Añade enlaces `[[...]]` hacia otros artículos relacionados, tanto nuevos como existentes. Si un artículo existente es relevante para el nuevo, edita también el existente para enlazar de vuelta (backlink).

f. Marca la fuente: cambia `compiled: false` por `compiled: true` en su frontmatter. No toques nada más de la fuente.

## 3. Actualizar el índice

Actualiza `knowledge/wiki/_index.md` añadiendo los artículos nuevos con una descripción de una línea. Mantén el orden alfabético dentro de cada sección.

## 4. Reconstruir la búsqueda

```
python knowledge/tools/wiki_search.py index
```

## 5. Informe final

Termina con un resumen corto:
- Fuentes procesadas
- Artículos creados (lista)
- Artículos actualizados (lista)

$ARGUMENTS
