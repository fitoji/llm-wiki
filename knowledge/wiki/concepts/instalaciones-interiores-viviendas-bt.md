---
title: Instalaciones interiores en viviendas: electrificación, circuitos y características (Guía-BT-25)
type: concept
tags: [rebt, baixa-tensio, espana, guia-tecnica, itc-bt, viviendas, circuitos]
sources: [papers/2026-11-10-guia-bt-25-circuitos-caracteristicas.md, papers/2026-11-10-rebt-itc-bt-25-instalaciones-interiores-en-viviendas-numero-de-circuitos-y-caracteristicas.md, papers/2026-11-10-guia-bt-25-instalaciones-interiores-en-viviendas-numero-de-circuitos-y-caracteristicas.md]
created: 2026-11-10
updated: 2026-11-10
---

# Instalaciones interiores en viviendas: electrificación, circuitos y características (Guía-BT-25)

Guía técnica de aplicación ITC-BT-25 (edición jul 12, revisión 2): número de circuitos, características eléctricas y grado de electrificación de las instalaciones interiores en viviendas.

## Punts clau
- Electrificación elevada cuando se cumple alguna de: superficie útil > 160 m²; previsión de aire acondicionado, calefacción eléctrica, sistemas de automatización, secadora; más de 30 puntos de luz; más de 20 tomas de uso general; más de 6 tomas en baños y auxiliares de cocina; o las condiciones del apartado 2.3.
- Electrificación básica: IGA mínimo 25 A (25 A para 5.750 W; 32 A para 7.360 W). Electrificación elevada: 40/50/63 A para 9.200/11.500/14.490 W.
- Protección general mínima: IGA omnipolar con protección contra sobrecargas y cortocircuitos; uno o varios diferenciales de ≤ 30 mA y corriente asignada ≥ IGA; dispositivos de protección contra sobretensiones si procede (ITC-BT-23).
- Circuitos independientes C1–C5 en electrificación básica (iluminación, uso general+frigorífico, cocina/horno, lavadora/lavavajillas/termo, baño y auxiliares de cocina). En elevada se añaden C6–C13 (iluminación adicional, uso general adicional, calefacción, aire acondicionado, secadora, automatización, circuitos adicionales, recarga de vehículo eléctrico).
- Diferencial único para varios circuitos puede provocar disparos intempestivos; conviene diferencial individual para equipos informáticos, frigoríficos y congeladores. Selectividad total: tiempo de no-actuación del diferencial aguas arriba superior al de operación del de aguas abajo; intensidad diferencial aguas arriba ≥ 3× la de aguas abajo (tipo S).
- Un diferencial por cada 5 circuitos como mínimo. Un diferencial de 30 mA Clase A exclusivo para el circuito C13 (recarga de vehículo eléctrico).
- Protección contra sobretensiones: instalarse aguas arriba del diferencial (entre IGA y diferencial) salvo si el diferencial es selectivo S. Limitador de sobretensiones transitorias con dispositivo de protección recomendado por el fabricante aguas arriba para mantener continuidad.
- Desdoblamiento de C1/C2/C5 sin pasar a elevada si se mantiene la sección mínima, el calibre del automático y se instala un diferencial adicional cuando el total de circuitos supera 5.
- Disparos intempestivos frecuentes: separar C3 (cocina/horno) y/o C9 (aire acondicionado) con diferencial individual (tipo A según ITC-BT-24 punto 3.5), o sustituir por diferencial rearmable (EN 50557); instalar protectores contra sobretensiones transitorias aguas arriba.

## Detalles
La sección mínima de cada circuito está calculada para un número limitado de puntos de utilización (Tabla 1): C1 1,5 mm² / 10 A / 30 puntos; C2 2,5 mm² / 16 A / 20 tomas; C3 6 mm² / 25 A / 2 tomas; C4 4 mm² / 16 A / 3 tomas; C5 2,5 mm² / 16 A / 6 tomas; C8/C9 6 mm² / 25 A; C10 2,5 mm² / 16 A / 1 toma; C11 1,5 mm² / 10 A.

La caída de tensión máxima es del 3 %, calculada para la intensidad nominal del automático y la distancia al punto de utilización más alejado; puede compensarse entre instalación interior y derivaciones individuales. Tabla B: longitudes máximas de conductor en función de sección e intensidad nominal (1,5 mm²: 27 m a 10 A; 2,5 mm²: 45 m a 10 A / 28 m a 16 A; 4 mm²: 45 m a 16 A / 36 m a 20 A; 6 mm²: 53 m a 20 A / 43 m a 25 A).

El IGA es independiente del ICP (interruptor de control de potencia) y no puede ser sustituido por él. Para instalaciones alimentadas por redes distintas a TT, la protección contra contactos indirectos se realiza según ITC-BT-24 apartado 4.1.

## Divergencias con la ITC-BT-25
Comparación entre la Guía-BT-25 (edición jul12 R2) y el texto consolidado de la ITC-BT-25 del BOE (RD 842/2002, BOE-A-2002-18099, en vigor desde 30/06/2015). Prevalece siempre la ITC-BT-25.

