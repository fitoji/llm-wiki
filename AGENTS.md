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
    imgs/           <- figuras extraídas de los PDF (las fuentes las referencian como ../imgs/...)
    tablas/         <- CSV de cada tabla (las fuentes las referencian como ../tablas/...)
  inbox/            <- material sin digerir (PDFs, capturas). Binarios, ignorados por git
  wiki/             <- tú escribes aquí
    concepts/       <- ideas, técnicas, marcos de trabajo
    people/         <- personas
    tools/          <- herramientas, productos, librerías
    _index.md       <- índice maestro
  output/           <- respuestas a consultas que merece la pena conservar
  tools/
    wiki_search.py  <- búsqueda de texto completo (SQLite FTS5)
```

`knowledge/tools/wiki_index.sqlite` se genera solo al indexar y está ignorado por git. No lo edites ni lo borres a mano: `search` reconstruye el índice si detecta cambios.

`tools/guia_rebt/` (en la raíz del repo) es el pipeline que regenera el corpus de Guías Técnicas del REBT: `convert_guia_to_markdown.py` vuelve a bajar los PDF oficiales de industria.gob.es y produce los `.md` con las tablas inline, `indice.json` lleva el `sha256` de cada PDF para detectar si el ministerio publicó otra edición y `auditar_cobertura.py` verifica qué ITC tienen guía publicada.

## Reglas generales

1. Nunca modifiques el contenido de `knowledge/raw/`. Lo único que puedes cambiar es `compiled: false` -> `compiled: true` en el frontmatter.
2. Escribe los artículos de la wiki en español SIEMPRE, aunque la fuente esté en otro idioma (catalán incluido): traduce al español todo contenido en catalán antes de escribirlo o actualizarlo. Mantén en el idioma original solo los nombres propios y términos técnicos sin equivalente corriente.
3. Antes de crear un artículo nuevo, comprueba si ya existe uno sobre el mismo tema (mira `_index.md` y busca con tu herramienta de búsqueda sobre `knowledge/wiki/`; en este equipo no hay `grep` ni `rg` en el PATH, así que no uses un comando de shell). Si existe, ACTUALIZALO en lugar de duplicarlo.
4. No inventes datos. Todo lo que escribas debe poder apoyarse en una fuente de `raw/`. Si algo no está claro en la fuente, no lo afirmes.
5. Cada afirmación importante debe poder rastrearse: lista las fuentes en el frontmatter (`sources`).
6. Los nombres de archivo van en minúsculas, con guiones y sin acentos: `capability-overhang.md`, `amol-avasari.md`.
7. Enlaza con la sintaxis de Obsidian: `[[nombre-del-archivo]]` (sin extensión).
8. Cada vez que crees, renombres o borres un artículo, actualiza `knowledge/wiki/_index.md` en el mismo paso. Un artículo que no está en el índice está incompleto.
9. Al modificar un artículo existente, actualiza `updated` con la fecha del día.
10. Si una fuente contradice algo que ya está en un artículo, no borres lo anterior: anota ambas versiones con su fecha y su fuente, y marca la contradicción como pendiente de resolver.
11. `knowledge/output/` no es wiki: no lleva enlaces `[[...]]`, no entra en `_index.md` y no se indexa en la búsqueda.

## Formato de un artículo de la wiki

```markdown
---
title: Título legible
type: concept
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

- `type` lleva **un solo valor**: `concept`, `person` o `tool`. No escribas el enum completo.
- `sources` son rutas **relativas a `knowledge/raw/`** (`articles/archivo-fuente.md`), sin el prefijo `knowledge/raw/`. Puede haber varias en la lista.

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

`compiled` es el único campo editable de una fuente: `false` hasta que `/wiki-compile` la procese, `true` después. El resto del archivo es intocable.

## Formato de `_index.md`

Una lista agrupada por tipo, un artículo por línea, en orden alfabético dentro de cada sección. El ejemplo muestra las tres secciones: en la práctica solo aparecen las que tienen artículos. Se actualiza en el mismo paso que el artículo (regla 8):

```markdown
# Índice de la wiki

## Concepts
- [[nombre]] — descripción de una línea

## People
- [[nombre]] — descripción de una línea

## Tools
- [[nombre]] — descripción de una línea
```

## Formato de un archivo en output/

Markdown plano, sin frontmatter. El nombre lleva la fecha delante:

- Respuesta guardada: `YYYY-MM-DD-tema.md`
- Informe de `/wiki-lint`: `lint-YYYY-MM-DD.md`

Como `output/` queda fuera del grafo, se cita con el nombre del artículo en texto (`ver capability-overhang`), no con `[[enlaces]]`.

## Memoria (Engram): higiene de sesiones

Guardar memoria es parte del trabajo, pero falla cerrado cuando hay ambigüedad de sesión. Protocolo:

1. **Resolver el proyecto primero**: `mem_current_project` con el directorio del vault. Usa el `project` devuelto tal cual (`llm-wiki`). Nunca inventes un nombre de proyecto ni un `session_id`.
2. **Si `mem_save` o `mem_session_summary` falla** con `multiple active runtime sessions match the current project and directory`: no reintentes a ciegas. Ejecuta `mem_doctor`, lee el finding `ambiguous_active_runtime_sessions` y cierra **solo** los IDs confirmados como obsoletos con `mem_session_end` (cada uno con un resumen de cierre).
3. **Después de cualquier tanda de subagentes en paralelo**, ejecuta `mem_doctor`: cada subagente abre su propia sesión de runtime y la deja abierta al terminar. Cierra las huérfanas antes de intentar guardar el resumen del padre.
4. **Los subagentes cierran su sesión** con `mem_session_end` antes de devolver el resultado, o el padre las cierra al recibir la tanda.
5. Si el guardado sigue bloqueado, deja el trabajo hecho y reporta la limitación de memoria; no inventes una sesión para forzar la escritura.

## Comandos disponibles

- `/ingest <url o ruta>`: guarda una fuente nueva en `raw/` con su frontmatter.
- `/wiki-compile`: convierte las fuentes con `compiled: false` en artículos de la wiki.
- `/wiki-lint`: revisa la salud de la wiki y escribe un informe.
- Búsqueda: `python knowledge/tools/wiki_search.py search "consulta"`. Reindexa sola si detectó cambios; `... index` la fuerza.

## Responder preguntas

Cuando el usuario pregunte algo sobre su conocimiento:
1. Lee `knowledge/wiki/_index.md`.
2. Busca con `wiki_search.py` y lee los artículos relevantes.
3. Responde citando los artículos con `[[enlaces]]`.
4. Si la wiki no alcanza pero la información está en una fuente de `knowledge/raw/`, responde desde la fuente, cita su ruta y ofrece compilarla con `/wiki-compile`.
5. Si no está ni en la wiki ni en `raw/`, dilo claramente; no la inventes.
6. Si la respuesta es valiosa, ofrece guardarla en `knowledge/output/` (con el formato de arriba) o convertirla en un artículo.
