---
title: ITC-BT-24 — Instalaciones interiores o receptoras. Protección contra los contactos directos e indirectos
type: concept
tags: [rebt, baja-tension, itc-bt-24, choques-electricos, proteccion]
sources: [papers/2026-11-10-rebt-itc-bt-24-instalaciones-interiores-o-receptoras-proteccion-contra-los-contactos-directos-e-indirectos.md]
created: 2026-11-10
updated: 2026-11-10
---

# ITC-BT-24 — Instalaciones interiores o receptoras. Protección contra los contactos directos e indirectos

Resume las medidas de la ITC-BT-24 (REBT, RD 842/2002) para proteger personas y animales domésticos contra los choques eléctricos: protección conjunta mediante MBTS, contra contactos directos (aislamiento, barreras, obstáculos, alejamiento y diferencial complementario) y contra contactos indirectos (corte automático por esquemas TN, TT e IT, clase II, locales no conductores, equipotencialidad local y separación eléctrica).

## Puntos clave
- Protección conjunta contra contactos directos e indirectos: MBTS con tensión en el campo I (UNE 20.481, ITC-BT-36), fuente de seguridad y circuitos según UNE 20.460-4-41 e ITC-BT-36.
- Contra contactos directos: aislamiento de las partes activas que solo pueda eliminarse destruyéndolo; pinturas, barnices y lacas no constituyen aislamiento suficiente.
- Barreras o envolventes con grado mínimo IP XXB; las superficies superiores horizontales fácilmente accesibles, IP4X o IP XXD. Solo pueden suprimirse con llave o herramienta, quitando antes la tensión, o con una segunda barrera interior IP2X/IP XXB.
- Obstáculos y puesta fuera de alcance por alejamiento: medidas incompletas, limitadas a locales de servicio eléctrico accesibles solo a personal autorizado; el volumen de accesibilidad está limitado a 2,5 m de altura.
- Diferencial residual ≤ 30 mA: medida complementaria en caso de fallo de otra protección o de imprudencia; jamás constituye protección completa por sí mismo. Debe ser de clase A cuando se prevean corrientes diferenciales no senoidales (p. ej. salas de radiología intervencionista).
- Corte automático de la alimentación: coordinación entre el esquema de conexión a tierra (ITC-BT-08) y los dispositivos de protección; tensión límite convencional 50 V (24 V para alumbrado público según ITC-BT-09, apartado 10).
- Esquema TN: condición Z_s × I_a ≤ U_0; permitidos dispositivos de máxima corriente y diferenciales; en TN-C no se admite diferencial y en TN-C-S no puede haber conductor CPN aguas abajo del diferencial.

| U_0 (V) | Tiempo máximo de interrupción (s) |
|---|---|
| 230 | 0,4 |
| 400 | 0,2 |
| > 400 | 0,1 |

- Esquema TT: masas protegidas por un mismo dispositivo interconectadas a una misma toma de tierra; condición R_A × I_a ≤ U (50, 24 V u otros). Se prefieren diferenciales; los de máxima corriente solo si R_A es muy baja. La selectividad se logra con diferenciales temporizados tipo «S» en serie, con tiempo máximo de funcionamiento de 1 s.
- Esquema IT: instalación aislada de tierra o unida por impedancia; el primer defecto no exige corte pero debe activar una señal acústica o visual; condición R_A × I_d ≤ U_L. En un segundo defecto se aplican las condiciones del TT (masas por grupos) o del TN (masas interconectadas).

| Tensión nominal U_0/U (V) | Neutro no distribuido (s) | Neutro distribuido (s) |
|---|---|---|
| 230/400 | 0,4 | 0,8 |
| 400/690 | 0,2 | 0,4 |
| 580/1000 | 0,1 | 0,2 |

## Detalles
En el esquema TN, con puestas a tierra múltiples repartidas y recomendación de conectar el conductor de protección a tierra en la entrada de cada edificio, la condición Z_s × I_a ≤ U_0 define el corte dentro de los tiempos de la tabla 1 (I_a es la corriente de funcionamiento del dispositivo o la diferencial asignada si es diferencial). Con diferencial en TN-C-S, la unión del conductor de protección al CPN debe estar aguas arriba del dispositivo.

En el esquema IT, cuando las masas están interconectadas colectivamente a tierra, deben cumplirse 2 × Z_s × I_a ≤ U si el neutro no está distribuido o 2 × Z_s' × I_a ≤ U_0 si lo está; si no es posible con dispositivos de máxima corriente, se usan diferenciales por aparato o conexión equipotencial complementaria.

La protección por equipos de clase II admite aislamiento doble o reforzado, aparamenta con aislamiento equivalente y aislamientos suplementarios o reforzados montados en la instalación. En locales o emplazamientos no conductores se admite material de clase 0: sin conductor de protección previsto, distancias mínimas de 2 m (1,25 m fuera del volumen de accesibilidad), obstáculos aislantes no conectados a tierra, o aislamiento de elementos conductores con ensayo mínimo de 2.000 V y corriente de fuga ≤ 1 mA; paredes y suelos con resistencia ≥ 50 kΩ (≤ 500 V) o ≥ 100 kΩ (> 500 V), evitando humedad y elementos añadidos que anulen la conformidad.

La conexión equipotencial local no conectada a tierra debe unir todas las masas y elementos conductores simultáneamente accesibles, sin conexión a tierra directa ni a través de otras masas. La separación eléctrica exige fuente de separación (transformador de aislamiento o equivalente); con un solo aparato las masas no se conectan a conductor de protección; con varios, equipotencialidad aislada no a tierra, bases con contacto de tierra conectado a ella, conductor de protección en cables flexibles de equipos no clase II usado como equipotencialidad, y dispositivo que corte ante dos fallos francos en el tiempo de la tabla 1.

## Relacionado
- [[instalaciones-interiores-viviendas-bt]]
- [[itc-bt-08-sistemas-de-conexion-del-neutro-y-de-las-masas-en-redes-de-distribucion-de-energia-electrica]]
- [[itc-bt-09-instalaciones-de-alumbrado-exterior]]
- [[itc-bt-36-instalaciones-a-muy-baja-tension]]
