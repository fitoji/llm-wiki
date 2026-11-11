---
title: ITC-BT-22 — Instalaciones interiores o receptoras. Protección contra sobreintensidades
type: concept
tags: [rebt, baja-tension, itc-bt-22, sobreintensidades, proteccion]
sources: [papers/2026-11-10-rebt-itc-bt-22-instalaciones-interiores-o-receptoras-proteccion-contra-sobreintensidades.md]
created: 2026-11-10
updated: 2026-11-10
---

# ITC-BT-22 — Instalaciones interiores o receptoras. Protección contra sobreintensidades

La ITC-BT-22 del REBT obliga a proteger todo circuito contra los efectos de las sobreintensidades que puedan presentarse en el mismo, interrumpiéndolo en un tiempo conveniente o dimensionándolo para las sobreintensidades previsibles. Distingue las causas de las sobreintensidades y las medidas de protección contra sobrecargas y cortocircuitos, remitiendo a las normas UNE 20.460-4-43 y UNE 20.460-4-473.

## Puntos clave

- Las sobreintensidades pueden estar motivadas por: sobrecargas debidas a los aparatos de utilización o defectos de aislamiento de gran impedancia, cortocircuitos y descargas eléctricas atmosféricas.
- Contra sobrecargas: la intensidad admisible del conductor queda garantizada en todo caso por el dispositivo de protección, que podrá ser un interruptor automático de corte omnipolar con curva térmica o cortacircuitos fusibles calibrados adecuados.
- Contra cortocircuitos: en el origen de todo circuito se instala un dispositivo con capacidad de corte acorde con la intensidad de cortocircuito que pueda presentarse en el punto de conexión; se admiten fusibles calibrados o interruptores automáticos omnipolares.
- En circuitos derivados de un principal, se admite que cada derivado disponga solo de protección contra sobrecargas mientras un único dispositivo general asegura la protección contra cortocircuitos de todos.
- La norma UNE 20.460-4-43 recoge la naturaleza de los dispositivos (432), protección contra sobrecargas (433), contra cortocircuitos (434), coordinación entre ambas (435) y limitación de sobreintensidades por las características de la alimentación (436).
- La UNE 20.460-4-473 define la aplicación de esas medidas según el origen (sobrecarga o cortocircuito), señala el emplazamiento u omisión de la protección y resume los casos en una tabla por esquema de red.

## Detalles

La tabla 1 de la instrucción indica, para cada esquema de red (TN-C, TN-S, TT e IT) y distribución de la instalación (3 F + N, 3 F, F + N y 2 F), sobre qué conductores debe preverse un dispositivo de protección o detección («P»), distinguiendo según la sección del neutro (S_N) sea mayor o igual o menor que la de fase (S_F). En general, la detección se prevé sobre los conductores de fase en todos los esquemas.

El conductor de neutro admite excepciones bajo condiciones estrictas. En el esquema TN-C con S_N < S_F es admisible no prever detección sobre el neutro si este queda protegido contra los cortocircuitos por el dispositivo de protección de las fases y la intensidad máxima que lo recorre en servicio normal es netamente inferior a su intensidad admisible. Condiciones análogas, con variantes propias de cada esquema, se aplican en TN-S, TT e IT.

Otras notas de la tabla: el corte y la conexión del neutro deben realizarse de modo que el neutro no se corte antes que las fases y se conecte al mismo tiempo o antes que estas; en esquema TT con neutro no distribuido puede omitirse la detección sobre una fase si existe aguas arriba una protección diferencial que corte todos los conductores de fase y no haya distribución del neutro a partir de un punto neutro artificial aguas abajo; y en esquemas con protección diferencial se salvan ciertas detecciones siempre que, en el caso del neutro, exista aguas arriba una protección diferencial cuya corriente diferencial-residual nominal sea como máximo 0,15 veces la corriente admisible del neutro, dispositivo que debe cortar todos los conductores activos del circuito, incluido el neutro.

## Relacionado
- [[guia-bt-22-proteccion-contra-sobreintensidades]] — guía técnica de aplicación (no vinculante: prevalece la ITC-BT-22)

- [[reglament-electrotecnic-baixa-tensio]]
- [[instalaciones-interiores-viviendas-bt]]
