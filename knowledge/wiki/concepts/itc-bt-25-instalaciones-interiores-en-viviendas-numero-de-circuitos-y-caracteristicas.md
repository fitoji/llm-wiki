---
title: ITC-BT-25 — Instalaciones interiores en viviendas. Número de circuitos y características
type: concept
tags: [rebt, baja-tension, itc-bt-25, viviendas, circuitos]
sources: [papers/2026-11-10-rebt-itc-bt-25-instalaciones-interiores-en-viviendas-numero-de-circuitos-y-caracteristicas.md]
created: 2026-11-10
updated: 2026-11-10
---

# ITC-BT-25 — Instalaciones interiores en viviendas. Número de circuitos y características

Texto normativo de la ITC-BT-25 (REBT, RD 842/2002): grado de electrificación básico, protección general del cuadro, previsión para automatización, esquema de derivaciones C1–C13, cálculo de intensidades y puntos de utilización. Véase la lectura de aplicación en [[instalaciones-interiores-viviendas-bt]] y los puntos por estancia en [[puntos-utilizacion-vivienda]].

## Puntos clave
- El grado de electrificación básico es el sistema mínimo de la instalación interior de viviendas en edificios nuevos, pensado para usar los electrodomésticos básicos sin obras posteriores de adecuación. La capacidad debe ser al menos la intensidad asignada del interruptor general automático, también en la derivación individual.
- Protección general: interruptor general automático omnipolar de accionamiento manual, intensidad nominal mínima de 25 A, con protección contra sobrecargas y cortocircuitos; es independiente del ICP y no puede ser sustituido por él.
- Uno o varios diferenciales protegen contra contactos indirectos todos los circuitos, con intensidad diferencial-residual máxima de 30 mA e intensidad asignada ≥ la del interruptor general; en serie, todos los circuitos deben quedar protegidos con 30 mA como máximo. En redes no TT, se aplica el apartado 4.1 de [[itc-bt-24-instalaciones-interiores-o-receptoras-proteccion-contra-los-contactos-directos-e-indirectos]].
- Previsión para automatización, gestión técnica de la energía y seguridad ([[itc-bt-51-instalaciones-de-sistemas-de-automatizacion-gestion-tecnica-de-la-energia-y-seguridad-para-vivi]]): la alimentación de los dispositivos de control y mando centralizado se hace con automático omnipolar contra sobrecargas y cortocircuitos, que puede situarse aguas arriba de cualquier diferencial si la fuente es de MBTS o MBTP ([[itc-bt-36-instalaciones-a-muy-baja-tension]]).
- Derivaciones: cada circuito independiente se protege con un automático omnipolar manual con protección contra sobrecargas y cortocircuitos según su aplicación. Electrificación básica: C1 (iluminación), C2 (tomas de uso general y frigorífico), C3 (cocina y horno), C4 (lavadora, lavavajillas y termo), C5 (tomas de baños y bases auxiliares del cuarto de cocina).
- Electrificación elevada añade: C6 (circuito adicional tipo C1 por cada 30 puntos de luz), C7 (tipo C2 por cada 20 tomas o si la superficie útil > 160 m²), C8 (calefacción), C9 (aire acondicionado), C10 (secadora independiente), C11 (automatización y seguridad), C12 (adicionales de tipos C3/C4, o tipo C5 si sus tomas exceden de 6) y C13 (recarga de vehículo eléctrico).
- Como mínimo un diferencial por cada cinco circuitos instalados, tanto en básica como en elevada.

| Circuito | Potencia por toma (W) | Fs | Fu | Automático (A) | Máx. puntos | Sección mín. (mm²) | Tubo (mm) |
|---|---|---|---|---|---|---|---|
| C1 Iluminación | 200 | 0,75 | 0,5 | 10 | 30 | 1,5 | 16 |
| C2 Tomas uso general | 3.450 | 0,2 | 0,25 | 16 | 20 | 2,5 | 20 |
| C3 Cocina y horno | 5.400 | 0,5 | 0,75 | 25 | 2 | 6 | 25 |
| C4 Lavadora, lavavajillas, termo | 3.450 | 0,66 | 0,75 | 20 | 3 | 4 | 20 |
| C5 Baño y cuarto de cocina | 3.450 | 0,4 | 0,5 | 16 | 6 | 2,5 | 20 |
| C8 Calefacción | — | — | — | 25 | — | 6 | 25 |
| C9 Aire acondicionado | — | — | — | 25 | — | 6 | 25 |
| C10 Secadora | 3.450 | 1 | 0,75 | 16 | 1 | 2,5 | 20 |
| C11 Automatización | — | — | — | 10 | — | 1,5 | 16 |
| C13 Recarga VE | según [[itc-bt-52-instalaciones-con-fines-especiales-infraestructura-para-la-recarga-de-vehiculos-electricos]] | 1 | 1 | según [[itc-bt-52-instalaciones-con-fines-especiales-infraestructura-para-la-recarga-de-vehiculos-electricos]] | 3 | 2,5 | 20 |

- La intensidad prevista de cada circuito se calcula con I = n × I_a × Fs × Fu (n: número de tomas o receptores; Fs: factor de simultaneidad; Fu: factor de utilización).
- Caída de tensión máxima del 3 %, calculada a la intensidad nominal del automático del circuito y hasta el punto de utilización más alejado; compensable con la de las derivaciones individuales si la caída total es inferior a la suma de los límites de ambas.
- El circuito C13 lleva un diferencial exclusivo con las características de [[itc-bt-52-instalaciones-con-fines-especiales-infraestructura-para-la-recarga-de-vehiculos-electricos]]; en aparcamientos colectivos en régimen de propiedad horizontal, C13 queda sustituido por los esquemas de conexión de las zonas comunes.

## Detalles
Notas de la Tabla 1: potencia máxima permisible de 5.750 W por circuito de calefacción (C8) y de 2.300 W en automatización (C11); tensiones referidas a 230 V fase-neutro; las secciones corresponden a dos conductores y tierra de PVC bajo tubo empotrado en obra (ITC-BT-19), pudiendo exigirse otras para cable o condiciones de instalación distintas. En C4 exclusivamente, cada toma individual puede partir de una caja de derivación de 4 mm² mediante conductor de 2,5 mm². Las bases de 16 A 2p+T y 25 A 2p+T son los tipos de la norma UNE 20315, y el punto de luz debe incluir conductor de protección.

En C4 no son necesarios los fusibles o automáticos de 16 A si cada aparato dispone de circuito independiente propio con su automático de 16 A; este desdoblamiento no implica pasar a electrificación elevada ni añadir un diferencial. Los datos de potencias, tipos de bases y calibre del automático de C13 se remiten a la ITC-BT-52.

Los apartados 2.3.2, 3 y 4 fueron modificados con efectos de 30 de junio de 2015 por la disposición final 6 del Real Decreto 1053/2014, de 12 de diciembre (BOE-A-2014-13681). Los puntos de utilización mínimos por estancia (Tabla 2) se recogen en [[puntos-utilizacion-vivienda]].

## Relacionado
- [[instalaciones-interiores-viviendas-bt]]
- [[puntos-utilizacion-vivienda]]
- [[itc-bt-23-instalaciones-interiores-o-receptoras-proteccion-contra-sobretensiones]]
- [[itc-bt-51-instalaciones-de-sistemas-de-automatizacion-gestion-tecnica-de-la-energia-y-seguridad-para-vivi]]
- [[itc-bt-52-instalaciones-con-fines-especiales-infraestructura-para-la-recarga-de-vehiculos-electricos]]
- [[reglament-electrotecnic-baixa-tensio]]
