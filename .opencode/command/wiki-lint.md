---
description: Revisa la salud de la wiki y escribe un informe
---

Haz una auditoría de `knowledge/wiki/`. Reglas en AGENTS.md. NO corrijas nada automáticamente salvo lo indicado en el paso 3.

## 1. Comprobaciones

Revisa todos los archivos `.md` de `knowledge/wiki/` (excepto `_index.md` para los puntos b y c):

a. **Enlaces rotos**: enlaces `[[nombre]]` que no corresponden a ningún archivo `nombre.md` en la wiki.
b. **Frontmatter**: faltan campos obligatorios (`title`, `type`, `sources`, `created`, `updated`).
c. **Huérfanos**: artículos que no aparecen en `_index.md` o a los que no enlaza ningún otro artículo.
d. **Índice**: entradas de `_index.md` que apuntan a archivos que no existen.
e. **Duplicados**: artículos que parecen tratar el mismo concepto con nombres distintos.
f. **Desactualizados**: artículos cuyo `updated` tiene más de 90 días mientras existen fuentes más recientes sobre el mismo tema.
g. **Fuentes sin compilar**: archivos de `knowledge/raw/` con `compiled: false`.
h. **Afirmaciones sin respaldo**: artículos con `sources` vacío.

## 2. Informe

Escribe el informe en `knowledge/output/lint-AAAA-MM-DD.md` (fecha de hoy) con una sección por comprobación y, en cada problema, el archivo afectado y la acción sugerida. Si una comprobación no encuentra nada, pon "OK".

## 3. Arreglos seguros

Solo estos arreglos puedes aplicarlos sin preguntar:
- Añadir al índice los artículos que faltan.
- Quitar del índice las entradas cuyo archivo no existe.

Todo lo demás (fusionar duplicados, borrar, reescribir) lo propones en el informe y esperas confirmación.

## 4. Resumen

Termina con un resumen de una línea por tipo de problema y la ruta del informe.

$ARGUMENTS
