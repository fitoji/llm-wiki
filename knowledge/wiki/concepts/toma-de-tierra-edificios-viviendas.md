---
title: Toma de tierra en edificios de viviendas (Guía-BT-26)
type: concept
tags: [rebt, baixa-tensio, espana, guia-tecnica, itc-bt, toma-de-tierra, edificios]
sources: [papers/2026-11-10-guia-bt-26-prescripciones-generales.md, papers/2026-11-10-rebt-itc-bt-18-instalaciones-de-puesta-a-tierra.md, papers/2026-11-10-guia-bt-26-instalaciones-interiores-en-viviendas-prescripciones-generales-de-instalaciones.md, articles/2026-11-17-prescripciones-generales-viviendas-tierra-cables-itc-bt-26.md]
created: 2026-11-10
updated: 2026-11-17
---

# Toma de tierra en edificios de viviendas (Guía-BT-26)

Prescripciones generales de la Guía-BT-26 (edición sep 03, revisión 1) sobre toma de tierra, protección contra contactos indirectos, cuadro general y conductores en instalaciones interiores de viviendas.

## Puntos clave
- En toda nueva edificación se establece una toma de tierra de protección: cable rígido de cobre desnudo en anillo cerrado en el fondo de las zanjas de cimentación, que interese todo el perímetro del edificio. Profundidad mínima de enterramiento 0,8 m. Sección mínima según ITC-BT-18 (con un mínimo de 35 mm² de Cu según NTE 1973 para el anillo). En rehabilitación se pueden usar electrodos en patios o jardines.
- La ITC-BT-18 concreta dos valores que conviene no perder de vista: la profundidad de enterramiento **nunca será inferior a 0,50 m** y, para un conductor enterrado protegido contra la corrosión, la sección mínima de cobre es **16 mm²** (25 mm² si no está protegido). Los 35 mm² del anillo y los 0,8 m son criterios de la Guía-BT-26/NTE 1973, más exigentes que el mínimo reglamentario.
- Electrodos verticales (picas) de 2 m cuando sea necesario disminuir la resistencia; separados al menos 2 veces su longitud. Tabla A orientativa del número de picas según terreno, longitud del anillo y presencia de pararrayos; resistencia a tierra objetivo < 15 Ω con pararrayos y < 37 Ω sin pararrayos.
- A la toma de tierra se conectan: masas metálicas importantes, masas accesibles de receptores, depósitos de gasóleo, instalaciones de calefacción general, agua, gas canalizado, antenas de radio/TV. Las partes conductoras con origen exterior se conectan a tierra tan cerca como sea posible de la entrada.
- Puntos de puesta a tierra (5 posibles): a) patios de luces (rehabilitación), b) centralización de contadores, c) base de estructuras de ascensores/montacargas, d) caja general de protección, e) locales con elementos a poner a tierra. En nuevas instalaciones: b), c), d) y e) si procede.
- Cada punto de puesta a tierra (PPAT) es un elemento superficial que interconecta la **línea de enlace con tierra (LET)** con la **línea principal de tierra (LPT)**. Aloja una caja seccionadora con puente de prueba desmontable para medir la resistencia de tierra sin desconectar la instalación. Es la frontera entre el tramo enterrado y el tramo visible.
- Líneas principales de tierra: conductor de protección desde el borne de puesta hasta el embarrado de protección de la centralización de contadores, por la misma canalización que la LGA. Derivaciones: desde el embarrado hasta el origen de la instalación interior. La instalación interior usa conductores de protección.
- Secciones de conductores de protección según ITC-BT-19: si S ≤ 16 mm², Sp = S; si 16 < S ≤ 35, Sp = 16 mm²; si S > 35, Sp = S/2 (mínimo 2,5 mm² protegido mecánicamente o 4 mm² sin protección). Líneas principales: mínimo 16 mm² de Cu, protección mecánica donde sean accesibles.
- No se pueden usar como conductores de tierra tuberías de agua, gas, calefacción, desagües, conductos de evacuación, cubiertas metálicas de cables ni partes conductoras de sistemas de conducción.
- Conexiones en conductores de tierra mediante dispositivos con tornillos de apriete u otros similares que garanticen conexión continua y perfecta.

## Detalles
Las conexiones a la estructura metálica del edificio o a los hierros principales de las zapatas de hormigón armado se establecen por soldadura aluminotérmica o autógena. Las tomas de tierra en edificios existentes pueden realizarse en patios de luces o jardines particulares.

### Puntos de puesta a tierra y línea de enlace con tierra

Los **puntos de puesta a tierra (PPAT)** son los bornes o elementos superficiales donde la instalación interior se conecta con el electrodo enterrado. Cada PPAT aloja una caja seccionadora con un **puente de prueba desmontable**: al abrir el puente se aísla el electrodo y se puede medir su resistencia sin desconectar la instalación. El PPAT marca la frontera entre el tramo enterrado y el tramo visible de la red de tierra.

