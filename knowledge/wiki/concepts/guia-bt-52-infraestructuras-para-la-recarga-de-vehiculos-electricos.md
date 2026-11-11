---
title: Guía-BT-52 — Guía técnica de aplicación de la ITC-BT-52 sobre recarga de vehículos eléctricos
type: concept
tags: [rebt, guia-tecnica, baja-tension, itc-bt-52, recarga-vehiculo-electrico]
sources: [papers/2026-11-10-guia-bt-52-infraestructuras-para-la-recarga-de-vehiculos-electricos.md]
created: 2026-11-10
updated: 2026-11-10
---

# Guía-BT-52 — Guía técnica de aplicación de la ITC-BT-52 sobre recarga de vehículos eléctricos

Documento del Ministerio de Industria que desarrolla la aplicación práctica de la [[itc-bt-52-instalaciones-con-fines-especiales-infraestructura-para-la-recarga-de-vehiculos-electricos]], edición de septiembre de 2024 (rev. 2). Guía de carácter **no vinculante** (art. 29 del RD 842/2002 y disposición adicional segunda del RD 1053/2014): **no sustituye ni relaja el texto reglamentario, la ITC-BT-52 del BOE tiene autoridad**.

## Puntos clave

- Reproduce los apartados de la ITC-BT-52 y añade tres anexos: buenas prácticas en garajes existentes en propiedad horizontal, previsión de cargas en viviendas de nueva construcción con garajes en condominio y capacidad disponible de un consumidor doméstico para recargar sin ampliar potencia.
- Cuatro familias de esquemas: colectivo o troncal con contador principal en el origen (1a, 1b, 1c), individual con contador común a vivienda y estación (2), individual con contador por estación (3a, 3b) y con circuitos adicionales (4a, 4b). La selección prioriza los módulos de reserva de la centralización existente, después su ampliación y, en último lugar, centralizaciones nuevas por falta de espacio.
- Previsión de cargas: simultaneidad 0,3 entre la recarga y el resto del edificio con el sistema de protección de la línea general de alimentación (SPL) y 1,0 sin él; dentro de un circuito colectivo la simultaneidad entre estaciones es 1, salvo control que mida la intensidad del circuito.
- Potencias normalizadas de una vivienda unifamiliar (esquema 4a, circuito C13 de [[itc-bt-25-instalaciones-interiores-en-viviendas-numero-de-circuitos-y-caracteristicas]]), máximo 9.200 W en monofásico:

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

- Potencias normalizadas de los circuitos de recarga colectivos trifásicos, con estaciones monofásicas de 3.680 W:

| IA en origen | Potencia instalada | Estaciones por circuito |
|---|---|---|
| 16 A | 11.085 W | 3 |
| 32 A | 22.170 W | 6 |
| 50 A | 34.641 W | 9 |
| 63 A | 43.647 W | 12 |

- Ejecución: caída de tensión máxima del 5 %, cobre de 2,5 mm² mínimo (4 mm² si es aluminio, fuera de viviendas y aparcamientos colectivos de viviendas), 20 lx en exterior y 50 lx en interior, circuito dedicado y corrección de armónicos desde más de cinco estaciones.
- Punto de conexión fijo junto a la plaza, de 60 cm a 120 cm de altura en uso público; en plazas accesibles, entre 80 y 120 cm, con contraste cromático y 35 cm como distancia mínima a encuentros en rincón.
- Protecciones: diferencial de 30 mA máximo por punto de conexión, selectivo o retardado en el origen del circuito colectivo; IP4X o IPXXD en interior e IP5X e IPX4 en exterior; envolventes IK08 y cuerpos de estación exteriores IK10; tierra exterior con tensión de contacto máxima de 24 V.

## Detalles

**Alcance y definiciones.** Aplica la ITC-BT-52 a aparcamientos unifamiliares, colectivos en propiedad horizontal, flotas privadas o de empresa, talleres, aparcamientos públicos y vías de dominio público, y mantiene sus exclusiones: sin recarga por inducción ni con baterías que desprendan gases. Introduce la definición de «gestor de cargas» (art. 6 de la Ley 24/2013), los reglamentos de metrología de los contadores secundarios (RD 244/2016, ITC 3022/2007, ITC 3747) y la especificación UNE 0048 sobre el SPL.

**Esquemas y ejecución.** Sobre los cuatro esquemas la guía añade criterios de proyecto: cuatro vías de paso de los conductores del circuito 4a en garajes existentes en propiedad horizontal (SCC de la derivación individual, tubo de reserva para DIs, canaladura de obra y SCC adicional compartido, este último con cable multiconductor de 0,6/1 kV); cajas de derivación en paramento vertical a más de 1,8 m, con 3 o 6 derivaciones, cierre y ninguna plaza a más de 20 m de una caja; y revisión de la instalación existente según UNE 202008 IN y UNE 202009 IN cuando se modifica la vivienda o el garaje. En garajes existentes con ventilación forzada o natural y más de cinco plazas exige revisar el proyecto original y, si no puede comprobarse la desclasificación, ejecutar un proyecto de desclasificación según la ITC-BT-29.

