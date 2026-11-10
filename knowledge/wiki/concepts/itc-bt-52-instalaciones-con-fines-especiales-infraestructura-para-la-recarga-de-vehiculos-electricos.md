---
title: ITC-BT-52 — Instalaciones con fines especiales. Infraestructura para la recarga de vehículos eléctricos
type: concept
tags: [rebt, baja-tension, itc-bt-52, recarga-vehiculo-electrico]
sources: [papers/2026-11-10-rebt-itc-bt-52-instalaciones-con-fines-especiales-infraestructura-para-la-recarga-de-vehiculos-electricos.md]
created: 2026-11-10
updated: 2026-11-10
---

# ITC-BT-52 — Instalaciones con fines especiales. Infraestructura para la recarga de vehículos eléctricos

ITC del REBT que regula las instalaciones de recarga de vehículos eléctricos en lugares públicos o privados: define los cuatro modos de carga, las clases de estaciones (punto simple y SAVE) y los cuatro esquemas de conexión (colectivo con contador principal, individual y circuitos adicionales). Fija la previsión de cargas con el SPL y el factor de simultaneidad (0,3 o 1,0), las protecciones de seguridad (diferencial de 30 mA clase A por punto de conexión, grados IP/IK y sobretensiones) y la red de tierra exterior con tensión de contacto máxima de 24 V.

- Objeto: prescripciones para las instalaciones de recarga de vehículos eléctricos dentro del ámbito del REBT, con titularidad individual, colectiva o de un gestor de cargas, en lugares públicos o privados (unifamiliares, aparcamientos colectivos, flotas, vía pública y áreas de servicio).
- No es aplicable a la recarga por inducción ni a baterías que desprendan gases durante la recarga; la recarga en locales cerrados de aparcamiento solo se permite sin desprendimiento de gases y fuera de locales con riesgo de incendio o explosión (ITC-BT-29).
- Cuatro modos de carga: 1 (toma normalizada hasta 16 A), 2 (hasta 32 A con control piloto y protección diferencial en el cable), 3 (conexión directa mediante SAVE conectado permanentemente) y 4 (SAVE con convertidor alterna-continua, hasta 1000 V c.a. trifásica o 1500 V c.c.).
- Solo dos tipos de estación de recarga: punto de recarga simple (protecciones, bases no específicas y envolvente) y punto de recarga tipo SAVE (Sistema de alimentación específico del vehículo eléctrico).
- Cuatro familias de esquemas: 1 colectivo/troncal con contador principal (1a, 1b, 1c), 2 individual con contador común a vivienda y estación, 3 individual con contador por estación (3a, 3b), y 4 con circuitos adicionales (4a, 4b); la selección prioriza los módulos de reserva de la centralización existente y su ampliación antes de crear centralizaciones nuevas.
- Viviendas unifamiliares nuevas con aparcamiento: circuito exclusivo C_13 (nomenclatura ITC-BT-25) siguiendo el esquema 4a; los C_13 monofásicos no superan 9.200 W para evitar desequilibrios.

Tabla 1. Potencias instaladas normalizadas en un circuito de recarga para una vivienda unifamiliar:

| U nominal | IA en origen | Potencia instalada | Estaciones por circuito |
|---|---|---|---|
| 230 V | 10 A | 2.300 W | 1 |
| 230 V | 16 A | 3.680 W | 1 |
| 230 V | 20 A | 4.600 W | 1 |
| 230 V | 32 A | 7.360 W | 1 |
| 230 V | 40 A | 9.200 W | 1 |
| 230/400 V | 16 A | 11.085 W | 1 a 3 |
| 230/400 V | 20 A | 13.856 W | 1 a 4 |
| 230/400 V | 32 A | 22.170 W | 1 a 6 |
| 230/400 V | 40 A | 27.713 W | 1 a 8 |

- Tabla 2 (circuitos de recarga colectivos trifásicos): 16 A → 11.085 W (3 estaciones), 32 A → 22.170 W (6), 50 A → 34.641 W (9), 63 A → 43.647 W (12); calculados con estaciones monofásicas de 3.680 W.
- Previsión de cargas: simultaneidad 0,3 entre recarga y resto del edificio si hay SPL (mide la intensidad de la LGA y reduce la potencia destinada a la recarga para evitar el fallo general), y 1,0 si no se instala; en esquemas 2, 3 y 4 el factor es 1,0.
- Protección: cada punto de conexión con diferencial de máxima 30 mA, clase A, en instalación fija o dentro del SAVE; el diferencial de origen del circuito colectivo será selectivo o retardado; en vía pública se prepara para rearme automático y en aparcamientos públicos o estaciones de movilidad eléctrica lleva aviso de desconexión o rearme automático.
- Punto de conexión junto a la plaza, a ≥60 cm del suelo (máximo 120 cm si es de uso público); en plazas accesibles, entre 80 y 120 cm, con contraste cromático y ≥35 cm respecto de encuentros en rincón.

