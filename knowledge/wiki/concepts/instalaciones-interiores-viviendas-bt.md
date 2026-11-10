---
title: Instalaciones interiores en viviendas: electrificación, circuitos y características (Guía-BT-25)
type: concept
tags: [rebt, baixa-tensio, espana, guia-tecnica, itc-bt, viviendas, circuitos]
sources: [papers/2026-11-10-guia-bt-25-circuitos-caracteristicas.md, papers/2026-11-10-rebt-itc-bt-25-instalaciones-interiores-en-viviendas-numero-de-circuitos-y-caracteristicas.md]
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

## Relacionado
- [[puntos-utilizacion-vivienda]]
- [[toma-de-tierra-edificios-viviendas]]
- [[conductores-y-ejecucion-instalacion-interior]]
- [[locales-banera-ducha-bt]]
- [[reglament-electrotecnic-baixa-tensio]]
