# Compilación de las Guías Técnicas del REBT desde `inbox/guia_rebt`

Objetivo: ingerir el corpus `guia_rebt` (39 md, ~1.3 MB) como fuentes raw y compilar artículos de la wiki por cada guía, comparando cada guía con su ITC-BT y **anotando divergencias en el artículo de la guía** (el REBT tiene siempre la autoridad).
Branch: master · Entrega: commits directos (convención del vault) · Verificación: revisión estructural (frontmatter, `_index.md`, sección de divergencias presente en cada artículo de guía).

## Specs

- S1: "revisa inbox, agregue las guias de la bt, a veces hay contradicciones con las itc bt del rebt, el rebt siempre tiene la autoridad, pero me interesa que apuntes donde hay divergencias en la guia" (petición del usuario, 2026-11-10, verbatim).
- S2: Ingesta de los 39 md del corpus a `knowledge/raw/papers/` con frontmatter del vault, autor "Ministerio de Industria y Turismo — Guías Técnicas de Aplicación del REBT", source = fuente_pdf del corpus, `compiled: false`.
- S3: Un artículo por guía de ITC-BT (`guia-bt-XX-<tema>`) con: puntos clave, detalles **solo del raw**, `## Divergencias con la ITC-BT-XX` (o "Sin divergencias detectadas") donde se cite qué dice la guía, qué dice la ITC-BT (texto consolidado BOE) y la nota de que prevalece la ITC-BT.
- S4: Artículos nuevos también para: guía del RD + intro + índice (`guia-rebt-introduccion`, 3 fuentes), Anexo 1 (códigos IP/IK), Anexo 2 (caídas de tensión), Anexo 3 (cortocircuito), Anexo 4 (verificación), y la nota ZZ (`nota-interpretacion-separacion-galvanica`).
- S5: Los 5 artículos existentes derivados de las guías 25/26/27 (instalaciones-interiores-viviendas-bt, puntos-utilizacion-vivienda, conductores-y-ejecucion-instalacion-interior, toma-de-tierra-edificios-viviendas, locales-banera-ducha-bt) reciben: fuente del corpus nuevo en `sources` (append) y su sección de divergencias; no se reescribe su contenido.
- S6: No inventar datos: toda divergencia citada debe estar en los dos raws comparados (guía e ITC-BT), con referencias a sección/punto.
- S7: No referenciar imágenes/CSV; las tablas del corpus van como markdown inline tal como están en el md.
- S8: `_index.md` actualizado en el mismo paso (regla 8); marcadores `[[ITC-BT-XX]]` resueltos a slugs reales; enlaces recíprocos ITC↔guía.
- S9: Higiene Engram: tras la tanda de writers, `mem_doctor` y cierre de sesiones huérfanas antes de guardar el resumen (AGENTS.md, sección Memoria).

## Tasks

- T1 (S2): ingesta raw de 39 fuentes [inline] — commit
- T2-T18 (S3,S4,S7): writers en paralelo, batches por tamaño (~90 KB guía por writer)
- T19 (S5): divergencias en los 5 artículos existentes 25/26/27 (2 writers)
- T20 (S8): postproceso inline: resolver `[[ITC-BT-XX]]`, enlaces recíprocos, `_index.md`, reindexar, verificar
- T21: commits + espejo memoria + resumen sesión + higiene Engram (S9)

## Log

- L1: "revisa inbox, agregue las guias de la bt, a veces hay contradicciones con las itc bt del rebt, el rebt siempre tiene la autoridad, pero me interesa que apuntes donde hay divergencias en la guia" — petición original (2026-11-10).
- L2: Inventario del inbox: `guia_rebt/` con 38 md (27 guías ITC-BT sin guías previas + guía RD + 4 anexos + intro + índice + nota ZZ), 381 csv, 123 png, indice.json. Los raws previos de BT-25/26/27 (OCR desde tecnicas-jordi, sin tablas) ya existían con `compiled: true`; el corpus nuevo trae tablas inline y se ingesta también como fuente adicional.
- L3: T1 — ingesta de las 38 fuentes raw (`knowledge/raw/papers/2026-11-10-guia-*.md`, autor Ministerio, `compiled: false`), commit `1f84b7d`.
- L4: T2-T18 — compilación por 17 batches en 6 olas (el runtime limita el uso free de modelos: waves de 3, con reintentos individuales cuando la cuota cae). 33 artículos nuevos: 27 `guia-bt-XX-*`, `guia-rebt-introduccion` (intro+índice+guía del RD), 4 anexos y `nota-interpretacion-separacion-galvanica`.
- L5: T19 — los 5 artículos preexistentes derivados de las guías 25/26/27 (instalaciones-interiores-viviendas-bt, puntos-utilizacion-vivienda, conductores-y-ejecucion-instalacion-interior, toma-de-tierra-edificios-viviendas, locales-banera-ducha-bt) reciben la fuente del corpus y su sección `## Divergencias`.
- L6: T20 — postproceso inline: 19 artículos con marcadores `[[ITC-BT-XX]]` resueltos a slugs reales, 27 artículos ITC con enlace recíproco a su guía, 6 enlaces generales desde el artículo del REBT, `_index.md` regenerado con 96 entradas (sin links rotos, ningún artículo fuera) y `wiki_index.sqlite` reindexado (96 artículos).
- L7: T21 — **223 divergencias** registradas en total (cada una cierra con "Prevalece la ITC-BT-XX."). Patrón dominante: las guías son ediciones de 2003-2024 y el texto consolidado del BOE (RD 298/2021, RD 770/2025, RD 1053/2014, RD 542/2020, RD 560/2010, RD 244/2019, Resolución 20-03-2025) las dejó desactualizadas en requisitos y en normas citadas. Divergencias destacadas: guía BT-14 exige neutro de igual sección que las fases (la ITC fija 50 %); guía BT-40 desarrolla un apartado derogado por el RD 244/2019; guía BT-52 conserva conectores TESLA con vigencia vencida; la Nota de Interpretación sobre separación galvánica no existe en la ITC-BT-40 consolidada.