## Detalles

**Ámbito y definiciones.** La instrucción aplica a aparcamientos de viviendas unifamiliares, aparcamientos colectivos en régimen de propiedad horizontal, flotas privadas o de empresa, estacionamientos públicos y vías de dominio público. Nexos de la instalación: el circuito de recarga individual parte de la centralización de contadores (o del cuadro de vivienda como circuito C_13) y alimenta una estación; el colectivo parte de una centralización o cuadro y alimenta dos o más estaciones. La infraestructura (IVEHÍCULO ELÉCTRICO) incluye estaciones, sistema de control, canalizaciones, cuadros y equipos de medida exclusivos. La estación de movilidad eléctrica tiene al menos dos estaciones de recarga simultáneas para vehículos de categoría M1/N1 (Directiva 2007/46/CE). El contador principal es punto frontera (reglamento unificado de puntos de medida); el contador secundario permite repercutir costes y gestionar consumos sin estar sujeto a ese reglamento. Las conexiones estación-vehículo se realizan según los casos A, B y C.

**Esquemas de instalación.** Toda instalación nueva o modificación exige memoria técnica de diseño o proyecto (ITC-BT-04) que indique el esquema. En el esquema 2 se justificará que el fusible de la centralización protege contra cortocircuitos a derivación y circuito de recarga, sobre todo para la intensidad mínima de cortocircuito; el control de potencia contratada lo hace el contador principal sin ICP independiente y el rearme se hace desde la vivienda. En 1a/1b y 3a/3b la prioridad es: módulos de reserva existentes → ampliación de la centralización → centralizaciones nuevas por falta de espacio. Los esquemas no aplican a estaciones alimentadas por redes independientes (c.c., c.a. ferroviaria o renovables con almacenamiento), donde el diseñador especifica el esquema. Las figuras son solo ilustrativas.

**Colectivos y preinstalación.** En un mismo edificio pueden convivir esquemas distintos si se cumplen todos los requisitos. En el 4a el circuito sigue las condiciones de la ITC-BT-15 con los mismos cables que una derivación individual; el 4b se usa cuando la recarga forma parte o ampliación de los servicios generales del garaje. La preinstalación preverá sistemas de conducción desde la centralización por las vías principales (hasta cada plaza si es del 100 % de plazas, o hasta las plazas definidas en caso contrario) y centralización según ITC-BT-16 con módulos de reserva para al menos el 20 % de las plazas no asociadas a vivienda y, como mínimo, un módulo aunque todas lo estén. Otras instalaciones (3.3) siguen los esquemas 1a, 1b, 1c, 3 o 4b. Las estaciones de autoservicio (usuarios no adiestrados) admiten cualquier modo; las de uso asistido (flotas, talleres, concesionarios) dispondrán preferentemente de los modos 3 o 4, pudiendo usar modos 1 o 2 para vehículos de baja potencia (bicicletas, ciclomotores y cuadriciclos).

**Previsión de cargas.** Con SPL: Pendificio = (P1 + P2 + P3 + P4) + 0,3·P5; sin él, + P5, donde P1 son viviendas (con el coeficiente de la tabla 1 de la ITC-BT-10), P2 servicios generales, P3 locales comerciales y oficinas, P4 garajes distintos de la recarga y P5 la recarga prevista. En edificios existentes se calculará el número máximo de estaciones alimentables según la potencia disponible en la LGA. Por circuito colectivo, la simultaneidad entre estaciones es 1, aunque puede reducirse si un sistema mide la intensidad del circuito y la reduce para evitar sobrecargas.

**Requisitos generales.** Alimentación 230/400 V c.a. para modos 1, 2 y 3 (con conversión si existe 127/220 V); esquemas TN solo en forma TN-S. Canalizaciones según el tipo de local; los cables fijos desde el SAVE al punto de conexión serán de 450/750 V, cobre clase 5 o 6 y resistentes a condiciones mecánicas, ambientales y de seguridad; al exterior, 0,6/1 kV. Iluminancia mínima de 20 lx en exterior y 50 lx en interior en la zona de recarga. Caída de tensión máxima del 5 %; sección mínima de 2,5 mm² de cobre (4 mm² si es aluminio, solo fuera de viviendas y aparcamientos colectivos, con técnicas apropiadas contra pares galvánicos). Con más de 5 estaciones se estudiarán filtros de corrección de armónicos. El circuito es dedicado, y las bases instaladas evitan prolongadores y adaptadores: para >3,7 kW y ≤22 kW, al menos bases o conectores tipo 2; >22 kW, conectores tipo 2; en modo 4, conectores combo 2 (EN 62196-3). Con potencia ≤3,7 kW monofásica en viviendas unifamiliares o propiedad horizontal valen las opciones de la tabla 3 (bases UNE 20315-1-2 Fig. C2a o UNE 20315-2-11 Fig. C7a con IA de 10 A en modos 1/2, u opciones tipo 2 del sistema EN 62196-2 en modo 3, con restricción de 63 A solo a otras instalaciones). En modos 3 y 4 las bases deben incorporarse en un SAVE o sistema equivalente. Está previsto adaptar el apartado a futuras directivas y reglamentos europeos.

