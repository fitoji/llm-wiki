---
title: ITC-BT-23 — Instalaciones interiores o receptoras. Protección contra sobretensiones
type: concept
tags: [rebt, baja-tension, itc-bt-23, sobretensiones, descargadores]
sources: [papers/2026-11-10-rebt-itc-bt-23-instalaciones-interiores-o-receptoras-proteccion-contra-sobretensiones.md]
created: 2026-11-10
updated: 2026-11-10
---

# ITC-BT-23 — Instalaciones interiores o receptoras. Protección contra sobretensiones

La ITC-BT-23 del REBT trata la protección de las instalaciones eléctricas interiores contra las sobretensiones transitorias transmitidas por las redes de distribución, originadas fundamentalmente por descargas atmosféricas, conmutaciones de red y defectos en las mismas. Define cuatro categorías de sobretensión según la tensión soportada a impulsos de los equipos y establece cuándo la protección es necesaria (situación controlada) o innecesaria (situación natural). No cubre la descarga directa del rayo ni la protección de señales de medida, control y telecomunicación.

## Puntos clave

- El nivel de sobretensión en la red depende del nivel isoceraúnico estimado, del tipo de acometida (aérea o subterránea) y de la proximidad del transformador de MT/BT; su incidencia depende de la coordinación del aislamiento, los dispositivos de protección y la red de tierras.
- Hay cuatro categorías de sobretensión, que fijan la tensión soportada a la onda de choque y el valor límite de tensión residual de los dispositivos de protección de cada zona.
- Categoría I: equipos muy sensibles, como ordenadores y equipos electrónicos muy sensibles; la protección se toma fuera de los equipos. Categoría II: equipos conectados a instalación fija, como electrodomésticos y herramientas portátiles. Categoría III: parte de la instalación fija (armarios de distribución, embarrados, aparamenta, canalizaciones, motores de conexión fija). Categoría IV: equipos en el origen de la instalación o muy próximos, aguas arriba del cuadro, como contadores de energía y aparatos de telemedida.
- Situación natural: alimentación por red subterránea en su totalidad (o línea aérea con conductores aislados con pantalla metálica unida a tierra en sus dos extremos, equivalente a subterránea); no se requiere protección suplementaria.
- Situación controlada: la instalación se alimenta por, o incluye, una línea aérea con conductores desnudos o aislados; se exige protección contra sobretensiones de origen atmosférico en el origen de la instalación.
- El nivel de protección de los descargadores debe ser inferior a la tensión soportada a impulso de la categoría de los equipos previstos.
- Conexión de descargadores: en redes TT o IT entre cada conductor (incluido el neutro o compensador) y tierra; en TN-S entre cada fase y el conductor de protección; en TN-C entre cada fase y el neutro o compensador.
- La estrategia de protección en cascada integra tres niveles (basta o grueso, media y fina) para reducir la sobretensión de entrada a un nivel no peligroso y prolongar la vida de los dispositivos.

## Detalles

La ordenada selección de categorías permite coordinar el aislamiento de la instalación completa, reduciendo el riesgo de fallo a un nivel aceptable. La tabla 1 de la instrucción fija la tensión soportada a impulsos 1,2/50 (kV) según la tensión nominal:

| Tensión nominal (trifásica/monofásica) | Cat. IV | Cat. III | Cat. II | Cat. I |
|---|---|---|---|---|
| 230/400 (230) | 6 | 4 | 2,5 | 1,5 |
| 400/690 · 1000 | 8 | 6 | 4 | 2,5 |

La existencia de una situación natural no excluye instalar dispositivos de protección por conveniencia: cuando prima la continuidad del servicio, el valor económico de los equipos o la irreparabilidad de pérdidas, una situación natural puede tratarse también como situación controlada. El control del nivel de sobretensiones puede lograrse con dispositivos colocados en las líneas aéreas, siempre que estén suficientemente próximos al origen de la instalación, o en la instalación eléctrica del edificio.

Aparte de la protección contra sobretensiones atmosféricas, los equipos y materiales deben escogerse con tensión soportada a impulsos no inferior a la prescrita para su categoría. Los equipos con tensión soportada inferior a la indicada pueden utilizarse en situación natural cuando el riesgo sea aceptable, o en situación controlada si la protección contra las sobretensiones es adecuada.

## Relacionado
- [[guia-bt-23-proteccion-contra-sobretensiones]] — guía técnica de aplicación (no vinculante: prevalece la ITC-BT-23)

- [[reglament-electrotecnic-baixa-tensio]]
- [[toma-de-tierra-edificios-viviendas]]
- [[instalaciones-interiores-viviendas-bt]]
