# Wiki del REBT: el reglamento, sus guías técnicas y el mapa de sus divergencias

Vault de conocimiento sobre el **Reglamento Electrotécnico para Baja Tensión** (REBT, RD 842/2002) que mantiene el agente: vos aportás material y hacés preguntas; el agente escribe, ordena y enlaza los artículos según el contrato de `AGENTS.md`.

Hoy contiene **100 fuentes** en bruto, **98 artículos** y **223 divergencias** documentadas entre el reglamento y sus 27 Guías Técnicas de Aplicación.

## Camino rápido

| Paso | Qué hacés | Qué ocurre |
| --- | --- | --- |
| 1. Traer material | `/ingest <url o ruta>` | El material queda en `knowledge/raw/` con `compiled: false` |
| 2. Compilar | `/wiki-compile` | El agente crea o actualiza artículos, enlaza, actualiza `_index.md` y marca las fuentes |
| 3. Auditar | `/wiki-lint` | Informe de salud en `knowledge/output/lint-YYYY-MM-DD.md` |
| 4. Consultar | Preguntás en el chat | El agente busca, lee y responde citando `[[enlaces]]` |
| 5. Conservar | Pedís guardar o convertir | La respuesta va a `knowledge/output/` o se vuelve artículo |

## Preguntar a la wiki

Escribís la pregunta como en un chat. El agente lee `_index.md`, busca con `wiki_search.py`, abre los artículos y responde citando con `[[enlaces]]`, que en Obsidian son enlaces navegables.

| Pregunta | Qué devuelve |
| --- | --- |
| «¿Qué dice el REBT sobre la caída de tensión?» | El artículo de la ITC-BT correspondiente, con el valor exacto |
| «¿Cómo lo interpreta la Guía-BT-52?» | El artículo de la guía: su criterio de interpretación **y** sus divergencias |
| «¿En qué se diferencian la Guía-BT-14 y la ITC-BT-14?» | El mapa de divergencias, con el valor que rige |

**La regla del vault:** el REBT tiene siempre la autoridad. Las Guías Técnicas son de carácter **no vinculante** (art. 29 del RD 842/2002) y el texto consolidado del BOE manda; donde discrepan, está anotado en el artículo de la guía y recopilado en el mapa.

Si el dato no está en la wiki pero sí en una fuente de `raw/`, el agente responde desde la fuente y te ofrece compilarla. Si no está en ninguno, te lo dice: no inventa.

Para buscar sin pasar por el chat:

```bash
python knowledge/tools/wiki_search.py search "caída de tensión" -n 5
python knowledge/tools/wiki_search.py index          # solo si querés forzar la reconstrucción
```

## Estado del vault

| Qué | Cuánto | Nota |
| --- | --- | --- |
| Fuentes en `raw/` | 100 | Con figuras (`knowledge/raw/imgs/`) y CSV de tablas (`knowledge/raw/tablas/`) que las fuentes referencian |
| Artículos | 98 | 52 de las ITC-BT, 33 de las guías técnicas, 13 de formularios y normativa |
| Entradas en `_index.md` | 98 | Sin links rotos y sin artículos fuera del índice |
| Divergencias guía ↔ ITC-BT | 223 | Cada una con el cierre «Prevalece la ITC-BT-XX» |
| Guías técnicas del REBT | 27 | De las 30 publicadas por el ministerio: 22 ITC con guía + las 4 que no la tienen, más la guía del RD y los anexos |

## El REBT en este vault

- **52 artículos de ITC-BT** (ITC-BT-01 a 52) con el texto consolidado del BOE.
- **33 artículos de guía técnica**: las 27 Guías Técnicas de Aplicación, la guía del RD 842/2002, los cuatro anexos (códigos IP/IK, caídas de tensión, cortocircuito, verificación) y la Nota de Interpretación sobre separación galvánica.
- **Un mapa con las 223 divergencias**, agrupadas por instrucción, con la tabla resumen y el detalle de cada una.
- **`tools/guia_rebt/`**: el pipeline que regenera el corpus desde los PDF oficiales del ministerio. `indice.json` lleva el `sha256` de cada PDF, así que avisa cuando se publica una edición nueva de una guía.

## Qué hay acá

