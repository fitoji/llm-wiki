# Compilación del REBT desde `inbox/rebt_salida`

Objetivo: convertir las 54 fuentes raw del REBT (ingesta `2026-11-10-rebt-*`) en artículos de la wiki, uno por ITC-BT (con actualización de artículos existentes que ya cubren ITC-BT-25/26/27).
Branch: main · Entrega: commits directos (convención del vault) · Verificación: revisión estructural de frontmatter + `_index.md` completo.

## Specs

- S1: "procesa inbox" (petición del usuario, 2026-11-10) — procesar todo el material de `knowledge/inbox/rebt_salida/` (54 md: reglamento + ITC-BT-01..52 + anexo).
- S2: Cada ITC-BT-XX produce un artículo en `knowledge/wiki/concepts/`, español, formato del vault; tipos `concept`; sources rutas relativas a `knowledge/raw/`.
- S3: No duplicar artículos existentes: ITC-BT-25/26/27 actualizan los artículos existentes (regla 3 del vault): añaden la fuente BOE a `sources`, sin borrar contenido.
- S4: `compiled: false → true` en las fuentes consumidas (único campo editable de raw).
- S5: `knowledge/wiki/_index.md` se actualiza en el mismo paso que los artículos (regla 8), sin duplicados (regla 3).
- S6: No inventar datos: todo afirmado en el artículo debe salir de la fuente raw correspondiente.
- S7: `[[ITC-BT-XX]]` como marcador de enlace entre ITCs se resuelve al slug real poster-compilación (por el orquestador).

## Tasks

- T1 (S1,S2): B1 — ingesta raw de 54 fuentes [hecho, commit `feat: ingiere el REBT...`] ruta inline
- T2 (S2,S4,S6): B1 write — art. itc-bt-01-terminologia + update reglament-electrotecnic-baixa-tensio (fuentes 00+zz) — delegado
- T3: B2 write — ITC 02,03,04 — delegado
- T4: B3 write — ITC 05,06,08,09,10,11 — delegado
- T5: B4 write — ITC 12..19 — delegado
- T6: B5 write — ITC 20,21,22,23 — delegado
- T7: B6 write — ITC 24..28 + updates existentes (instalaciones-interiores-viviendas-bt, puntos-utilizacion-vivienda, conductores-y-ejecucion-instalacion-interior, toma-de-tierra-edificios-viviendas, locales-banera-ducha-bt) — delegado
- T8: B7 write — ITC 29..35 — delegado
- T9: B8 write — ITC 36..44 — delegado
- T10: B9 write — ITC 45..51 — delegado
- T11: B10 write — ITC 52 — delegado
- T12 (S5,S7): postproceso del orquestador: resolver `[[ITC-BT-XX]]`, actualizar `_index.md`, verificar — inline
- T13: commit artículos + espejo memoria + resumen sesión

## Log

- L1: "procesa inbox" — petición original del usuario (2026-11-10); interpretada como ingerir + compilar todo el material del inbox según `/ingest` + `/wiki-compile` del vault.
- L2: Ingesta ejecutada: 54 archivos → `knowledge/raw/papers/2026-11-10-rebt-*.md`, frontmatter del vault (author BOE, source BOE-A-2002-18099), contenido verbatim, `compiled: false`. Commit `feat: ingiere el REBT completo...`.
- L3: Compilación ejecutada (T2-T11): 52 artículos nuevos en `knowledge/wiki/concepts/` (incluido `itc-bt-01-terminologia`), 6 artículos existentes con fuentes BOE añadidas (reglament-electrotecnic, toma-de-tierra, instalaciones-interiores, puntos-utilizacion, conductores, locales-banera), raws `compiled: true`, marcadores `[[ITC-BT-XX]]` resueltos a los slugs reales. Notas: la ITC-BT-07 no tenía batch asignado y se compiló en un writer aparte (B11); los writers de ITC-02/03/04 omitieron `sources:` y se corrigió inline.
- L4: Postproceso (T12): `knowledge/wiki/_index.md` regenerado con 63 entradas, todas resueltas a archivos reales y ningún artículo fuera del índice; `wiki_index.sqlite` reindexado (63 artículos); búsqueda funciona. El anti-duplicado de S3 se resolvió como pedía: los writers de ITC-25/26/27 cubrieron los ángulos no tratados por los artículos Guía y añadieron las fuentes a los existentes.
- L5: Commits: `feat: compila la wiki del REBT completo (52 articulos ITC-BT-01 a 52)` (114 archivos) + `chore: doc de seguimiento...`. Verificación estructural: 63 entradas en índice, raws pendientes con `compiled: false`: 0, worktree limpio.
- L6: El usuario confirmó borrar el inbox: eliminado `knowledge/inbox/rebt_salida/` (cache/tablas/imgs/originales) y su `.DS_Store`. Inbox vacío; el material queda ingerido y compilado en el vault.
