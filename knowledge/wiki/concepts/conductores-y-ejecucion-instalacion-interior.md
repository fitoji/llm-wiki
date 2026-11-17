---
title: Conductores y ejecución de la instalación interior en viviendas (Guía-BT-26)
type: concept
tags: [rebt, baixa-tensio, espana, guia-tecnica, itc-bt, conductores, ejecucion]
sources: [papers/2026-11-10-guia-bt-26-prescripciones-generales.md, papers/2026-11-10-rebt-itc-bt-26-instalaciones-interiores-en-viviendas-prescripciones-generales-de-instalacion.md, papers/2026-11-10-guia-bt-26-instalaciones-interiores-en-viviendas-prescripciones-generales-de-instalaciones.md, articles/2026-11-17-prescripciones-generales-viviendas-tierra-cables-itc-bt-26.md]
created: 2026-11-10
updated: 2026-11-17
---

# Conductores y ejecución de la instalación interior en viviendas (Guía-BT-26)

Prescripciones generales de la Guía-BT-26 sobre conductores (naturaleza, secciones, identificación, conexiones) y ejecución de la instalación (sistemas, condiciones generales), incluido el cuadro general de distribución.

## Puntos clave
- Conductores activos de cobre, aislados, tensión asignada mínima 450/750 V. Secciones según ITC-BT-25. Tipos habituales: H07V-U (clase 1, rígido), H07V-R (clase 2, rígido), H07V-K (clase 5, flexible). Norma UNE 21.031-3 y UNE 21.022.
- Conductores de protección de cobre con el mismo aislamiento que los activos, misma canalización, sección según ITC-BT-19 (igual a la del conductor de fase para secciones habituales ≤ 16 mm²).
- Identificación por color: neutro (o previsión de paso a neutro) azul claro; protección verde-amarillo; fases marrón, negro o gris.
- En los circuitos de alumbrado, la **vuelta de llave o retorno** entre el mecanismo de maniobra y la luminaria se identifica con un color distinto al de la fase de alimentación (por ejemplo, fase marrón y retorno negro o gris). Es una práctica de identificación, no un color adicional fijado por la ITC-BT-26.
- Conexiones según ITC-BT-19 apartado 2.11; se admiten conexiones en paralelo entre bases juntas con bornes previstos. Productos: bornes UNE-EN 60998, bases UNE 20315, cajas de empalme UNE 20451. Bases de 16 A previstas para dos conductores por terminal; las de 25 A no lo exigen normativamente. Las conexiones deben ser accesibles.
- Queda **prohibido unir o derivar conductores por simple retorcimiento o arrollamiento** entre sí y cubrirlos con cinta aislante. La unión se hace con bornes de conexión individuales, bloques o regletas, o bridas de conexión, dentro de cajas de empalme o derivación (ITC-BT-19, 2.11).
- Conexiones en canales protectoras de grado IP4X o superior ("canales con tapa de acceso que solo puede abrirse con herramientas", UNE-EN 50.085-1) admiten empalmes en su interior.
- Cuadro general de distribución según ITC-BT-17: envolvente IP30 e IK07, placa identificadora permanente con nombre/marca del instalador, fecha de la instalación e intensidad asignada del IGA. Normas de producto: envolvente UNE 20451, aparamenta UNE-EN 60439-3, ICP UNE 20317, automáticos UNE-EN 60898, diferenciales UNE-EN 61008/61009, fusibles UNE-EN 60269-3, bornes UNE-EN 60998.
- Dentro del cuadro, la **derivación de la línea principal de tierra (DLPT)** se reparte a los conductores de protección de cada circuito mediante una barra o pletina de tierra, o regletas repartidoras verdes-amarillas montadas en carril DIN. La conexión debe ser por presión o tornillo con apriete asegurado, no por simple contacto.
- Sistemas de instalación: empotrada (cables aislados bajo tubo flexible o curvable) o superficial (tubo curvable, rígido, canal protectora cerrada, canalizaciones prefabricadas). Diámetros de tubo según tabla (1,5–6 mm², 1–5 conductores). Para más de 5 conductores o secciones distintas en el mismo tubo: sección interior ≥ 3× (empotrada) o ≥ 2,5× (superficial) la sección ocupada. Características mínimas: tubo rígido UNE-EN 50086-2-1, curvable UNE-EN 50086-2-2, flexible UNE-EN 50086-2-3, canal UNE-EN 50085-1, canalización prefabricada UNE-EN 60439-2.
- Condiciones generales: no usar un mismo conductor neutro para varios circuitos; todo conductor debe poder seccionarse en cualquier punto de derivación; tomas de una misma habitación conectadas a la misma fase; cubiertas/tapas/mandos de aparatos en cocinas, baños, secaderos y locales húmedos de material aislante; instalación empotrada en cajas especiales (metálicas aisladas o puestas a tierra); aparatos en marcos metálicos solo si no permiten puesta bajo tensión del marco (conectado a tierras); aparatos empotrados en bastidores de madera u otro material aislante según ITC-BT 49.

