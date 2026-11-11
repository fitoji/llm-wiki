---
title: Guía-BT-23 — Protección contra sobretensiones
type: concept
tags: [rebt, guia-tecnica, baja-tension, itc-bt-23, sobretensiones]
sources: [papers/2026-11-10-guia-bt-23-proteccion-contra-sobretensiones.md]
created: 2026-11-10
updated: 2026-11-10
---

# Guía-BT-23 — Protección contra sobretensiones

La Guía-BT-23 (noviembre de 2019, revisión 4, Ministerio de Industria y Turismo) desarrolla la [[itc-bt-23-instalaciones-interiores-o-receptoras-proteccion-contra-sobretensiones]] del REBT sobre sobretensiones transitorias. La ITC-BT-23 tiene autoridad: donde la guía añada o interprete, prevalece el texto consolidado del BOE.

## Puntos clave

- Objeto: protección frente a sobretensiones transitorias (descargas atmosféricas, conmutaciones, defectos de red); no trata el impacto directo del rayo ni las sobretensiones temporales por rotura del neutro.
- Situación natural: con red subterránea total basta la tensión soportada de la tabla 1; una línea aérea con conductores aislados y pantalla metálica a tierra en ambos extremos equivale a línea subterránea.
- Situación controlada: con línea aérea de conductores desnudos o aislados la protección atmosférica es necesaria en el origen de la instalación.
- Categorías de sobretensión, con tensión soportada a impulsos 1,2/50 µs en kV:

| Tensión nominal (kV) trifásica / monofásica | Cat. IV | Cat. III | Cat. II | Cat. I |
|---|---|---|---|---|
| 230/400 y 230 | 6 | 4 | 2,5 | 1,5 |
| 400/690 y 1000 | 8 | 6 | 4 | 2,5 |

- Dispositivos (UNE-EN 61643-11): tipo 1 para el impacto directo del rayo, tipo 2 para atmosféricas y de conmutación, tipo 3 para equipos sensibles; conductor de tierra de 16, 4 y 2,5 mm² para los tipos 1, 2 y 3.
- Criterio geográfico: se recomienda protección con 20 o más días de tormenta al año y es muy recomendable con 25 o más; en emplazamientos elevados, el nivel inmediato superior al de la provincia.

## Detalles

La estrategia es la protección en cascada con tres niveles (basta, media y fina). El nivel de protección Up debe ser inferior a la categoría del equipo (categoría II → Up ≤ 2,5 kV); en red TT 230/400 V la tensión máxima de servicio permanente es 253 V (230 × 1,1) y la In del tipo 2 no baja de 5 kA 8/20 µs.

La guía conecta los descargadores según el régimen de neutro (en TT e IT entre cada conductor, incluido el neutro, y la tierra; en TN-S entre fases y el conductor de protección; en TN-C entre fases y el neutro), coordina los dispositivos en cascada y exige la protección aguas arriba que indique el fabricante cuando el dispositivo no la incorpore.

## Divergencias con la ITC-BT-23

- La guía (1) amplía el alcance con el artículo 16.1 del Reglamento: incluye las instalaciones receptoras de fines especiales (caravanas, marinas, ferias, obra, agrícolas, eólicas) y el criterio de 50 m de proximidad; la ITC-BT-23 no lo recoge. Prevalece la ITC-BT-23.
- La guía (1) aclara que no se tratan las sobretensiones temporales y que las de maniobra son inferiores a las atmosféricas; la ITC-BT-23 no lo dice. Prevalece la ITC-BT-23.
- La guía (3) remite al CTE (SUA 8 y anejo B) para el sistema externo de protección contra el rayo, que la ITC-BT-23 no menciona. Prevalece la ITC-BT-23.
- La guía (3.2) enumera las situaciones controladas que obligan a protección según la UNE EN 62305-2 (vida humana, animales, servicios públicos, locales de la ITC-BT-28, actividad industrial no interrumpible) y añade el criterio de días de tormenta y la nueva ITC-BT-52; la ITC-BT-23 no las enumera. Prevalece la ITC-BT-23.
- La guía (3.2) exige tipo 1 en edificios con pararrayos (CTE SUA 8), lo recomienda en 50 m alrededor de un pararrayos, fija las reglas de instalación en TT (aguas arriba del diferencial o aguas abajo con tipo S) y un segundo tipo 2 cada 10 m (UNE-CLC TS 61643-12); la ITC-BT-23 no lo contiene. Prevalece la ITC-BT-23.
- La guía (3.2 y 4) añade las tablas A y B de situaciones obligatorias y recomendadas y los apartados A a D sobre tipos de dispositivo, límites de In e Iimp y secciones de tierra; la ITC-BT-23 solo regula la selección de materiales. Prevalece la ITC-BT-23.

## Relacionado

- [[itc-bt-23-instalaciones-interiores-o-receptoras-proteccion-contra-sobretensiones]]
- [[reglament-electrotecnic-baixa-tensio]]
- [[itc-bt-28-instalaciones-en-locales-de-publica-concurrencia]]
- [[itc-bt-52-instalaciones-con-fines-especiales-infraestructura-para-la-recarga-de-vehiculos-electricos]]
- [[itc-bt-24-instalaciones-interiores-o-receptoras-proteccion-contra-los-contactos-directos-e-indirectos]]
