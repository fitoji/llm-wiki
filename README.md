# Starter kit: LLM wiki para opencode

## Instalación

1. Copia el contenido de esta carpeta a la raíz de tu vault de Obsidian:
   - `AGENTS.md`
   - `.opencode/command/` (los tres comandos)
   - `knowledge/` (con `tools/wiki_search.py`)
2. Crea las carpetas vacías que faltan:
   ```
   mkdir -p knowledge/raw/{articles,transcripts,papers} knowledge/wiki/{concepts,people,tools} knowledge/output
   ```
3. Crea `knowledge/wiki/_index.md` con el contenido: `# Índice de la wiki`
4. Abre opencode desde la raíz del vault.

## Uso

- `/ingest https://...`   guarda una fuente en `knowledge/raw/`
- `/wiki-compile`         genera/actualiza los artículos de la wiki
- `/wiki-lint`            auditoría de la wiki
- `python knowledge/tools/wiki_search.py search "tema"`

## Modelo

Los comandos no fijan modelo, así que usan el que tengas activo en opencode (DeepSeek Flash).
Si quieres un modelo más potente solo para `/wiki-lint` o consultas, añade `model: proveedor/modelo`
al frontmatter del comando (el id exacto lo ves con `opencode models`).

## Consejos con un modelo "flash"

- Compila de 1 a 3 fuentes cada vez; los modelos pequeños pierden calidad con lotes grandes.
- Tras las primeras compilaciones, revisa a mano un par de artículos para comprobar que siguen el formato.
- Ejecuta `/wiki-lint` cada pocas fuentes.
- Recuerda que Obsidian es solo el visor: abre `knowledge/wiki/` como parte de tu vault y usa la vista de grafo.
