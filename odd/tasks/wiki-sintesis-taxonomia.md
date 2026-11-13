# Síntesis transversal y taxonomía de divergencias del REBT

Objetivo: precisión y síntesis del conocimiento del vault. (A) Clasificar las 223 divergencias guía↔ITC-BT con una taxonomía de 4 tipos y aplicarla al mapa y a los 37 artículos de guía. (B) Crear 3 artículos transversales que integran varias fuentes.
Branch: feat/wiki-sintesis-taxonomia · Entrega: commits por unidad de trabajo · Verificación: revisión estructural (frontmatter, `_index.md`, formato de tags, recuento 223) + `wiki_search.py`.

## Specs

- S1: "sigamos tu recomendacion" (petición del usuario, 2026-11-13, verbatim). La recomendación aceptada: "empezar por #3 y #5 juntas — sintetizar 3–4 temas transversales (caída de tensión, protección diferencial, criterios de puesta a tierra, secciones de protección) y taggear las 223 divergencias."
- S2: Taxonomía de 4 tipos de brecha, definidos por la relación entre la guía y el texto consolidado de la ITC-BT. Se alinea con los "Patrones comunes" que el propio mapa ya describe en prosa:
  - `conflicto` — la guía y la ITC-BT fijan valores o requisitos incompatibles, sin desfase normativo de por medio. Prevalece el valor de la ITC-BT.
  - `ampliacion` — la guía desarrolla criterios, valores, tablas o recomendaciones que la ITC-BT no recoge; la ITC no se pronuncia.
  - `omision` — la ITC-BT exige o recoge algo que la guía no menciona.
  - `desactualizacion` — desfase normativo o temporal: la guía (o el propio texto consolidado) cita una norma, requisito o terminología que la otra parte o un RD posterior ya superó o derogó.
- S3: Regla de clasificación, en este orden: (1) ¿una de las dos partes cita algo que la otra o un RD posterior superó/derogó? → `desactualizacion`; (2) ¿la ITC-BT exige algo que la guía no menciona? → `omision`; (3) ¿la guía y la ITC-BT fijan lo mismo con valores incompatibles? → `conflicto`; (4) ¿solo la guía desarrolla algo que la ITC-BT no recoge? → `ampliacion`.
- S4: Formato: cada ítem de divergencia lleva el tag al inicio de su viñeta, en ASCII y sin acentos: `[conflicto]`, `[ampliacion]`, `[omision]`, `[desactualizacion]`. Ej.: `- [ampliacion] **Sección mínima del conductor de tierra.** La Guía-BT-26 ...`.
- S5: El mapa `divergencias-guias-tecnicas-rebt-vs-itc-bt.md` queda completo con los 223 ítems etiquetados y reporta la distribución por tipo, que debe sumar 223.
- S6: Los 37 artículos con sección `## Divergencias` etiquetan sus viñetas con el mismo formato y la misma taxonomía. Un ítem que tenga homólogo en el mapa debe recibir el mismo tipo.
- S7: `AGENTS.md` define la taxonomía y la obligatoriedad del tag; `.opencode/commands/wiki-lint.md` añade la comprobación de que toda viñeta de divergencia lleva un tipo válido.
- S8: Tres artículos transversales nuevos, cada uno integrando varias fuentes de `knowledge/raw/` y enlazando con los artículos existentes:
  - `caida-de-tension` — límites, cálculo, compensación entre tramos y tablas de longitudes.
  - `proteccion-diferencial-selectividad` — 30 mA, selectividad 3×, tipo S, ubicación respecto a protecciones y sobretensiones.
  - `esquemas-conexion-neutro-masas` — esquemas TT/TN/IT, neutro y masas, y su relación con la protección.
- S9: `_index.md` actualizado en el mismo paso (regla 8 del vault); enlaces recíprocos entre los nuevos artículos y los que integran.

## Tasks

- T1 (S1): crear este documento y su espejo Engram. [inline]
- T2 (S2,S3,S4,S7): taxonomía en `AGENTS.md` + comprobación en `wiki-lint.md`. [inline]
- T3 (S5): etiquetar las 223 viñetas del mapa + distribución por tipo. [delegado]
- T4 (S6): etiquetar las viñetas de los 37 artículos con sección de divergencias, en olas de 3. [delegado]
- T5 (S8): escribir los 3 artículos transversales. [delegado]
- T6 (S9): `_index.md`, enlaces recíprocos, reindexado y verificación estructural. [inline]

## Log

- L1: "sigamos tu recomendacion" — petición original (2026-11-13).
- L2: Verificación previa del mapa completo (428 líneas): el mapa ya clasifica en prosa sus "Patrones comunes" en 6 apartados, que colapsan en los 4 tipos de S2 (patrones 1 y 4 → `desactualizacion`; 2 → `ampliacion`; 3 → `conflicto`; 5 → `omision`). No existe hoy ningún tag por ítem. 38 archivos tienen sección `## Divergencias` (el mapa + 37 artículos).
