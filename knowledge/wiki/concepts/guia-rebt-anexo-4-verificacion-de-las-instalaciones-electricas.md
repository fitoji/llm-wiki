---
title: Guía REBT Anexo 4 — Verificación de las instalaciones eléctricas (edición sep 03, rev 1)
type: concept
tags: [rebt, guia-tecnica, baja-tension, verificaciones, mediciones]
sources: [papers/2026-11-10-guia-rebt-anexo-4-verificacion-de-las-instalaciones-electricas.md]
created: 2026-11-10
updated: 2026-11-10
---

# Guía REBT Anexo 4 — Verificación de las instalaciones eléctricas (edición sep 03, rev 1)

El Anexo 4 de las Guías Técnicas de Aplicación del REBT (edición de septiembre de 2003, revisión 1) resume las verificaciones de los instaladores autorizados antes de la puesta en servicio: por examen y con medidas y ensayos. Guía no vinculante: prevalecen el RD 842/2002 y sus ITC-BT, único texto vinculante (BOE).

## Puntos clave

- Dos fases previas a la puesta en servicio: verificación por examen, sin medidas y con la instalación sin tensión, y verificaciones mediante medidas o ensayos; el alcance se detalla en la ITC-BT-19 y la UNE 20460-6-61, y en la ITC-BT-18 para la puesta a tierra.
- El examen comprueba la conformidad del material con el proyecto, su instalación correcta, los daños visibles, las protecciones frente a contactos directos e indirectos, el calibrado de protecciones, los cortafuegos y la accesibilidad.
- Nueve comprobaciones: continuidad de conductores de protección, resistencia de puesta a tierra, resistencia de aislamiento, aislamiento de suelos y paredes, rigidez dieléctrica, fugas de corriente, impedancia de bucle, disparo de los diferenciales y secuencia de fases.
- Aislamiento mínimo (tabla 1 del anexo), para canalizaciones de hasta 100 m; por encima se fracciona en tramos de unos 100 m y el mínimo se divide por la longitud en hectómetros:

| Tensión nominal | Ensayo (V, continua) | Aislamiento (MΩ) |
|---|---|---|
| MBTS / MBTP | 250 | ≥ 0,25 |
| Hasta 500 V | 500 | ≥ 0,5 |
| Más de 500 V | 1000 | ≥ 1,0 |

- Rigidez dieléctrica: un minuto a 2U + 1000 V y 50 Hz, con mínimo de 1.500 V; no se ensaya en locales con riesgo de incendio o explosión.
- Impedancia de bucle: Icc ≤ Ia con los tiempos de interrupción de la ITC-BT-24 (TN: 0,4 / 0,2 / 0,1 s; IT: 0,4-0,8 / 0,2-0,4 / 0,1-0,2 s).
- Puesta a tierra: telurómetro con tres electrodos en línea separados 20 m, revisión anual en la época más seca y examen al descubierto cada cinco años.

## Detalles

El anexo detalla el instrumental: ohmímetro con 200 mA en continua para la continuidad de conductores de protección y megóhmetro con 1 mA para el aislamiento; en suelos y paredes, tres medidas por superficie importante.

Los casos particulares remiten a otras ITC: en quirófanos la impedancia al embarrado no excede 0,2 Ω y la de las partes metálicas 0,1 Ω, con suelos antielectrostáticos de hasta 1 MΩ (ITC-BT-38); en baños, la bañera o ducha aislada exige 100 kΩ (ITC-BT-27).

En esquemas TT se cumple R_A·I_a ≤ U_A, con tensión de contacto límite de 50 V (24 V en alumbrado público). Las medidas de bucle y de fuga se hacen en tensión, con los diferenciales aguas arriba puentados; en los diferenciales se prueba a IΔn/2 (no dispara), IΔn (<200 ms), 2IΔn (<150 ms) y 5IΔn (<40 ms).

## Divergencias con el REBT

- Quién comprueba la puesta a tierra: el anexo (apartado 2.2) indica que debe comprobarla el Director de la Obra o el Instalador Autorizado. La ITC-BT-18 (apartado 12) dice «Director de la Obra o Empresa instaladora», tras el RD 560/2010. Prevalece la ITC-BT-18.
- Corriente de fuga medida: el anexo (apartado 2.6) exige valores medidos inferiores a la mitad de la sensibilidad del diferencial. La ITC-BT-19 (apartado 2.9) solo fija que no superen la sensibilidad del diferencial instalado. Prevalece la ITC-BT-19.
- Alcance: el anexo lo sitúa en la ITC-BT-19 y la UNE 20460-6-61, sin mencionar inspecciones. La ITC-BT-05 desarrolla los artículos 18 y 20 del REBT, regula las inspecciones iniciales y periódicas y clasifica los defectos en muy graves, graves y leves. Prevalece la ITC-BT-05.

## Relacionado

- [[reglament-electrotecnic-baixa-tensio]]
- [[ITC-BT-05]]
- [[ITC-BT-18]]
- [[ITC-BT-19]]
- [[ITC-BT-24]]
- [[ITC-BT-27]]
- [[ITC-BT-38]]