**Vivienda y preinstalación.** En viviendas unifamiliares nuevas el C13 debe quedar totalmente instalado, con CPM que incorpore protector de sobretensiones transitorias antes del contador y espacio para filtro PLC después. En aparcamientos colectivos la preinstalación debe facilitar cualquier esquema posterior: sistemas de conducción desde la centralización por las vías principales, hasta cada plaza si es del 100 % o hasta las plazas definidas en caso contrario, y centralización con módulos de reserva para el 20 % de las plazas no asociadas a vivienda y al menos un módulo en todo caso. Las dotaciones mínimas y los porcentajes se remiten a la sección HE6 del DB HE del Código Técnico de la Edificación.

**Previsión de cargas.** La guía parte de la fórmula del REBT (P1 viviendas, P2 servicios generales, P3 locales y oficinas, P4 garajes distintos de la recarga, P5 recarga) con los factores 0,3 y 1,0, y añade mínimos de P5: 0,1 × plazas × 3,68 kW en propiedad horizontal y (plazas / 40) × 3,68 kW en edificios no residenciales. El anexo 2 desarrolla el procedimiento para promociones con preinstalación en más del 50 % de las plazas, con los casos 1a/1b/1c/4b, 2/4a y 3a/3b, el valor Y = parte entera de 0,3 × N a partir del cual debe instalarse el SPL y la memoria técnica de diseño por cada punto añadido salvo previsión superior a 50 kW (10 kW en exteriores, ITC-BT-04). El anexo 3 estima que un consumidor doméstico dispone de cerca del 50 % de su punta a la 1:00 h según los perfiles de REE, y de ahí el coeficiente 0,5 de la previsión nocturna de viviendas.

**Ejecución y protecciones.** La tabla 3 detalla los puntos de conexión admisibles (UNE 20315-1-2 Fig. C2a, UNE 20315-2-11 Fig. C7a, UNE-EN 62196-2 tipo 2) por modo de carga, intensidad y ubicación, y distingue el modo 4 con Combo 2. Las canalizaciones exigen 450/750 V con cobre clase 5 o 6 entre el SAVE y el punto de conexión y 0,6/1 kV en exterior; en protección, IP4X o IPXXD, IP5X, IPX4, IK08, IK10, tubos con grado 4 al impacto y 5 a la compresión y canales con IK08. La red de tierra exterior fija 24 V de tensión de contacto máxima, borne por poste, cobre desnudo de 35 mm² o aislado de 16 mm² en verde-amarillo. Destaca además el ruido PLC: reservar espacio junto al contador principal, en la CPM o en la centralización, para que la distribuidora instale filtros que no perturben la telegestión del resto de contadores.

## Divergencias con la ITC-BT-52