- **Criterios de electrificación elevada (apartado 1 de la guía).** La guía enumera nueve condiciones para que la vivienda sea de electrificación elevada: superficie útil superior a 160 m², previsión de aire acondicionado, de calefacción eléctrica, de sistemas de automatización o de secadora, más de 30 puntos de utilización de alumbrado, más de 20 tomas de uso general, más de 6 tomas de baño y auxiliares de cocina, y las condiciones del apartado 2.3. El apartado 1 del texto consolidado de la ITC-BT-25 del BOE no recoge esa lista: se limita a definir la electrificación básica y remite la electrificación elevada al apartado 2.3.2. Prevalece la ITC-BT-25.
- **Tabla A de potencia prevista y calibre del IGA (apartado 2.1 de la guía).** La guía fija para electrificación básica 5.750 W con IGA de 25 A y 7.360 W con IGA de 32 A, y para electrificación elevada 9.200 W con 40 A, 11.500 W con 50 A y 14.490 W con 63 A. La ITC-BT-25 del BOE no publica esa tabla y solo exige un interruptor general automático de intensidad nominal mínima de 25 A, sin correspondencia entre potencia prevista y calibre. Prevalece la ITC-BT-25.
- **Selectividad entre diferenciales en serie (apartado 2.1 de la guía).** La guía exige, para garantizar la selectividad total, que el tiempo de no-actuación del diferencial aguas arriba sea superior al tiempo total de operación del diferencial aguas abajo y que su intensidad diferencial-residual sea como mínimo tres veces la de este (diferenciales tipo S). La ITC-BT-25 del BOE no regula estas condiciones; su único reenvío a la ITC-BT-24 se refiere a la protección contra contactos indirectos en redes distintas de TT. Prevalece la ITC-BT-25.
- **Colocación de los protectores contra sobretensiones y diferencial único (apartado 2.1 de la guía).** La guía sitúa el dispositivo de protección contra sobretensiones aguas arriba del diferencial (entre el interruptor general y el propio diferencial, salvo si el diferencial es selectivo S), exige un dispositivo de protección recomendado por el fabricante aguas arriba del limitador para mantener la continuidad del servicio y prescribe que, con un único interruptor diferencial, este sea de disparo instantáneo. La ITC-BT-25 del BOE solo indica que los dispositivos de protección contra sobretensiones se instalarán, si fuese necesario, conforme a la ITC-BT-23, sin fijar esa colocación ni el disparo instantáneo. Prevalece la ITC-BT-25.
- **Tabla B de longitudes máximas de conductor (apartado 3 de la guía).** La guía publica la Tabla B con la longitud máxima del cable para una caída de tensión del 3 % a 40 ºC y cos ϕ = 1 (1,5 mm²: 27 m a 10 A; 2,5 mm²: 45 m a 10 A y 28 m a 16 A; 4 mm²: 45 m a 16 A y 36 m a 20 A; 6 mm²: 53 m a 20 A y 43 m a 25 A). La ITC-BT-25 del BOE fija el límite del 3 % y la regla de compensación entre la instalación interior y las derivaciones individuales, pero no incluye esa tabla de longitudes. Prevalece la ITC-BT-25.
- **Criterios del apartado 2.3.1 sobre derivaciones y desdoblamiento (guía).** La guía añade criterios que el texto consolidado del BOE no recoge en el apartado 2.3.1: recomendación de dos o tres circuitos independientes en C4 sin pasar a electrificación elevada; instalación de la toma del termo eléctrico aunque no se prevea su uso; asignación al circuito C1 de las bases de toma de corriente de aparatos de alumbrado; asignación al circuito C5 de la toma del horno microondas y de la bañera de hidromasaje (con los requisitos de la ITC-BT-27); y reglas de desdoblamiento de C1, C2 y C5 (mantener la sección mínima y el calibre reflejados en la tabla 1, instalar un diferencial adicional si el número total de circuitos supera 5 y no pasar a electrificación elevada). La ITC-BT-25 del BOE solo recoge, en la nota 8 de su tabla 1, que el desdoblamiento de C4 no supone pasar a electrificación elevada ni necesitar un diferencial adicional. Prevalece la ITC-BT-25.
- **Circuito C13 de recarga de vehículo eléctrico (apartado 2.3.2).** La guía exige para C13 un interruptor diferencial de 30 mA, Clase A, exclusivo para su protección. La ITC-BT-25 del BOE remite a la (ITC) BT-52 para las características del diferencial exclusivo de C13 y añade que en aparcamientos o estacionamientos colectivos en edificios o conjuntos inmobiliarios en régimen de propiedad horizontal el circuito C13 queda sustituido por los esquemas de conexión instalados en las zonas comunes. Prevalece la ITC-BT-25.
- **Fila C13 de la tabla 1.** La tabla 1 de la guía (edición jul12 R2) termina en C11 y no incluye el circuito C13; la tabla 1 de la ITC-BT-25 del BOE incorpora la fila "C13 Recarga del vehículo eléctrico" con un máximo de 3 puntos de utilización, sección mínima de 2,5 mm² y conducto de 20 mm, remitiendo la potencia prevista por toma, el tipo de base y la intensidad asignada del automático a la ITC-BT-52. El resto de filas (C1, C2, C3, C4, C5, C8, C9, C10 y C11) coincide en ambos textos. Prevalece la ITC-BT-25.

## Relacionado
- [[puntos-utilizacion-vivienda]]
- [[toma-de-tierra-edificios-viviendas]]
- [[conductores-y-ejecucion-instalacion-interior]]
- [[locales-banera-ducha-bt]]
- [[reglament-electrotecnic-baixa-tensio]]
- [[itc-bt-25-instalaciones-interiores-en-viviendas-numero-de-circuitos-y-caracteristicas]]
