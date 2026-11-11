---
title: Guía-BT-10 — Previsión de cargas para suministros en baja tensión
type: concept
tags: [rebt, guia-tecnica, baja-tension, itc-bt-10, prevision-cargas]
sources: [papers/2026-11-10-guia-bt-10-prevision-de-cargas-para-suministros-en-baja-tension.md]
created: 2026-11-10
updated: 2026-11-10
---

# Guía-BT-10 — Previsión de cargas para suministros en baja tensión

La Guía-BT-10 (edición de septiembre de 2003, revisión 1, Ministerio de Industria y Turismo) desarrolla con ejemplos y tablas la previsión de cargas para suministros en baja tensión. Acompaña a la [[itc-bt-10-prevision-de-cargas-para-suministros-en-baja-tension]]: es orientativa y la ITC-BT-10 del BOE tiene autoridad y prevalece ante cualquier discrepancia.

## Puntos clave

- Garantiza la conexión y el uso seguro de los receptores y evita que el crecimiento de la demanda obligue a modificar la instalación; también dimensiona las líneas de distribución.
- Las cifras son mínimos teóricos: si se conoce la demanda real, se utiliza cuando supere el mínimo.
- Electrificación básica: necesidades primarias sin obras posteriores. Elevada: uso electrodoméstico superior, calefacción eléctrica o aire acondicionado, o superficie útil superior a 160 m².
- Potencia mínima en obra nueva: 5 750 W a 230 V por vivienda, y 9 200 W con electrificación elevada; la potencia contratada por cada usuario es independiente.
- Carga del conjunto de viviendas = media aritmética de las potencias máximas previstas × coeficiente de simultaneidad de la tabla 1.
- Mínimos: locales comerciales y oficinas 100 W/m² (3 450 W por local); garajes 10 W/m² natural y 20 W/m² forzada (3 450 W); concentración de industrias 125 W/m² (10 350 W por local).

| N.º viviendas | Simultaneidad |
|---|---|
| 4 | 3,8 |
| 12 | 9,9 |
| 20 | 14,8 |
| n > 21 | 15,3 + (n − 21) × 0,5 |

| Electrificación | Potencia (W) / IGA (A) |
|---|---|
| Básica | 5 750 / 25 y 7 360 / 32 |
| Elevada | 9 200 / 40, 11 500 / 50 y 14 490 / 63 |

## Detalles

Los lugares de consumo son edificios de viviendas, comerciales u oficinas, de industria específica y de concentración de industrias. Para las viviendas la guía aplica, además de los 160 m², criterios que la instrucción no enumera: automatización, secandra, más de 30 puntos de alumbrado, más de 20 tomas de uso general y más de 6 de baños y cocina, con remisión a la [[itc-bt-25-instalaciones-interiores-en-viviendas-numero-de-circuitos-y-caracteristicas]]. Con tarifa nocturna el coeficiente de simultaneidad es 1; el ejemplo resuelto da 70,544 kW para doce viviendas de 100 m² y dos de 200 m².

Para servicios generales ofrece la tabla A de elevadores según la norma ITE-ITA (de 4,5 kW a 46 kW según carga) y estima el alumbrado de portal en 15 W/m² con incandescentcia o 8 W/m² con fluorescencia, y en 7 W/m² o 4 W/m² en la escalera.

## Divergencias con la ITC-BT-10

- La guía (2.1.2) omite la recarga de vehículo eléctrico en unifamiliares como condición de electrificación elevada, que sí consta en la ITC-BT-10, y añade criterios no enumerados en ella: automatización, secandra, número de puntos de utilización y remisión a la ITC-BT-25. Prevalece la ITC-BT-10.
- La guía omite el capítulo 5 de la ITC-BT-10 (recarga de vehículo eléctrico: 3 680 W por el 10 % de las plazas) y remite a los capítulos 2, 3 y 4, frente a los 2, 3, 4 y 5 consolidados. Prevalece la ITC-BT-10.
- La guía no recoge la modificación por la disposición final 4 del RD 1053/2014 (BOE-A-2014-13681), con efectos de 30 de junio de 2015, que sí consta en el texto consolidado. Prevalece la ITC-BT-10.
- La guía añade una tabla de escalones de potencia prevista y calibre del IGA que la ITC-BT-10 no contiene. Prevalece la ITC-BT-10.
- La guía añade criterios de cálculo ausentes de la ITC-BT-10 (elevadores, alumbrado de servicios generales, normativa contra incendios en garajes) y generaliza el uso de la demanda real, que la ITC-BT-10 limita a edificios comerciales o industriales. Prevalece la ITC-BT-10.

## Relacionado

- [[itc-bt-10-prevision-de-cargas-para-suministros-en-baja-tension]]
- [[reglament-electrotecnic-baixa-tensio]]
- [[guia-bt-13-cajas-generales-de-proteccion]]
- [[guia-bt-14-linea-general-de-alimentacion]]
- [[guia-bt-16-contadores-ubicacion-y-sistemas-de-instalacion]]
- [[itc-bt-25-instalaciones-interiores-en-viviendas-numero-de-circuitos-y-caracteristicas]]
- [[itc-bt-52-instalaciones-con-fines-especiales-infraestructura-para-la-recarga-de-vehiculos-electricos]]
