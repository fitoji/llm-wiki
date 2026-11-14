---
title: Protección diferencial y selectividad en baja tensión
type: concept
tags: [rebt, baja-tension, diferencial, selectividad, contactos-indirectos, itc-bt-24, itc-bt-19, guia-tecnica]
sources: [papers/2026-11-10-rebt-itc-bt-24-instalaciones-interiores-o-receptoras-proteccion-contra-los-contactos-directos-e-indirectos.md, papers/2026-11-10-guia-bt-24-proteccion-contra-los-contactos-directos-e-indirectos.md, papers/2026-11-10-rebt-itc-bt-19-instalaciones-interiores-o-receptoras-prescripciones-generales.md, papers/2026-11-10-rebt-itc-bt-52-instalaciones-con-fines-especiales-infraestructura-para-la-recarga-de-vehiculos-electricos.md, papers/2026-11-10-guia-bt-17-dispositivos-generales-e-individuales-de-mando-y-proteccion.md, papers/2026-11-10-guia-bt-23-proteccion-contra-sobretensiones.md, papers/2026-11-10-guia-bt-25-instalaciones-interiores-en-viviendas-numero-de-circuitos-y-caracteristicas.md, papers/2026-11-10-guia-bt-26-instalaciones-interiores-en-viviendas-prescripciones-generales-de-instalaciones.md]
created: 2026-11-14
updated: 2026-11-14
---

# Protección diferencial y selectividad en baja tensión

El interruptor diferencial protege contra los contactos indirectos y, con 30 mA, complementa la protección contra los contactos directos. Este artículo integra cuándo se exige, cómo se coordina en serie para que actúe solo el dispositivo más próximo al defecto y dónde se ubica, reuniendo lo que la ITC-BT-24 fija como obligación con lo que las guías BT-17, BT-23, BT-25 y BT-26 desarrollan como criterio de buena práctica.

## Puntos clave

- El diferencial de **30 mA** es una **medida complementaria**, no una protección completa: cubre el fallo de otra protección o una imprudencia. Debe ser de **clase A** cuando se prevean corrientes diferenciales no senoidales (ITC-BT-24).
- La **selectividad en serie** exige que el diferencial aguas arriba tenga una intensidad diferencial residual de al menos **tres veces** la del aguas abajo, sea de **tipo S** y su tiempo de no actuación supere el tiempo total de operación del de aguas abajo (Guía-BT-25, Guía-BT-26).
- La **ubicación** importa: el protector contra sobretensiones va aguas arriba del diferencial, o aguas abajo si el diferencial es tipo S; con un único diferencial, este debe ser de disparo instantáneo (Guía-BT-25).
- En la **recarga de vehículo eléctrico** la ITC-BT-52 exige clase A y 30 mA por punto; la Guía-BT-52 admite tipo B o tipo A con RDC-DD para corrientes con componente continua.
- La **subdivisión en circuitos** y la selectividad respecto a los dispositivos generales forman parte del mismo criterio de coordinación (ITC-BT-19).
- Los **tiempos de desconexión** dependen del esquema de conexión a tierra: ver [[esquemas-conexion-neutro-masas]].

## Detalles

### Cuándo se exige

La ITC-BT-24 sitúa el diferencial residual de 30 mA como medida complementaria contra los contactos directos e indirectos, y aclara que jamás constituye protección completa por sí mismo. En los circuitos con corrientes diferenciales no senoidales (por ejemplo, salas de radiología intervencionista) exige clase A. La protección principal contra los contactos indirectos sigue siendo el corte automático coordinado con el esquema de conexión a tierra, no el diferencial aislado.

### Selectividad en serie

La Guía-BT-25 y la Guía-BT-26 desarrollan el criterio del apartado 2.1 de la ITC-BT-25: el diferencial aguas arriba debe tener una intensidad diferencial-nominal de al menos tres veces la del aguas abajo, y su tiempo de no actuación debe superar el tiempo total de operación del de aguas abajo, lo que en la práctica se consigue con diferenciales de tipo S. La Guía-BT-17 concreta las condiciones de selectividad total entre diferenciales en serie y admite que la ITC-BT-17 solo exige que exista selectividad.

Esta regla es una **ampliación** de la guía: la ITC-BT-25 no fija la relación de tres veces ni el tipo S; solo remite a la ITC-BT-24 para la protección contra contactos indirectos. Se aplica como criterio de proyecto, no como exigencia del BOE.

### Ubicación respecto a otras protecciones

La Guía-BT-25 sitúa el dispositivo de protección contra sobretensiones aguas arriba del diferencial (entre el interruptor general y el propio diferencial), salvo que el diferencial sea selectivo tipo S; exige un dispositivo recomendado por el fabricante aguas arriba del limitador para mantener la continuidad del servicio y, con un único diferencial, que sea de disparo instantáneo. La Guía-BT-23 añade que en edificios con pararrayos se instala un protector tipo 1 y, si la distancia alcanza los 10 m, un segundo tipo 2.

### Tipo de diferencial y componente continua

La ITC-BT-52 exige, por punto de recarga, un diferencial de clase A y 30 mA máximos. La Guía-BT-52 admite además diferenciales de tipo B o de tipo A con RDC-DD conforme a la IEC 62955 (UNE-HD 60364-7-722) para las corrientes con componente continua, una ampliación que la ITC no recoge.

### Tiempos de desconexión

La ITC-BT-24 fija los tiempos máximos de interrupción según el esquema de conexión a tierra. En TN dependen de la tensión: 0,4 s para 230 V, 0,2 s para 400 V y 0,1 s por encima de 400 V. En IT son 0,4 s con neutro no distribuido y 0,8 s con neutro distribuido. En TT la condición es R_A × I_a ≤ U, con diferenciales preferentes y selectividad mediante temporizados tipo S de 1 s como máximo; la Tabla A de tiempos de desconexión en TT (0,2 / 0,07 / 0,04 s) que añade la Guía-BT-24 es una ampliación respecto del BOE. El desarrollo de cada esquema está en [[esquemas-conexion-neutro-masas]].

## Relacionado

- [[esquemas-conexion-neutro-masas]] — TT, TN e IT y sus condiciones de protección
- [[itc-bt-24-instalaciones-interiores-o-receptoras-proteccion-contra-los-contactos-directos-e-indirectos]] — texto consolidado de la instrucción
- [[guia-bt-24-proteccion-contra-los-contactos-directos-e-indirectos]] — criterio de la guía y sus divergencias
- [[itc-bt-19-instalaciones-interiores-o-receptoras-prescripciones-generales]] — subdivisión en circuitos y selectividad
- [[itc-bt-52-instalaciones-con-fines-especiales-infraestructura-para-la-recarga-de-vehiculos-electricos]] — diferencial en la recarga de vehículo eléctrico
- [[instalaciones-interiores-viviendas-bt]] — circuitos C1–C13 y diferencial general
- [[criterios-puesta-a-tierra]] — toma de tierra y resistencia de defecto
- [[divergencias-guias-tecnicas-rebt-vs-itc-bt]] — mapa de las 221 divergencias y sus tipos
