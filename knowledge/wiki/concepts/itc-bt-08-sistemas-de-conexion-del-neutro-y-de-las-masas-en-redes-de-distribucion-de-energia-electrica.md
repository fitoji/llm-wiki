---
title: ITC-BT-08 — Sistemas de Conexión del Neutro y de las Masas en Redes de Distribución de Energía Eléctrica
type: concept
tags: [rebt, baja-tension, itc-bt-08, esquemas-distribucion, puesta-a-tierra]
sources: [papers/2026-11-10-rebt-itc-bt-08-sistemas-de-conexion-del-neutro-y-de-las-masas-en-redes-de-distribucion-de-energia-electrica.md]
created: 2026-11-10
updated: 2026-11-10
---

# ITC-BT-08 — Sistemas de Conexión del Neutro y de las Masas en Redes de Distribución de Energía Eléctrica

Define los esquemas de distribución TN, TT e IT según las conexiones a tierra de la alimentación y de las masas, y las prescripciones para aplicar el esquema TN.

## Puntos clave

- El esquema se determina por las conexiones a tierra de la red de alimentación y de las masas de la instalación receptora.
- Primera letra (alimentación): T = conexión directa de un punto a tierra; I = aislamiento de las partes activas o conexión a través de una impedancia.
- Segunda letra (masas): T = masas conectadas directamente a tierra; N = masas conectadas al punto de la alimentación puesto a tierra.
- Letra adicional: S = neutro y protección con conductores separados; C = combinados en un solo conductor (CPN).
- En redes TN un defecto franco fase-masa es un cortocircuito, con bucle de defecto de solo elementos conductores metálicos.
- En TT el defecto fase-masa puede ser inferior a la corriente de cortocircuito aunque suficiente para producir tensiones peligrosas; el bucle incluye la resistencia de paso a tierra.
- En IT el primer defecto fase-masa es de valor reducido, sin tensiones de contacto peligrosas; se recomienda no distribuir el neutro.
- La red pública de baja tensión tiene el neutro puesto a tierra por prescripción reglamentaria: el esquema para receptores alimentados directamente es TT.
- Para el esquema TN: resistencia de tierra del neutro ≤ 5 Ω junto a la central o centro de transformación y en los 200 últimos metros de toda derivación; resistencia global de todas sus tomas de tierra ≤ 2 Ω.

## Detalles

**Variantes de TN.** TN-S, con neutro y conductor de protección distintos en todo el esquema; TN-C, combinados en un solo conductor en todo el esquema; y TN-C-S, combinados solo en una parte del esquema.

**Esquema TT.** Las masas quedan conectadas a una toma de tierra separada de la de la alimentación. Aunque existan conexiones, voluntarias o no, entre ambas zonas de tierra, el esquema sigue siendo TT si no se cumplen todas las condiciones del TN: no se tienen en cuenta esas conexiones para determinar la protección.

**Esquema IT.** Ningún punto de la alimentación está conectado directamente a tierra y las masas van puestas a tierra. La intensidad del primer defecto se limita por la ausencia de conexión a tierra o insertando una impedancia entre la alimentación y tierra; puede ser preciso limitar la extensión de la instalación para reducir el efecto capacitivo de los cables.

**Elección del esquema.** Por las características técnicas y económicas de cada instalación, con estos principios: alimentados directamente de red pública, el esquema es TT; desde un centro de transformación de abonado, puede elegirse cualquiera de los tres; y puede establecerse un IT parcial en una instalación de red pública mediante transformadores adecuados, aplicando en el secundario y la parte afectada las disposiciones del propio esquema IT.

**Prescripciones para aplicar TN.** La sección del neutro, en todo su recorrido, debe ser como mínimo la indicada según la sección de fase (con 50 mm² de fase, 50 mm² en redes aéreas y 25 mm² en subterráneas; con 240 mm², 120 mm² en ambas). Además: el neutro de las líneas aéreas se tiende con las mismas precauciones que los conductores de fase; los neutros de líneas principales y derivaciones se ponen a tierra también en sus extremos cuando su longitud supera los 200 m; y en el esquema TN-C las masas se conectan al conductor neutro mediante conductores de protección.

## Relacionado

- [[itc-bt-06-redes-aereas-para-distribucion-en-baja-tension]]
- [[itc-bt-07-redes-subterraneas-para-distribucion-en-baja-tension]]
- [[toma-de-tierra-edificios-viviendas]]