| Ruta | Qué es |
| --- | --- |
| `AGENTS.md` | El contrato: estructura, reglas y formatos. Es lo primero que lee el agente. |
| `.opencode/commands/` | Los tres comandos: `/ingest`, `/wiki-compile`, `/wiki-lint`. |
| `knowledge/raw/` | Material en bruto. Solo lectura para el agente (salvo el campo `compiled`). |
| `knowledge/wiki/` | La wiki. Acá escribe el agente. |
| `knowledge/output/` | Respuestas e informes que vale la pena conservar. |
| `knowledge/tools/wiki_search.py` | Búsqueda de texto completo (SQLite FTS5, sin dependencias). |
| `tools/guia_rebt/` | Pipeline de regeneración del corpus de guías del REBT. |
| `odd/tasks/` | Documentos de seguimiento de los trabajos grandes. |

## Los tres comandos

| Comando | Qué hace | Qué escribe | Cuándo |
| --- | --- | --- | --- |
| `/ingest <url o ruta>` | Descarga o lee el material y lo deja en `raw/` con frontmatter | Un archivo en `knowledge/raw/` | Cada vez que aparece material nuevo |
| `/wiki-compile` | Convierte fuentes pendientes en artículos y los enlaza | `knowledge/wiki/`, `_index.md`, flag `compiled` | Después de uno o más `/ingest` |
| `/wiki-lint` | Audita la salud de la wiki | Informe en `knowledge/output/` (+ arreglos de índice) | Cada pocas compilaciones |

`/ingest` decide la carpeta según el tipo (artículo, transcripción, paper) y nunca inventa contenido: si no puede obtenerlo, te lo pide. Para YouTube usa `yt-dlp` **si está instalado**; si no, te pide la transcripción.

Los binarios que no son texto (PDF, capturas) van a `knowledge/inbox/`, que está ignorada por git. Lo que se versiona es el `.md` que queda en `raw/`.

## Herramientas de búsqueda

| Qué buscás | Herramienta |
| --- | --- |
| Artículos de la wiki | `wiki_search.py` (índice FTS5, reindexa solo si algo cambió) |
| Fuentes de `knowledge/raw/` o cualquier archivo | La herramienta de búsqueda nativa del agente |
| Símbolos y flujo de código | CodeGraph, solo para el Python del vault |

## Instalación (si vas a montar el kit en otro vault)

1. Copia `AGENTS.md`, `.opencode/commands/` y `knowledge/` a la raíz de tu vault de Obsidian.
2. Las carpetas vacías vienen con `.gitkeep`; si armas el vault de cero:
   ```
   knowledge/raw/{articles,transcripts,papers,imgs,tablas}
   knowledge/wiki/{concepts,people,tools}
   knowledge/output
   ```
3. Crea `knowledge/wiki/_index.md` con una sola línea: `# Índice de la wiki`.
4. Abre opencode desde la raíz del vault.

Requisitos: opencode y Python 3. Nada más: la búsqueda usa el módulo `sqlite3` de la biblioteca estándar. En Linux y macOS el intérprete suele ser `python3`; en Windows es `python`.

## Modelo

Los comandos no fijan modelo: usan el que tengas activo en opencode. Para fijar uno solo a un comando, agregá al frontmatter del archivo:

```yaml
---
description: Revisa la salud de la wiki y escribe un informe
model: proveedor/modelo
---
```

Los ids exactos salen de `opencode models`. Para cambiarlo en toda la sesión, usá `/models`.

## Problemas comunes

- **«Sin resultados» y hay artículos.** Ejecutá `index` a mano. Si se repite, revisá que los archivos estén en UTF-8.
- **«Aviso: se omitieron archivos ilegibles».** Alguno está guardado en ANSI (pasa con el Bloc de notas y con `Set-Content` de PowerShell). Volvé a guardarlo como UTF-8.
- **El agente intenta usar `grep` o `rg`.** Hoy ambos están en el PATH, pero no dependas de eso: usá la herramienta de búsqueda nativa, que es portable. Para los artículos, `knowledge/tools/wiki_search.py` es lo más rápido.
- **`knowledge/tools/wiki_index.sqlite` aparece como cambio.** No debería: está en `.gitignore`. Si lo ves, revisá que el `.gitignore` haya viajado con el kit.
- **Una fuente queda sin artículo.** `compiled: true` no garantiza que exista un artículo que la cite: verificá en los dos sentidos, pendientes y huérfanas.

## Consejos con modelos chicos

- Compilá de 1 a 3 fuentes por tanda; los modelos chicos pierden calidad con lotes grandes.
- Si el runtime corta los subagentes por cuota de uso, lanzalos en olas de 3 en vez de todos juntos.
- Después de las primeras compilaciones, revisá a mano un par de artículos para confirmar que respetan el formato.
- Ejecutá `/wiki-lint` cada pocas fuentes: es más barato corregir temprano.
- Obsidian es solo el visor: abrí `knowledge/wiki/` como parte de tu vault y usá la vista de grafo para ver los enlaces.
