---
title: Guía-BT-29 — Instalaciones eléctricas de los locales con riesgo de incendio o explosión
type: concept
tags: [rebt, guia-tecnica, baja-tension, itc-bt-29, atex, zonas-riesgo]
sources: [papers/2026-11-10-guia-bt-29-instalaciones-electricas-de-los-locales-con-riesgo-de-incendio-o-explosion.md]
created: 2026-11-10
updated: 2026-11-10
---

# Guía-BT-29 — Instalaciones eléctricas de los locales con riesgo de incendio o explosión

La Guía-BT-29 (noviembre de 2019, revisión 4) desarrolla la ITC-BT-29 del REBT: reglas de diseño, ejecución, explotación, mantenimiento y reparación de instalaciones de baja tensión en emplazamientos con riesgo de explosión o incendio por sustancias inflamables, para que no sean la causa de su inflamación. Acompaña a la [[itc-bt-29-prescripciones-particulares-para-las-instalaciones-electricas-de-los-locales-con-riesgo-de-ince]], que TIENE AUTORIDAD: prevalece el texto reglamentario consolidado del BOE.

## Puntos clave

- Dos clases de emplazamiento según la naturaleza de la sustancia inflamable, con zonas por probabilidad de atmósfera explosiva:

| Clase | Zona | Criterio |
|---|---|---|
| I (gases, vapores, nieblas) | 0 | Presente permanente, prolongada o frecuente |
| I | 1 | Formación ocasional en funcionamiento normal |
| I | 2 | Muy breve, si se forma |
| II (polvo inflamable) | 20 | Nube de polvo permanente, prolongada o frecuente; las capas no son zona 20 |
| II | 21 | Formación ocasional de nube de polvo |
| II | 22 | Muy breve, si se forma |

- La clasificación la realiza un técnico competente; la guía la asigna al técnico del proyecto de la [[itc-bt-04-documentacion-y-puesta-en-servicio-de-las-instalaciones]] y exige lista de sustancias, fuentes de escape y plano de áreas peligrosas.
- Categorías admisibles (tablas 1 y 2, idénticas a las de la ITC) y modos de protección típicos:

| Categoría | Gases | Polvos | Modos típicos |
|---|---|---|---|
| 1 | 0, 1 y 2 | 20, 21 y 22 | 'ia', 'ma', 'ta', 'da' |
| 2 | 1 y 2 | 21 y 22 | 'db', 'pxb'/'pyb', 'qb', 'ob', 'eb', 'mb', 'ib', 'tb' |
| 3 | 2 | 22 | 'dc', 'pzc', 'ec', 'mc', 'ic', 'tc' |

- Clase I según UNE-EN 60079-14 y Clase II según EN 50281-1-2, ya sustituida por UNE-EN 60079-14; la Instrucción prevalece sobre la norma.
- Cableado: 450/750 V mínimos, intensidad admisible -15 %, cables de 5 m o más protegidos contra sobrecargas y cortocircuitos y reacción al fuego mínima C-s1b,d1,a1 ca (Reglamento Delegado (UE) 2016/364).
- Equipos portátiles o móviles: 1,5 mm² y 30 m como máximo, que la guía acota a herramientas no instaladas y sustituye por 1,0 mm² con 250 V y 6 A.
- Seguridad intrínseca: solo en zonas 0 y 20 con circuitos de categoría 1; con más de dos aparatos de categoría 1 el resultado global pasa a categoría 2.
- Riesgo electrostático en canalizaciones no metálicas: resistencia superficial no mayor de 1 GΩ y equipotencial a tierra no mayor de 1 MΩ; por encima, prohibición en zonas 0 y 20, no accesibilidad y señalización.
- Inspección y mantenimiento según UNE-EN 60079-17 y reparación según CEI 60079-19; la guía los declara orientativos y reserva la obligación legal a las inspecciones administrativas de la [[itc-bt-05-verificaciones-e-inspecciones]] por organismo ENAC.

## Detalles

El campo de aplicación solo considera el riesgo de coexistencia entre lo eléctrico y la atmósfera explosiva. La guía amplía las exclusiones de la ITC (dispositivos médicos, aparatos ATEX con peligro por sustancias explosivas, uso doméstico, protección individual, navíos, medios de transporte), recuerda que la ITC solo es exigible dentro del REBT (1000 V CA, 1500 V CC) y advierte de las mezclas híbridas de gas y polvo.

En requisitos de los equipos la guía actualiza el marco ATEX: los productos conformes al R.D. 144/2016 son obligatorios desde el 20 de abril de 2016 y los adquiridos antes solo son usables justificando su seguridad en la documentación técnica (artículo 23.1.b del Reglamento). Recoge los modos 'd', 'o' e 'i' y la declaración UE de conformidad del Anexo X.