![Interior de una caja seccionadora de tierra con puente de prueba desmontable](https://circuitoelectrico.com/wp-content/uploads/2026/08/caja-seccionadora-tierra-puente-de-prueba-arqueta.webp)

Los PPAT se sitúan en los emplazamientos previstos por la ITC-BT-26: patios de luces en rehabilitaciones, local o armario de centralización de contadores, caja general de protección (CGP), locales de servicios generales y bases de las estructuras metálicas de ascensores y montacargas. El punto principal en edificios con contadores centralizados es el de la centralización; el de la CGP se coloca junto a ella para facilitar las mediciones periódicas.

![Plano con las ubicaciones de los puntos de puesta a tierra en un edificio](https://circuitoelectrico.com/wp-content/uploads/2026/08/ubicacion-puntos-puesta-a-tierra-edificio-contadores.webp)

Cada conductor que une un PPAT con el anillo enterrado se denomina **línea de enlace con tierra (LET)**. En un edificio puede haber varias LET: CGP, contadores, ascensores y antenas de TV/radio.

![Anillo enterrado en la cimentación con cuatro puntos de puesta a tierra y sus líneas de enlace](https://circuitoelectrico.com/wp-content/uploads/2024/07/Ejemplo-de-anillo-enterrado-4-puntos-de-puesta-a-tierra.jpg)

### Profundidad, sección y comprobación

La ITC-BT-18 fija la profundidad mínima de enterramiento en **0,50 m** y la sección mínima del conductor enterrado según su protección: **16 mm² de cobre** si está protegido contra la corrosión y **25 mm²** si no lo está (o 50 mm² de hierro). La Guía-BT-26 recomienda 0,8 m de profundidad y 35 mm² de cobre según la NTE 1973; son valores más exigentes, no el mínimo reglamentario.

La instalación se comprueba con un **telurómetro** midiendo entre el PPAT y tierra, con el puente de prueba abierto. En terrenos desfavorables, la ITC-BT-18 exige poner al descubierto los electrodos y conductores de enlace para examen al menos una vez cada cinco años.

### Cómo leer la Tabla A de la Guía-BT-26

La Tabla A es orientativa: no aparece en la ITC-BT-26, que solo exige electrodos verticales «cuando se prevea la necesidad de disminuir la resistencia de tierra». Se lee por columnas: cada tipo de terreno tiene dos subcolumnas, «sin pararrayos» y «con pararrayos». El número de cada celda es la longitud mínima del conductor enterrado del anillo (∑L, en metros) exigida para esa fila, que indica el número de picas de 2 m. El símbolo «^» significa que hay que aumentar la longitud del anillo en lugar de añadir picas.

- Sin pararrayos la resistencia objetivo es < 37 Ω (con pararrayos, < 15 Ω), así que se necesita menos electrodo.
- En terrenos orgánicos, arcillas y margas **sin pararrayos**, 0 picas requieren ∑L ≥ 25 m; la tabla no prevé añadir picas en esa columna: si el anillo es más corto hay que alargarlo.
- En arenas arcillosas y graveras **sin pararrayos**, 0 picas requieren ∑L ≥ 28 m y 1 pica reduce el mínimo a 25 m.
- Ojo con el nombre: «arenas arcillosas y graveras» (2.ª columna) no es «grava y arena silícea» (4.ª columna, mucho más resistiva). En esta última, 0 picas exigen ∑L ≥ 162 m.

Ejemplo: edificio sin pararrayos con L1 = 7 m y L2 = 8 m en terreno arcilloso con grava. En un anillo rectangular L3 = L1 y L4 = L2, luego ∑L = 2 · (7 + 8) = 30 m. Como 30 m ≥ 28 m (y también ≥ 25 m), la tabla da **0 picas**: basta el anillo enterrado de la cimentación. El ejemplo de la propia guía es el caso contrario: con pararrayos, en arena arcillosa y ∑L = 33 m hacen falta 8 picas y 2 m más de conductor, porque la fila de 8 picas marca 35 m.

Nota: el Markdown generado desde el PDF muestra «L = 3L1 + 3L2 + 3L3 + 3L4»; parece un artefacto de la extracción. Tomado literalmente daría 90 m, que también cae en 0 picas, así que la conclusión del ejemplo no cambia.

## Divergencias con la ITC-BT-26
Comparación de la Guía-BT-26 (edición sep 03, revisión 1) con el texto consolidado de la ITC-BT-26 del BOE (RD 842/2002). En todos los casos prevalece la ITC-BT-26.
- [ampliacion] **Sección mínima del conductor de tierra.** La Guía-BT-26 (edición sep 03, revisión 1, apartado 3.1) fija que los conductores de cobre desnudos utilizados como electrodos son de construcción y resistencia eléctrica según la clase 2 de la UNE 21 022, con una sección mínima de 35 mm² según la NTE 1973 "Puesta a tierra". La ITC-BT-26 (apartado 3.1 del texto consolidado del BOE) solo indica "una sección mínima según se indica en la ITC-BT-18", sin fijar valor; la propia guía lo hace constar en su apartado 00, al señalar que la tabla de la ITC-BT-18 apartado 3.2 presenta valores inferiores a los del reglamento de 1973. Prevalece la ITC-BT-26.
- [ampliacion] **Profundidad de enterramiento.** La Guía-BT-26 (edición sep 03, revisión 1, apartado 3.1) recomienda una profundidad mínima de enterramiento del conductor de 0,8 m. La ITC-BT-26 (apartado 3.1) no fija profundidad de enterramiento del anillo. Prevalece la ITC-BT-26.
- [ampliacion] **Electrodos verticales y resistencia de tierra.** La Guía-BT-26 (edición sep 03, revisión 1, apartado 3.1 y Tabla A) añade picas de puesta a tierra UNE 202 006 de 2 metros de longitud, separadas al menos dos veces su longitud y repartidas proporcionalmente a lo largo del anillo enterrado, un número orientativo de electrodos verticales según características del terreno, longitud del anillo y presencia de pararrayos, y una resistencia a tierra obtenida que "debería ser, en la práctica, inferior a 15 Ω para edificios con pararrayos y de 37 Ω para edificios sin pararrayos". La ITC-BT-26 (apartado 3.1) solo menciona que al anillo "deberán conectarse electrodos verticalmente hincados en el terreno cuando, se prevea la necesidad de disminuir la resistencia de tierra", sin valores. Prevalece la ITC-BT-26.
- [ampliacion] **Secciones de las líneas de enlace con tierra.** La Guía-BT-26 (edición sep 03, revisión 1, apartado 3.1 y tabla de la ITC-BT-18) reproduce las secciones mínimas convencionales de los conductores de tierra o líneas de enlace con el electrodo: protegido contra la corrosión y protegido mecánicamente, según el apartado 3.4 (1) de la ITC-BT-18 (Sp = S si S ≤ 16 mm², Sp = 16 mm² si 16 < S ≤ 35 mm², Sp = S/2 si S > 35 mm²); protegido contra la corrosión y no protegido mecánicamente, 16 mm² de cobre o 16 mm² de acero galvanizado; no protegido contra la corrosión y protegido mecánicamente, 25 mm² de cobre o 50 mm² de hierro. La ITC-BT-26 (apartado 3.1) solo remite de forma genérica a la ITC-BT-18 sin reproducir esos valores. Prevalece la ITC-BT-26.
- [ampliacion] **Partes conductoras con origen exterior.** La Guía-BT-26 (edición sep 03, revisión 1, apartado 3.2) añade que "cuando dichas partes conductoras tengan su origen en el exterior del edificio, deberán conectarse a tierra tan cerca como sea posible de su entrada al edificio". La ITC-BT-26 (apartado 3.2) enumera los elementos a conectar a tierra sin recoger esa exigencia. Prevalece la ITC-BT-26.
- [ampliacion] **Puntos de puesta a tierra.** La Guía-BT-26 (edición sep 03, revisión 1, apartado 3.3) precisa que en edificios de viviendas existen cinco posibles puntos o bornes de puesta a tierra, que pueden coexistir y que en ese caso se considera borne principal el situado en la centralización de contadores; que en nuevas instalaciones los puntos de conexión deben situarse en las ubicaciones b), c) y d) y, si procede, en la e); que en rehabilitación la ubicación a) es orientativa; y que el punto de puesta a tierra de la caja general de protección debe estar situado junto a ella. La ITC-BT-26 (apartado 3.3) se limita a enumerar las ubicaciones a) a e) sin criterio de selección ni borne principal. Prevalece la ITC-BT-26.
- [ampliacion] **Líneas principales de tierra y derivaciones.** La Guía-BT-26 (edición sep 03, revisión 1, apartado 3.4) define que tanto las líneas principales como sus derivaciones forman parte de los conductores de protección según la ITC-BT-18, que la línea principal es el conductor de protección que va desde el borne de puesta hasta el embarrado de protección y bornes de salida de la centralización de contadores (o discurre por la misma canalización que la LGA hasta cada embarrado si hay varias centralizaciones) y que la derivación es el conductor de protección que va desde ese embarrado hasta el origen de la instalación interior, por la misma canalización que las derivaciones individuales. La ITC-BT-26 (apartado 3.4) fija las canalizaciones y la sección mínima (16 mm² de cobre) sin definir línea principal ni derivación. Prevalece la ITC-BT-26.
- [conflicto] **Sección y profundidad del anillo en el recorte divulgativo.** El recorte de circuitoelectrico.com (2024) presenta 35 mm² y 0,8 m como mínimos del anillo de cimentación. La ITC-BT-18 fija 16 mm² de cobre para un conductor enterrado protegido contra la corrosión y una profundidad nunca inferior a 0,50 m. Los valores de 35 mm² y 0,8 m proceden de la NTE 1973 y de la Guía-BT-26; el mínimo reglamentario es el de la ITC-BT-18, sin perjuicio de que el proyecto adopte los valores más exigentes.

## Relacionado
- [[conductores-y-ejecucion-instalacion-interior]]
- [[instalaciones-interiores-viviendas-bt]]
- [[itc-bt-26-instalaciones-interiores-en-viviendas-prescripciones-generales-de-instalacion]]
- [[reglament-electrotecnic-baixa-tensio]]
- [[criterios-puesta-a-tierra]] — criterios generales de la ITC-BT-18
