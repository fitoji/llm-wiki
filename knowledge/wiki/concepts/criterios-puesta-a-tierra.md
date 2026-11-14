---
title: Criterios de puesta a tierra en baja tensión
type: concept
tags: [rebt, baja-tension, puesta-a-tierra, electrodos, itc-bt-18, guia-bt-18, bt-26]
sources: [papers/2026-11-10-rebt-itc-bt-18-instalaciones-de-puesta-a-tierra.md, papers/2026-11-10-guia-bt-18-instalaciones-de-puesta-a-tierra.md, papers/2026-11-10-rebt-itc-bt-26-instalaciones-interiores-en-viviendas-prescripciones-generales-de-instalacion.md, papers/2026-11-10-guia-bt-26-prescripciones-generales.md, papers/2026-11-10-guia-rebt-anexo-4-verificacion-de-las-instalaciones-electricas.md]
created: 2026-11-14
updated: 2026-11-14
---

# Criterios de puesta a tierra en baja tensión

La puesta a tierra limita la tensión de las masas metálicas respecto a tierra, asegura la actuación de las protecciones y reduce el riesgo de avería. Este artículo reúne los criterios generales de la ITC-BT-18 (electrodos, secciones, borne principal, medición y revisión), lo que la Guía-BT-18 añade como criterio de buena práctica y su aplicación en edificios de viviendas, que desarrolla [[toma-de-tierra-edificios-viviendas]].

## Puntos clave

- La toma de tierra es la unión eléctrica directa, **sin fusibles ni protección**, de las masas a electrodos enterrados. Los electrodos admisibles son barras o tubos, pletinas y conductores desnudos, placas, anillos o mallas, armaduras de hormigón enterradas (excepto pretensadas) y otras estructuras enterradas apropiadas.
- La **profundidad** de los electrodos nunca es inferior a **0,50 m**. Las canalizaciones metálicas de otros servicios (agua, gases inflamables, calefacción central) **no** pueden usarse como toma de tierra.
- La **sección** de los conductores de tierra sigue la tabla 1 de la ITC-BT-18 según estén o no protegidos contra la corrosión y mecánicamente; la de los conductores de protección sigue la tabla 2 (S ≤ 16 → S; 16 < S ≤ 35 → 16; S > 35 → S/2).
- Toda instalación tiene un **borne principal de tierra** con un dispositivo desmontable que permite medir la resistencia. La tensión de contacto no supera **24 V** en locales o emplazamientos conductores y **50 V** en los demás casos.
- La **revisión** es obligatoria al dar de alta la instalación; la resistencia se mide al menos **una vez al año** en la época en que el terreno está más seco y, en terrenos no favorables, se descubren electrodos y conductores de enlace al menos cada **cinco años**.
- La Guía-BT-18 añade criterios no vinculantes (35 mm² de cobre, 0,8 m de profundidad, método de medición con electrodos auxiliares) que son **ampliaciones** respecto de la ITC-BT-18.

## Detalles

### Electrodos y profundidad

La ITC-BT-18 admite como electrodos barras o tubos, pletinas y conductores desnudos, placas, anillos o mallas, armaduras de hormigón enterradas —excepto las pretensadas— y otras estructuras enterradas apropiadas. La profundidad nunca es inferior a 0,50 m. La Guía-BT-18 recomienda 0,8 m con heladas y fija dimensiones mínimas de electrodo con las UNE 21056 y 202006; son ampliaciones, no exigencias del BOE.

No pueden usarse como toma de tierra las canalizaciones metálicas de otros servicios: agua, líquidos o gases inflamables, calefacción central, etc.

### Secciones

La tabla 1 de la ITC-BT-18 fija la sección de los conductores de tierra según su protección:

| Tipo | Protegido mecánicamente | No protegido mecánicamente |
|---|---|---|
| Protegido contra la corrosión | Según el apartado 3.4 | 16 mm² Cu / 16 mm² acero galvanizado |
| No protegido contra la corrosión | 25 mm² Cu / 50 mm² hierro | (indicado en la instrucción) |

La tabla 2 fija la sección mínima del conductor de protección en función de la sección de fase S: S si S ≤ 16 mm², 16 mm² si 16 < S ≤ 35 mm² y S/2 si S > 35 mm². Fuera de la canalización de alimentación, el conductor de protección es de cobre, de 2,5 mm² como mínimo con protección mecánica y 4 mm² sin ella.

### Elementos a conectar y borne principal

Se conectan a tierra las masas metálicas importantes, las masas accesibles de los receptores, los depósitos de gasóleo, las instalaciones de calefacción general, el agua y el gas canalizados y las antenas de radio y televisión. Las partes conductoras con origen exterior se conectan a tierra tan cerca como sea posible de su entrada al edificio.

Toda instalación prevé un borne principal de tierra al que se unen los conductores de tierra, de protección, de unión equipotencial principal y de puesta a tierra funcional, con un dispositivo desmontable por útil para medir la resistencia.

### Medición y resistencia

La ITC-BT-18 fija la tensión de contacto máxima (24 V en local o emplazamiento conductor, 50 V en los demás casos) y el criterio de independencia de dos tomas de tierra: lo son cuando, circulando por una la máxima corriente de defecto prevista, la otra no supera 50 V respecto a un punto de potencial cero. La Guía-BT-18 desarrolla el procedimiento con electrodos auxiliares y la fórmula R = 1,6 ρ/P, además de coeficientes de la UNE 207003; son criterios de la guía. El detalle de la comprobación está en [[guia-rebt-anexo-4-verificacion-de-las-instalaciones-electricas]].

### Aplicación en viviendas y verificación

En edificios de viviendas la Guía-BT-26 concreta el anillo de cimentación, las picas, los cinco puntos de puesta a tierra y las líneas principales y derivaciones; ese desarrollo está en [[toma-de-tierra-edificios-viviendas]]. La revisión de la instalación se hace al dar de alta, anualmente en la época seca y cada cinco años en terrenos no favorables.

## Relacionado

- [[toma-de-tierra-edificios-viviendas]] — aplicación de la Guía-BT-26 en edificios de viviendas
- [[itc-bt-18-instalaciones-de-puesta-a-tierra]] — texto consolidado de la instrucción
- [[guia-bt-18-instalaciones-de-puesta-a-tierra]] — criterio de la guía y sus divergencias
- [[esquemas-conexion-neutro-masas]] — TT, TN e IT y las resistencias de tierra asociadas
- [[proteccion-diferencial-selectividad]] — protección contra contactos indirectos
- [[guia-rebt-anexo-4-verificacion-de-las-instalaciones-electricas]] — comprobación de la puesta a tierra
- [[divergencias-guias-tecnicas-rebt-vs-itc-bt]] — mapa de las 221 divergencias y sus tipos