- **Vivienda unifamiliar (guía 3.1).** La guía exige C13 totalmente instalado en toda vivienda unifamiliar nueva y una CPM con protector de sobretensiones transitorias antes del contador y hueco para filtro PLC después; la ITC-BT-52 (3.1) solo exige circuito exclusivo C13 con esquema 4a y las potencias de la tabla 1. Prevalece la ITC-BT-52.
- **Cableado en garajes existentes (guía 3.2).** La guía admite cuatro vías de paso de conductores (SCC de la derivación individual, tubo de reserva, canaladura de obra o SCC adicional con cable de 0,6/1 kV) y la revisión UNE 202008 IN / UNE 202009 IN; la ITC-BT-52 (3.2) solo remite a la ITC-BT-15 y al apartado 5. Prevalece la ITC-BT-52.
- **Reserva para PLC y gestión de cargas (guía 3 y 5).** La guía incorpora espacio para filtros PLC y contactores de gestión desde el SPL en la selección de esquemas y en el diseño de centralizaciones; la ITC-BT-52 no contempla esa reserva. Prevalece la ITC-BT-52.
- **Caja de derivación de la LGA y contador del 4b (guía 5).** La guía exige situar la caja de derivación de la LGA en cuarto o armario de contadores o zona común, cerrada y con cierre, y ubicar el contador principal del 4b en la centralización; la ITC-BT-52 (5) solo regula la ubicación de contadores en los esquemas 1a, 1b, 1c, 2, 3a y 3b. Prevalece la ITC-BT-52.
- **Desclasificación del garaje (guía 5).** La guía obliga a revisar el proyecto original del garaje con ventilación forzada o natural y más de cinco plazas y, si no puede comprobarse la desclasificación, a redactar un proyecto de desclasificación según la ITC-BT-29; la ITC-BT-52 solo prohibe recargar en locales con riesgo de incendio o explosión. Prevalece la ITC-BT-52.
- **Dotaciones mínimas según el CTE (guía 3.2).** La guía remite las dotaciones mínimas de infraestructura y los porcentajes de preinstalación a la sección HE6 del DB HE; la ITC-BT-52 (3.2) fija los módulos de reserva del 20 % pero no remite al DB HE. Prevalece la ITC-BT-52.
- **Tabla 3, notas (5) y (6).** La guía admite bases UNE 20315 en «otras instalaciones» si existe al menos un punto Tipo 2 (columna «no (6)») y cualquier conector normalizado si un punto es Tipo 2 (nota 5); la ITC-BT-52 mantiene «No» en esas ubicaciones y solo incluye las notas (1) a (4). Prevalece la ITC-BT-52.
- **Tabla 3, nota (3).** La guía extiende la excepción de plazas de baja potencia a cualquier vehículo de categoría L (ciclomotores, motocicletas, quads) y limita la base normalizada a 3,7 kW; la ITC-BT-52 solo menciona bicicletas, ciclomotores y cuadriciclos, sin límite de potencia. Prevalece la ITC-BT-52.
- **Modo de carga 4 (guía 5.4).** La guía permite cualquier conector normalizado si al menos un punto es Combo 2 en configuración FF; la ITC-BT-52 exige conectores tipo combo 2 conforme a EN 62196-3, sin esa ampliación. Prevalece la ITC-BT-52.
- **Conectores TESLA (guía 5.4).** La guía reproduce la autorización de conectores TESLA como único conector en estaciones de más de 100 kW (Orden IET/2388/2015), con vigencia «temporal hasta el 18 de noviembre de 2017»; el texto consolidado de la ITC-BT-52 en el BOE no recoge ese párrafo. Prevalece la ITC-BT-52.
- **Altura mínima de estación o caja (guía 5.4).** La guía recomienda 1,5 m de altura mínima para estaciones y cajas con bases, y 1,0 m en plazas de movilidad reducida; la ITC-BT-52 solo fija 60 cm mínimos, 120 cm máximos en uso público y 80 a 120 cm en plazas accesibles. Prevalece la ITC-BT-52.
- **Diferenciales con componente continua (guía 6.1).** La guía admite diferenciales de tipo B o de tipo A con RDC-DD conforme a IEC 62955 (UNE-HD 60364-7-722) y cita EN 61008-1, EN 61009-1, EN 60947-2 y EN 62423; la ITC-BT-52 (6.1) exige clase A con 30 mA máximos por punto, sin excepción por componente continua. Prevalece la ITC-BT-52.
- **Obturadores en bases tipo 2 (guía 6.2.1).** La guía declara que el grado de la estación no se extiende a la base o conector tipo 2 si hay elemento de corte y que por ello no hacen falta obturadores, aunque los recomienda para personal no adiestrado; la ITC-BT-52 (6.2.1) solo dice que el grado no aplica durante la recarga. Prevalece la ITC-BT-52.
- **Resistencia mecánica reforzada (guía 6.2.3.2).** La guía añade que, ante riesgo importante de choque de vehículos contra la canalización, los tubos deben resistir grado 5 al impacto (UNE-EN 61386) y los canales 20 J (UNE-EN 50085); la ITC-BT-52 fija grado 4 al impacto y 5 a la compresión en tubos e IK08 en canales. Prevalece la ITC-BT-52.
- **Sobretensiones (guía 6.4).** La guía exige UNE-EN 50550 para sobretensiones temporales con 440 V fase-neutro, recomienda un protector tipo 1 aguas arriba del contador o junto al IGM y, por UNE-CLC/TS 61643-12, un tipo 2 junto a la estación si la distancia alcanza los 10 m; la ITC-BT-52 (6.4) solo fija la protección temporal hasta 440 V y el transitorio cerca del origen. Prevalece la ITC-BT-52.
- **Mínimos de P5 y SPL en el 4b (guía 4.1 a 4.3 y anexo 2).** La guía fija P5 mínimo = 0,1 × plazas × 3,68 kW (regla de la ITC-BT-10) y P5 mínimo = (plazas / 40) × 3,68 kW (disposición adicional primera del RD 1053/2014), y sostiene en su anexo 2 que la ITC-BT-52 no regulaba el SPL en el esquema 4b aunque tampoco lo excluía, aplicándole el factor 0,3; la ITC-BT-52 no fija mínimos de P5 y para el esquema 4 establece un factor de 1,0. Prevalece la ITC-BT-52.
- **Contenidos que la guía añade (apartado 2 y anexos 1 a 3).** La guía incorpora el coeficiente 0,5 y la disponibilidad estimada del 50 % de la punta a la 1:00 h según REE, la definición de «gestor de cargas», los reglamentos de metrología de los contadores secundarios, la especificación UNE 0048 sobre el SPL y un caso de conexión D para vehículo eléctrico ligero; la ITC-BT-52 no contiene ninguno de estos contenidos. Prevalece la ITC-BT-52.

## Relacionado

- [[itc-bt-52-instalaciones-con-fines-especiales-infraestructura-para-la-recarga-de-vehiculos-electricos]]
- [[itc-bt-25-instalaciones-interiores-en-viviendas-numero-de-circuitos-y-caracteristicas]] (circuito C13)
- [[classificacio-p1-p2]]
- [[reglament-electrotecnic-baixa-tensio]]
- [[ITC-BT-YY]]
