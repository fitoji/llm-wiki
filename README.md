# Starter kit: LLM wiki para opencode

Una base de conocimiento que **mantiene el agente**. Tú aportas material y haces preguntas; el agente escribe y ordena la wiki siguiendo el contrato de `AGENTS.md`.

## Qué hay acá

| Ruta | Qué es |
| --- | --- |
| `AGENTS.md` | El contrato: estructura, reglas y formatos. Es lo primero que lee el agente. |
| `.opencode/commands/` | Los tres comandos: `/ingest`, `/wiki-compile`, `/wiki-lint`. |
| `knowledge/raw/` | Material en bruto. Solo lectura para el agente (salvo el campo `compiled`). Incluye `raw/imgs/` (figuras) y `raw/tablas/` (CSV), que las fuentes referencian. |
| `knowledge/wiki/` | La wiki. Acá escribe el agente. |
| `knowledge/output/` | Respuestas e informes que vale la pena conservar. |
| `knowledge/tools/wiki_search.py` | Búsqueda de texto completo (SQLite FTS5, sin dependencias). |
| `tools/guia_rebt/` | Pipeline que regenera el corpus de Guías Técnicas del REBT desde los PDF oficiales (`indice.json` lleva el `sha256` de cada PDF). |

## Instalación

1. Copia el contenido de esta carpeta a la raíz de tu vault de Obsidian: `AGENTS.md`, `.opencode/commands/` y `knowledge/`.
2. Las carpetas vacías ya vienen con un `.gitkeep`; si armas el vault desde cero, crea:
   ```
   knowledge/raw/{articles,transcripts,papers,imgs,tablas}
   knowledge/wiki/{concepts,people,tools}
   knowledge/output
   ```
3. Crea `knowledge/wiki/_index.md` con una sola línea: `# Índice de la wiki`.
4. Abre opencode desde la raíz del vault.

Requisitos: opencode y Python 3. Nada más: la búsqueda usa el módulo `sqlite3` de la biblioteca estándar. En Linux y macOS el intérprete suele ser `python3`; en Windows es `python`.

## Empezar a trabajar con material

El ciclo completo, de cero a una wiki usable:

**1. Traer material.**

```
/ingest https://example.com/articulo
/ingest C:\Users\vos\Downloads\paper.pdf
```

`/ingest` decide la carpeta según el tipo (artículo, transcripción, paper), guarda el archivo en `knowledge/raw/` con su frontmatter y deja `compiled: false`. Si no puede obtener el contenido, te lo dice y te pide que lo pegues: no inventa.

Si tenés el PDF u otro binario a mano, dejalo en `knowledge/inbox/` (ignorada por git) y procesalo desde ahí:

```
/ingest knowledge/inbox/paper.pdf
```

`inbox/` es la bandeja de entrada: material crudo que todavía no se convirtió. Lo que se versiona es el `.md` que queda en `raw/`, no el binario.

**2. Compilar.**

```
/wiki-compile
```

Lee las fuentes con `compiled: false`, crea o actualiza los artículos en `knowledge/wiki/`, actualiza `_index.md`, marca las fuentes como compiladas y reconstruye el índice de búsqueda. Procesa todas las pendientes de una en una; si tienes muchas, conviene ir de a tandas chicas (trae 1-3 fuentes, compila, repite) para no perder calidad.

**3. Auditar.**

```
/wiki-lint
```

Revisa enlaces rotos, frontmatter, huérfanos, duplicados, `sources` que no existen y fuentes sin compilar. Escribe el informe en `knowledge/output/lint-YYYY-MM-DD.md` y solo corrige el índice por su cuenta; todo lo demás te lo propone.

**4. Consultar.**

Pregunta normal en el chat:

```
¿qué dice la wiki sobre capability overhang?
```

El agente lee `_index.md`, busca con `wiki_search.py`, abre los artículos y responde citando con `[[enlaces]]`. Si el dato no está en la wiki pero sí en una fuente de `raw/`, responde desde la fuente y te ofrece compilarla.

**5. Conservar lo que sirve.**

Si la respuesta fue buena, pídele que la guarde en `knowledge/output/` o que la convierta en artículo. Los artículos nuevos entran al índice y al grafo de Obsidian; los archivos de `output/` no.

## Los tres comandos

| Comando | Qué hace | Qué escribe | Cuándo |
| --- | --- | --- | --- |
| `/ingest <url o ruta>` | Descarga o lee el material y lo deja en `raw/` con frontmatter | Un archivo en `knowledge/raw/` | Cada vez que aparece material nuevo |
| `/wiki-compile` | Convierte fuentes pendientes en artículos y los enlaza | `knowledge/wiki/`, `_index.md`, flag `compiled` | Después de uno o más `/ingest` |
| `/wiki-lint` | Audita la salud de la wiki | Informe en `knowledge/output/` (+ arreglos de índice) | Cada pocas compilaciones |

Para YouTube, `/ingest` usa `yt-dlp` **si está instalado**; si no, te pide la transcripción o el texto. No lo instala por su cuenta.

## Búsqueda manual

```bash
python knowledge/tools/wiki_search.py search "capability overhang"
python knowledge/tools/wiki_search.py search "aves" -n 5
python knowledge/tools/wiki_search.py index          # fuerza la reconstrucción
```

`search` reindexa sola cuando detecta artículos nuevos o modificados, así que el `index` manual casi nunca hace falta. Si un archivo no está en UTF-8, la indexación lo omite y avisa en vez de abortar.

## Modelo

Los comandos no fijan modelo: usan el que tengas activo en opencode. Para fijar uno solo a un comando, agrega al frontmatter del archivo:

```yaml
---
description: Revisa la salud de la wiki y escribe un informe
model: proveedor/modelo
---
```

Los ids exactos salen de `opencode models`. Para cambiarlo en toda la sesión, usa `/models`.

## Problemas comunes

- **"Sin resultados" y hay artículos.** Ejecuta `index` a mano. Si el problema se repite, revisa que los archivos estén en UTF-8.
- **"Aviso: se omitieron archivos ilegibles".** Alguno está guardado en ANSI (pasa con el Bloc de notas y con `Set-Content` de PowerShell). Vuelve a guardarlo como UTF-8.
- **El agente intenta usar `grep` o `rg`.** Hoy ambos están en el PATH, pero no dependas de eso: usá tu herramienta de búsqueda nativa, que es portable entre equipos. Para los artículos, `wiki_search.py` (índice FTS5) es lo más rápido.
- **`knowledge/tools/wiki_index.sqlite` aparece como cambio.** No debería: está en `.gitignore`. Si lo ves, revisa que el `.gitignore` haya viajado con el kit.

## Consejos con modelos chicos

- Compila de 1 a 3 fuentes por tanda; los modelos chicos pierden calidad con lotes grandes.
- Después de las primeras compilaciones, revisa a mano un par de artículos para confirmar que respetan el formato.
- Ejecuta `/wiki-lint` cada pocas fuentes: es más barato corregir temprano.
- Obsidian es solo el visor: abre `knowledge/wiki/` como parte de tu vault y usa la vista de grafo para ver los enlaces.
