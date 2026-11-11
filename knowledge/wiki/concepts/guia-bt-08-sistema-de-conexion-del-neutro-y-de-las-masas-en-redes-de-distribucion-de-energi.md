---
title: Guía-BT-08 — Sistema de conexión del neutro y de las masas en redes de distribución de energía eléctrica
type: concept
tags: [rebt, guia-tecnica, baja-tension, itc-bt-08, esquemas-conexion, masas]
sources: [papers/2026-11-10-guia-bt-08-sistema-de-conexion-del-neutro-y-de-las-masas-en-redes-de-distribucion-de-energi.md]
created: 2026-11-10
updated: 2026-11-10
---

# Guía-BT-08 — Sistema de conexión del neutro y de las masas en redes de distribución de energía eléctrica

Guía técnica de aplicación del REBT (edición oct 05, revisión 1) que comenta la ITC-BT-08, la instrucción que define los tres esquemas de distribución (TN, TT e IT) según la puesta a tierra de la alimentación y de las masas. Acompaña al texto reglamentario sin sustituirlo: la ITC-BT-08 del BOE (RD 842/2002) tiene la autoridad y prevalece ante cualquier discrepancia. En el consolidado del BOE (actualización de 03/09/2025) conserva su redacción original de 2002.

## Puntos clave

- El esquema de distribución condiciona las protecciones contra contactos indirectos (ITC-BT-24) y sobreintensidades, y la especificación de la aparamenta que las realiza.
- Nomenclatura: primera letra, alimentación respecto a tierra (T = conexión directa a tierra; I = aislamiento o punto a tierra por impedancia); segunda, masas (T = masas a tierra; N = masas al punto de la alimentación puesto a tierra, normalmente el neutro); adicionales, neutro y protección (S = separados; C = un solo conductor CPN).
- Variantes TN: TN-S (neutro y protección distintos en todo el esquema), TN-C (combinados en todo el esquema) y TN-C-S (combinados solo en una parte).
- En TN todo defecto franco fase-masa es un cortocircuito con bucle exclusivamente metálico. En TT la intensidad de defecto puede ser inferior a la de cortocircuito pero suficiente para provocar tensiones peligrosas, y el esquema sigue siendo TT aunque las tomas de tierra no sean independientes. En IT el primer defecto no debe generar tensiones peligrosas y se recomienda no distribuir el neutro.
- Las redes de distribución pública de BT usan el esquema TT; desde un centro de transformación de abonado puede elegirse cualquiera de los tres según criterios técnicos y económicos; y puede establecerse IT en parte de una instalación alimentada de red pública mediante transformadores adecuados.
- Prescripciones del TN: sección mínima del neutro en todo su recorrido, tendido del neutro en líneas aéreas como las fases, puestas a tierra en los extremos de líneas y derivaciones de más de 200 m, resistencia del neutro ≤ 5 Ω, resistencia global de las tomas del neutro ≤ 2 Ω y masas unidas al neutro mediante conductores de protección en TN-C.

Tabla 1 de la guía (sección mínima del conductor neutro según la sección de los conductores de fase):

| Sección de fase (mm²) | Neutro en redes aéreas (mm²) | Neutro en redes subterráneas (mm²) |
|---|---|---|
| 16 | 16 | 16 |
| 25 | 25 | 16 |
| 35 | 35 | 16 |
| 50 | 50 | 25 |
| 70 | 50 | 35 |
| 95 | 50 | 50 |
| 120 | 70 | 70 |
| 150 | 70 | 70 |
| 185 | 95 | 95 |
| 240 | 120 | 120 |
| 300 | 150 | 150 |
| 400 | 185 | 185 |

## Detalles

La guía BT-08 es de las más escuetas: reproduce el articulado de la ITC-BT-08 y solo añade un párrafo de encuadre que remite a la ITC-BT-24 para las características de la protección contra contactos indirectos. No incorpora tablas propias ni criterios que modifiquen valores reglamentarios.

El TN es el más exigente: para que las masas se conecten al neutro como medida de protección, la red debe cumplir todas las prescripciones del apartado 2. El TT es el propio de la red pública y el habitual en el alumbrado exterior: el bucle de defecto incluye resistencia de paso a tierra y la protección se dimensiona según el apartado 4.1.2 de la ITC-BT-24, con 24 V como tensión de contacto límite.

En el IT la corriente de primer defecto se limita por la ausencia de conexión a tierra de la alimentación o por una impedancia suficiente entre el punto de alimentación y tierra, lo que puede obligar a limitar la extensión de la instalación por el efecto capacitivo de los cables.

## Divergencias con la ITC-BT-08

Sin divergencias detectadas entre esta guía y el texto consolidado de la ITC-BT-08 del BOE.

Nota de autoridad: la guía reproduce literalmente el articulado, incluida la tabla de secciones mínimas del conductor neutro con los mismos valores para redes aéreas y subterráneas, y solo añade el párrafo de encuadre, conforme al apartado 1.4 y a la ITC-BT-24. La única diferencia es formal: la tabla llega como texto continuo en la guía y como tabla numerada en el BOE. La ITC-BT-08 del RD 842/2002 (consolidado del BOE, actualización de 03/09/2025) es el texto con autoridad y prevalece sobre cualquier criterio de la guía.

## Relacionado

- [[itc-bt-08-sistemas-de-conexion-del-neutro-y-de-las-masas-en-redes-de-distribucion-de-energia-electrica]]
- [[reglament-electrotecnic-baixa-tensio]]
- [[itc-bt-24-instalaciones-interiores-o-receptoras-proteccion-contra-los-contactos-directos-e-indirectos]]
- [[itc-bt-06-redes-aereas-para-distribucion-en-baja-tension]]
- [[itc-bt-07-redes-subterraneas-para-distribucion-en-baja-tension]]