## Detalles
La protección contra contactos indirectos se realiza mediante puesta a tierra de las masas y los dispositivos del apartado 2.1 de la ITC-BT-25: diferenciales ≤ 30 mA, intensidad asignada ≥ IGA; en serie, intensidad diferencial aguas arriba ≥ 3× la de aguas abajo y tipo S. Los conductores de protección no forman parte de la canalización de alimentación y tienen protección mecánica según la tabla de secciones.

### Colores, retornos y secciones

La ITC-BT-26 fija los colores de los conductores: fase en marrón o negro, gris cuando hay que distinguir tres fases, neutro en azul claro y protección en verde-amarillo. El recorte divulgativo añade una práctica habitual en alumbrado: la **vuelta de llave o retorno** entre el mecanismo y la luminaria se lleva en un color distinto al de la fase de alimentación (por ejemplo, fase marrón y retorno negro o gris) para identificarla rápidamente. La ITC-BT-26 no asigna un color específico al retorno, así que se trata de una convención de identificación, no de un requisito adicional.

![Código de colores de cables normalizado en viviendas](https://circuitoelectrico.com/wp-content/uploads/2026/07/Codigo-colores-cables-normalizado.webp)

La sección del conductor de protección se deduce de la del conductor de fase según la ITC-BT-19: $S_{PE} = S_F$ si $S_F \leq 16\ \text{mm}^2$; $S_{PE} = 16\ \text{mm}^2$ si $16 < S_F \leq 35\ \text{mm}^2$; y $S_{PE} = S_F/2$ si $S_F > 35\ \text{mm}^2$. Para las secciones habituales de vivienda (1,5 a 6 mm²) el PE tiene la misma sección que la fase.

### Barra de tierra del cuadro y derivación de la línea principal de tierra

Dentro del cuadro general, todos los conductores de protección de los circuitos llegan a una **barra o pletina de tierra**. Esa barra se une a la **derivación de la línea principal de tierra (DLPT)**, que va al electrodo de puesta a tierra del edificio. En los cuadros actuales la barra lleva el símbolo de tierra (⏚) y está separada de los bornes de fase y neutro.

![Bornes y pletinas de conexión de los conductores de protección a la derivación de la línea principal de tierra en el cuadro general](https://circuitoelectrico.com/wp-content/uploads/2024/07/Bornes-y-pletinas-conexion-al-cuadro-conductores-de-proteccion.jpg)

Para el reparto se usan regletas repartidoras o bloques de bornes verdes-amarillos, con fijación de pestaña para carril DIN o con tornillos de apriete asegurado. La conexión debe mantener la equipotencialidad frente a vibraciones y tracciones. Un falso contacto en esta barra anula la protección: conviene comprobar la continuidad y medir la resistencia de puesta a tierra con un telurómetro.

### Diámetro de tubo: matiz sobre la tabla divulgativa

El recorte resume el tubo empotrado como «corrugado de diámetro ≥ 16 mm». Es una simplificación: la referencia es la **tabla 5 de la ITC-BT-21**, que fija el diámetro exterior mínimo en función del número y la sección de los conductores. Para 1,5 mm², el mínimo es 12 mm con uno o dos conductores y 16 mm con tres o más; para 2,5 mm², 12 mm con uno, 16 mm con dos y 20 mm con tres o más; para 4 mm², de 12 a 25 mm; y para 6 mm², de 12 a 25 mm. El valor de 16 mm es habitual en los circuitos de vivienda, pero no es un mínimo universal.

### Montaje empotrado y superficial

La instalación **empotrada** aloja los cables en tubos flexibles o curvables dentro de rozas de paredes, tabiques, techos o bajo el pavimento. Queda oculta tras el yeso, el mortero o el pavimento, lo que protege los conductores de impactos y agentes ambientales. Cuando la roza discurre por el suelo, el tubo debe resistir una compresión mínima de 450 N y quedar recubierto por al menos 1 cm de mortero antes de la solera.

![Tubos en canalizaciones empotradas en la pared](https://circuitoelectrico.com/wp-content/uploads/2026/04/Tubos-canalizaciones-empotradas.webp)

La instalación **superficial** se reserva para garajes, trasteros, lavaderos, zonas técnicas o reformas sin rozas. La ITC-BT-26 admite tres configuraciones: tubo curvable o rígido, canal protectora cerrada con tapa desmontable y canalizaciones prefabricadas con conductores ya montados.

![Conductores aislados bajo tubo rígido en montaje superficial sobre paredes](https://circuitoelectrico.com/wp-content/uploads/2026/04/Conductores-aislados-tubo-rigido-superficial.webp)

![Canaletas de pared, suelo y rodapié en una oficina](https://circuitoelectrico.com/wp-content/uploads/2026/04/Canaletas-pared-suelo-rodapie.webp)

![Canalización eléctrica prefabricada en la cocina de una vivienda](https://circuitoelectrico.com/wp-content/uploads/2026/07/Canalizacion-electrica-prefabricada-cocina-vivienda.webp)

### Mecanismos en zonas húmedas y marcos metálicos

En cocinas, cuartos de baño, secaderos y locales húmedos o mojados, los mecanismos (interruptores, bases, reguladores, mandos y pulsadores) deben ser de material aislante y disponer de cubiertas, tapas o envolventes aislantes. La misma exigencia se aplica a los locales con paredes y suelos conductores.

![Mecanismos eléctricos aislantes en zonas húmedas o mojadas](https://circuitoelectrico.com/wp-content/uploads/2026/07/Mecanismos-electricos-aislantes-zonas-humedas.webp)

Las cajas de empotrar metálicas deben tener un revestimiento interior aislante y estar conectadas a la red de tierra. Cuando se montan mecanismos sobre carpinterías o marcos metálicos, el mecanismo debe aislar las partes activas e impedir la puesta bajo tensión del marco, y el marco debe conectarse directamente al PE. Los mecanismos sobre bastidores, mamparas, paneles de madera o tabiques combustibles se rigen por la ITC-BT-49.

![Instalación de mecanismos eléctricos sobre marcos metálicos con puesta a tierra del marco](https://circuitoelectrico.com/wp-content/uploads/2026/07/Instalacion-electrica-marcos-metalicos.webp)

### Ubicación y espacio libre del cuadro

La ITC-BT-17 exige prever el cuadro general junto a la puerta de entrada de la vivienda y prohíbe situarlo en dormitorios, baños o aseos, con una altura de montaje entre 1,4 y 2 m desde el suelo (ver [[itc-bt-17-instalaciones-de-enlace-dispositivos-generales-e-individuales-de-mando-y-proteccion-interruptor]]). El recorte añade recomendaciones prácticas que el REBT no fija como distancias obligatorias: 1,10 m libres en el frente, 20 cm en los laterales y un 20–25 % de espacio interior libre para futuras ampliaciones.

## Divergencias con la ITC-BT-26
Comparación de la Guía-BT-26 (edición sep 03, revisión 1) con el texto consolidado de la ITC-BT-26 del BOE (RD 842/2002). En todos los casos prevalece la ITC-BT-26.
- [ampliacion] **Envolvente del cuadro general de distribución.** La Guía-BT-26 (edición sep 03, revisión 1, apartado 5 y figura) fija "Envolvente con un IP 30 e IK 07" y añade una tabla de normas de producto (UNE 20451 para la envolvente, UNE-EN 60439-3 para el conjunto de aparamenta, UNE 20317 para el interruptor de control de potencia, UNE-EN 60898 para los interruptores automáticos, UNE-EN 60947-3 para interruptores y seccionadores, UNE-EN 61008 y UNE-EN 61009 para los diferenciales, UNE-EN 60269-3 para los fusibles y UNE-EN 60998 para los bornes de conexión). La ITC-BT-26 (apartado 5 del texto consolidado del BOE) solo remite a la ITC-BT-17 y a las ITC-BT-10 e ITC-BT-25, sin indicar grado IP ni IK ni normas de producto. Prevalece la ITC-BT-26.
- [ampliacion] **Criterio de los interruptores diferenciales.** La Guía-BT-26 (edición sep 03, revisión 1, apartado 4) desarrolla los criterios del apartado 2.1 de la ITC-BT-25: interruptores diferenciales con una intensidad diferencial residual máxima de 30 mA e intensidad asignada superior o igual que la del interruptor general; en serie, el diferencial instalado aguas arriba con una intensidad diferencial-nominal como mínimo tres veces superior a la del aguas abajo y de tipo S. La ITC-BT-26 (apartado 4) se limita a remitir al apartado 2.1 de la ITC-BT-25 sin fijar esos valores. Prevalece la ITC-BT-26.
- [ampliacion] **Tipos de conductor activo.** La Guía-BT-26 (edición sep 03, revisión 1, apartado 6.1.1) identifica los conductores aislados de uso habitual (H07V-U con conductor de cobre clase 1 según UNE 21.031-3, H07V-R con clase 2 y H07V-K con clase 5, con la UNE 21 022 como norma de características constructivas y eléctricas de las clases). La ITC-BT-26 (apartado 6.1.1) solo fija que los conductores activos son de cobre, aislados y con tensión asignada 450/750 V como mínimo, y remite a la ITC-BT-25 para circuitos y secciones. Prevalece la ITC-BT-26.
- [ampliacion] **Sección del conductor de protección.** La Guía-BT-26 (edición sep 03, revisión 1, apartado 6.1.2) añade que, para las secciones habituales de los conductores de fase de las instalaciones interiores de viviendas, la sección del conductor de protección es igual a la del conductor de fase porque no suelen emplearse conductores de fase de sección superior a 16 mm². La ITC-BT-26 (apartado 6.1.2) remite a la sección indicada en la ITC-BT-19 sin esa equivalencia. Prevalece la ITC-BT-26.
- [ampliacion] **Conexiones.** La Guía-BT-26 (edición sep 03, revisión 1, apartado 6.3) añade una tabla de normas de producto (bornes de conexión UNE-EN 60998, bases de toma de corriente UNE 20315, cajas de empalme y/o derivación UNE 20451), precisa que las bases de 16 A de la UNE 20315 están previstas para la conexión de dos conductores por terminal mientras que en las de 25 A no se exige normativamente esa característica, exige que las conexiones sean accesibles para facilitar su verificación, ensayos, mantenimiento y substitución, y admite empalmes de conductores y conexiones a los mecanismos en las canales protectoras de grado IP4X clasificadas como "canales con tapa de acceso que solo puede abrirse con herramientas" (UNE-EN 50.085-1, ITC-BT-21 apartado 3.1). La ITC-BT-26 (apartado 6.3) solo admite las conexiones en paralelo entre bases de toma de corriente juntas que dispongan de bornes de conexión previstos para varios conductores. Prevalece la ITC-BT-26.
- [ampliacion] **Ejecución de las instalaciones.** La Guía-BT-26 (edición sep 03, revisión 1, apartado 7.1) añade las tablas de diámetros exteriores de tubo (de 12 mm para 1,5 mm² con un conductor hasta 25 mm en la instalación empotrada con 6 mm² y cinco conductores; de 12 a 25 mm en la superficial), la regla de la ITC-BT-21 de sección interior mínima igual a 3 veces la sección ocupada por los conductores (empotrada) y a 2,5 veces (superficial) cuando hay más de 5 conductores por tubo o secciones distintas en el mismo tubo, y las características mínimas de los sistemas de conducción de cables (tubo rígido UNE-EN 50086-2-1, tubo curvable UNE-EN 50086-2-2, tubo flexible UNE-EN 50086-2-3, canal protectora UNE-EN 50085-1 y canalización prefabricada UNE-EN 60439-2). La ITC-BT-26 (apartado 7.1) enumera los sistemas de instalación y remite a las ITC-BT-20 e ITC-BT-21 sin tablas de diámetros, sin factores de sección ocupada y sin características mínimas de producto. Prevalece la ITC-BT-26.
- [conflicto] **Diámetro mínimo del tubo empotrado.** El recorte divulgativo de circuitoelectrico.com (2024) resume el tubo corrugado de vivienda como «ø ≥ 16 mm». La ITC-BT-21 (tabla 5) admite 12 mm para 1,5 mm² con uno o dos conductores y para 2,5 mm² con un conductor, y exige 16 mm o más según el número de conductores y la sección. Prevalece la ITC-BT-21.

## Relacionado
- [[toma-de-tierra-edificios-viviendas]]
- [[instalaciones-interiores-viviendas-bt]]
- [[itc-bt-26-instalaciones-interiores-en-viviendas-prescripciones-generales-de-instalacion]]
- [[reglament-electrotecnic-baixa-tensio]]
