---
description: Revisa la salud de la wiki y escribe un informe
---

Haz una auditoría de `knowledge/wiki/`. Reglas en AGENTS.md. NO corrijas nada automáticamente salvo lo indicado en el paso 3.

## 1. Comprobaciones

Mantén el espíritu LLM wiki: además de consistencia formal, busca oportunidades de que el conocimiento componga mejor (síntesis dispersa, conexiones faltantes, respuestas valiosas que deberían haberse integrado en la wiki).

Revisa todos los archivos `.md` de `knowledge/wiki/` (excepto `_index.md` para los puntos b y c):

a. **Enlaces rotos**: enlaces `[[nombre]]` que no corresponden a ningún archivo `nombre.md` en la wiki.
b. **Frontmatter**: faltan campos obligatorios (`title`, `type`, `sources`, `created`, `updated`), `type` no es `concept`, `person` o `tool`, o alguna ruta de `sources` no existe en `knowledge/raw/`.
c. **Huérfanos**: artículos que no aparecen en `_index.md` o a los que no enlaza ningún otro artículo.
d. **Índice**: entradas de `_index.md` que apuntan a archivos que no existen.
e. **Duplicados**: artículos que parecen tratar el mismo concepto con nombres distintos.
f. **Desactualizados**: artículos cuyo `updated` tiene más de 90 días mientras existen fuentes más recientes sobre el mismo tema.
g. **Fuentes sin compilar**: archivos de `knowledge/raw/` con `compiled: false`.
h. **Afirmaciones sin respaldo**: artículos con `sources` vacío.
i. **Tipos de divergencia**: cada viñeta de divergencia (el mapa y los artículos con sección `## Divergencias`) empieza por un tipo válido: `[conflicto]`, `[ampliacion]`, `[omision]` o `[desactualizacion]` (ver "Divergencias: taxonomía obligatoria" en AGENTS.md). Reportá las viñetas sin tipo, con tipo desconocido o con tipo que no corresponde a la relación descrita.
j. **Índice de fuentes desactualizado**: `knowledge/sources.md` no coincide con lo que correspondería generar. Comprobá con `python knowledge/tools/wiki_sources.py check` (sale con código 1 si está desactualizado). Ese archivo es generado: no lo edites a mano, regeneralo con `... wiki_sources.py build`.

## 2. Informe

Escribe el informe en `knowledge/output/lint-YYYY-MM-DD.md` (fecha de hoy) con una sección por comprobación y, en cada problema, el archivo afectado y la acción sugerida. Si una comprobación no encuentra nada, pon "OK".

## 3. Arreglos seguros

Solo estos arreglos puedes aplicarlos sin preguntar:
- Añadir al índice los artículos que faltan.
- Quitar del índice las entradas cuyo archivo no existe.

Todo lo demás (fusionar duplicados, borrar, reescribir) lo propones en el informe y esperas confirmación.

## 4. Resumen

Termina con un resumen de una línea por tipo de problema y la ruta del informe.

$ARGUMENTS