La clasificación exige caracterizar antes las sustancias: en Clase I, estado físico, contención, punto de inflamación, densidad relativa, temperatura de ignición, límites de explosión, presión de vapor, subgrupo y ventilación; en Clase II, granulometría, humedad, temperatura de inflamación en capa y nube, conductividad, concentración mínima explosiva y Kmax, con subgrupos IIIA, IIIB e IIIC. La guía presume peligroso todo emplazamiento con sustancias inflamables salvo que la clasificación demuestre lo contrario.

Las prescripciones generales sitúan los equipos en áreas no peligrosas siempre que se pueda y prevén un permiso especial de trabajo para tareas excepcionales (soldadura, plantas piloto) con operación limitada y supervisión de personal formado. La guía añade al proyecto el documento de protección contra explosiones del artículo 8 del R.D. 681/2003.

Los conductos mantienen las tablas 3, 4 y 5 de la ITC, y la guía precisa entrada por prensaestopas compatibles, 10 m máximos entre puestas a tierra de tubos conductores y certificado UNE-EN 60079-1 para tubos flexibles. Los anexos son material propio: el Anexo I relaciona modos con su norma UNE-EN 60079-x; el Anexo II, las normas de instalaciones; el Anexo III, los garajes y su desclasificación por ventilación; el Anexo IV, la detección de gases (UNE-EN 60079-29-1 y -29-2).

## Divergencias con la ITC-BT-29

- Equipos: la guía (5) remite al R.D. 144/2016, obligatorio desde el 20 de abril de 2016, y admite equipos anteriores justificando su seguridad en la documentación técnica; la ITC-BT-29 (5) exige solo el R.D. 400/1996. Prevalece la ITC-BT-29.
- Terminología: la guía (2) añade a las categorías 1, 2 y 3 los modos UNE-EN 60079-x y la "declaración UE de conformidad"; la ITC-BT-29 (2) solo define las categorías y la "declaración CE". Prevalece la ITC-BT-29.
- Zonas: la guía (4.1.1 y 4.1.2) remite a UNE-EN 60079-10-1 y 60079-10-2 y sustituye la CEI 61241-3; la ITC-BT-29 cita UNE-EN 60079-10 y CEI 61241-3. Prevalece la ITC-BT-29.
- Normas: la guía (7.1, 8.1, 8.3, 9.1, 9.2, 9.3) sustituye EN 50281-1-2 por UNE-EN 60079-14, UNE-EN 50039 por UNE-EN 60079-25 y UNE-EN 50086 por UNE-EN 61386; la ITC-BT-29 cita las sustituidas, aunque el listado del BOE (Resolución de 20 de marzo de 2025) ya lo hace. Prevalece la ITC-BT-29.
- Inspección: la guía (6.1 y 6.3) declara los procedimientos de UNE-EN 60079-17 y 60079-19 orientativos para la propiedad y mantiene la obligación legal en las inspecciones administrativas de la [[itc-bt-05-verificaciones-e-inspecciones]] por organismo ENAC; la ITC-BT-29 (6.1) obliga a inspeccionar según UNE-EN 60079-17. Prevalece la ITC-BT-29.
- Seguridad intrínseca: la guía (9.1) limita el uso en zonas 0 y 20 a circuitos de categoría 1, degrada a categoría 2 el resultado global con más de dos aparatos de categoría 1 y excluye del apartado 9 a las instalaciones de seguridad intrínseca; la ITC-BT-29 (9.1) solo remite a UNE-EN 60079-14 y 50039. Prevalece la ITC-BT-29.
- Reacción al fuego: la guía (9.2 a)) fija la clase mínima C-s1b,d1,a1 ca y añade la tabla A de canalización en superficie; la ITC-BT-29 (9.2 a)) solo remite a UNE 20432-3. Prevalece la ITC-BT-29.
- Cables portátiles y móviles: la guía (9.2 b)) limita los 30 m a herramientas no instaladas, sustituye UNE 21027-4 por UNE-EN 50525-2-21 y añade 1,0 mm² con 250 V y 6 A; la ITC-BT-29 (9.2 b)) fija 1,5 mm² y 30 m sin excepción. Prevalece la ITC-BT-29.
- Documentación: la guía (4 y 6.2) exige además el documento de protección contra explosiones del artículo 8 del R.D. 681/2003, la relación de sustancias y fuentes de escape y el plano de áreas peligrosas; la ITC-BT-29 solo pide clasificación con plano, categorías, instrucciones y condiciones especiales. Prevalece la ITC-BT-29.
- Desclasificación de garajes: la guía (Anexo III) fija un método de desclasificación por ventilación (f = 5, k = 0,25 o 0,5) y concluye que los garajes que cumplen el CTE HS3 son desclasificados; la ITC-BT-29 no prevé vía de desclasificación y mantiene los garajes entre los emplazamientos peligrosos. Prevalece la ITC-BT-29.

## Relacionado

- [[itc-bt-29-prescripciones-particulares-para-las-instalaciones-electricas-de-los-locales-con-riesgo-de-ince]]
- [[classificacio-p1-p2]]
- [[reglament-electrotecnic-baixa-tensio]]
- [[itc-bt-05-verificaciones-e-inspecciones]]
