---
title: ITC-BT-10 — Previsión de Cargas para Suministros en Baja Tensión
type: concept
tags: [rebt, baja-tension, itc-bt-10, prevision-cargas, simultaneidad]
sources: [papers/2026-11-10-rebt-itc-bt-10-prevision-de-cargas-para-suministros-en-baja-tension.md]
created: 2026-11-10
updated: 2026-11-10
---

# ITC-BT-10 — Previsión de Cargas para Suministros en Baja Tensión

Establece la potencia a prever por vivienda y edificio (viviendas, servicios generales, locales comerciales, garajes y recarga de vehículos eléctricos) según el grado de electrificación.

## Puntos clave

- Clasificación de lugares de consumo: edificios de viviendas, comerciales o de oficinas, destinados a industria específica, a concentración de industrias, y aparcamientos con infraestructura de recarga de vehículos eléctricos.
- Electrificación básica: cobertura de las necesidades primarias de uso sin obras posteriores; electrificación elevada: uso electrodoméstico mayor, calefacción eléctrica o aire acondicionado, superficie útil superior a 160 m², o recarga de vehículo eléctrico en unifamiliares, o combinaciones.
- Potencia a prever en construcción nueva: como mínimo 5 750 W a 230 V por vivienda; con electrificación elevada, no inferior a 9 200 W.
- La potencia a prever se corresponde con la capacidad máxima de la instalación, definida por la intensidad asignada del interruptor general automático (ITC-BT-25).
- Servicios generales del edificio: se suman sin factor de reducción (simultaneidad = 1).
- Locales comerciales y oficinas: mínimo 100 W por m² y planta, con un mínimo de 3 450 W a 230 V por local y simultaneidad 1.
- Garajes: 10 W/m² y planta con ventilación natural y 20 W/m² con ventilación forzada, mínimo 3 450 W a 230 V y simultaneidad 1.
- Concentración de industrias: mínimo 125 W por m² y planta, mínimo por local 10 350 W a 230 V, simultaneidad 1.

| N.º viviendas | Coef. simultaneidad |
|---|---|
| 1 | 1 |
| 2 | 2 |
| 3 | 3 |
| 4 | 3,8 |
| 5 | 4,6 |
| 10 | 8,5 |
| 20 | 14,8 |
| n > 21 | 15,3 + (n − 21) × 0,5 |

Para tarifa nocturna, la simultaneidad es 1 (coeficiente igual al número de viviendas).

## Detalles

La carga de un conjunto de viviendas se obtiene multiplicando la media aritmética de las potencias máximas previstas por el coeficiente de simultaneidad de la tabla. El promotor, propietario o usuario fija esta potencia con la Empresa Suministradora; la potencia a prever no debe confundirse con la potencia a contratar por cada usuario, que depende de la utilización de la instalación. Si la NBE-CPI-96 exige ventilación forzada para evacuación de humos de incendio en garajes, la previsión de cargas se estudia de forma específica.

**Recarga de vehículos eléctricos.** En unifamiliares con infraestructura de recarga se considera grado de electrificación elevado. En plazas colectivas de edificios o conjuntos en propiedad horizontal, la previsión resulta de multiplicar 3 680 W por el 10 % del total de plazas construidas, aplicar el factor de simultaneidad que corresponda y sumar el resultado a la previsión del resto de la instalación, según el esquema y la disponibilidad de protección de la línea general de alimentación que prevé la ITC-BT-52; el proyectista puede prever mayor potencia instalada si dispone de datos que lo justifiquen.

**Uso de la previsión.** La carga total prevista es la base para calcular los conductores de las acometidas y las instalaciones de enlace. Para edificios comerciales o de oficinas la demanda determina la carga a prever, nunca por debajo de los valores mínimos citados.

**Suministros monofásicos.** Las distribuidoras deben efectuar, a solicitud del cliente, suministro apto para cualquier receptor monofásico de potencia ≤ 5 750 W a 230 V, hasta un máximo de 14 490 W a 230 V.

La instrucción quedó modificada, con efectos del 30 de junio de 2015, por la disposición final 4 del Real Decreto 1053/2014, de 12 de diciembre (BOE-A-2014-13681).

## Relacionado
- [[guia-bt-10-prevision-de-cargas-para-suministros-en-baja-tension]] — guía técnica de aplicación (no vinculante: prevalece la ITC-BT-10)

- [[itc-bt-25-instalaciones-interiores-en-viviendas-numero-de-circuitos-y-caracteristicas]]
- [[itc-bt-52-instalaciones-con-fines-especiales-infraestructura-para-la-recarga-de-vehiculos-electricos]]
- [[reglament-electrotecnic-baixa-tensio]]