**Contadores secundarios.** Clase A o superior y con medida de energía activa. Son obligatorios en esquemas 1a, 1b, 1c y 4b si hay transacción comercial según la medida, en plazas en propiedad horizontal, estaciones de movilidad eléctrica y vía pública; en edificios comerciales, de oficinas o industrias, cuando haya que identificar consumos individuales; opcionales para el titular en esquemas 2 y 4a.

**Protecciones.** Solo se admiten de la ITC-BT-24: contra contacto directo los apartados 3.1 (aislamiento) y 3.2 (barreras o envolventes), e indirecto los 4.1 (corte automático), 4.2 (clase II) y 4.5 (separación eléctrica); siempre con conductor de protección y toma de tierra. Sobreintensidades (ITC-BT-22): dispositivos omnipolares curva C; en tomas UNE 20315, IA de 10 A como máximo (16 A solo si el fabricante garantiza la protección de la base con recargas diarias de 8 horas a 16 A); en modo 3 la selección del IA evita el disparo intempestivo y puede superar la suma de intensidades de los puntos de conexión por tolerancia de señal, consumo interno y condiciones ambientales. Sobretensiones: contra temporales hasta 440 V fase-neutro; contra transitorias junto al origen, con dispositivo adicional junto a la estación si hay distancia (coordinados entre sí) y protección aguas arriba recomendada por el fabricante si no incorpora la propia. Influencias externas: canalizaciones exteriores IP4X o IPXXD e IPX4 si hay agua; estaciones y cuadros IP4X o IPXXD en interior, IP5X e IPX4 en exterior; impactos: envolventes IK08 mínimo, cuerpos de estaciones exteriores IK10 (excluye teclado, leds, pantallas y rejillas), tubos grado 4 de impacto y 5 de compresión, canales protectoras IK08 o cables armados. Estos grados no aplican durante el proceso de recarga, y la corrosión exterior remite a la ITC-BT-30.

**Red de tierra exterior (7.1).** Aplica a vía pública y aparcamientos a la intemperie: la instalación de puesta a tierra debe garantizar que nunca se produzcan tensiones de contacto mayores de 24 V en partes metálicas accesibles, y cada poste dispone de borne de tierra conectado al circuito general. Conductores entre electrodos: desnudos de cobre de 35 mm² mínimos por fuera de las canalizaciones, o aislados de 450/750 V verde-amarillo con 16 mm² de cobre; el conductor de protección de cada punto de recarga será unipolar aislado 450/750 V verde-amarillo de 16 mm², con conexiones mediante terminales, grapas, soldadura u otros elementos con contacto permanente y protegido contra corrosión.

**Historial normativo.** Los apartados 3.2 y 5.4 fueron modificados por el RD 1053/2014 (añadido con efectos de 30 de junio de 2015), en redacción dada por el RD 542/2020 y por la disposición final 1.2 y 3 del RD 450/2022.

## Relacionado

- [[reglament-electrotecnic-baixa-tensio]]
- [[instalaciones-interiores-viviendas-bt]]
- [[toma-de-tierra-edificios-viviendas]]
- [[itc-bt-04-documentacion-y-puesta-en-servicio-de-las-instalaciones]]
- [[itc-bt-10-prevision-de-cargas-para-suministros-en-baja-tension]]
- [[itc-bt-15-instalaciones-de-enlace-derivaciones-individuales]]
- [[itc-bt-16-instalaciones-de-enlace-contadores-ubicacion-y-sistemas-de-instalacion]]
- [[itc-bt-22-instalaciones-interiores-o-receptoras-proteccion-contra-sobreintensidades]]
- [[itc-bt-24-instalaciones-interiores-o-receptoras-proteccion-contra-los-contactos-directos-e-indirectos]]
- [[itc-bt-25-instalaciones-interiores-en-viviendas-numero-de-circuitos-y-caracteristicas]]
- [[itc-bt-29-prescripciones-particulares-para-las-instalaciones-electricas-de-los-locales-con-riesgo-de-ince]]
- [[itc-bt-30-instalaciones-en-locales-de-caracteristicas-especiales]]
- [[itc-bt-52-instalaciones-con-fines-especiales-infraestructura-para-la-recarga-de-vehiculos-electricos]]
