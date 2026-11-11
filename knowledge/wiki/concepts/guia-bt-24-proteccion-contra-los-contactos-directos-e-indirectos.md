---
title: Guía-BT-24 — Protección contra los contactos directos e indirectos
type: concept
tags: [rebt, guia-tecnica, baja-tension, itc-bt-24, contactos-directos, seguridad-electrica]
sources: [papers/2026-11-10-guia-bt-24-proteccion-contra-los-contactos-directos-e-indirectos.md]
created: 2026-11-10
updated: 2026-11-10
---

# Guía-BT-24 — Protección contra los contactos directos e indirectos

La Guía-BT-24 (junio 2019, revisión 2) desarrolla con tablas y ejemplos las medidas de protección frente a los choques eléctricos exigidas por la ITC-BT-24. Acompaña a la [[itc-bt-24-instalaciones-interiores-o-receptoras-proteccion-contra-los-contactos-directos-e-indirectos]]: es orientativa y la ITC-BT-24 del BOE tiene la autoridad y prevalece ante cualquier discrepancia.

## Puntos clave

- Edición de 2019 motivada por la UNE-HD 60364-4-41, que sustituye a la UNE 20.460-4-41 citada en la ITC-BT-24: los contactos directos son «protección principal» y los indirectos «protección en caso de defecto».
- Contra contactos directos: aislamiento de partes activas, barreras o envolventes (mínimo IP XXB; IP4X o IP XXD en superficies horizontales accesibles), obstáculos, alejamiento (altura 2,5 m) y diferenciales de IΔn ≤ 30 mA como complemento.
- Contra contactos indirectos: corte automático de la alimentación (TN, TT, IT), equipos de clase II, locales no conductores, equipotencialidad local no conectada a tierra y separación eléctrica; tensión de contacto límite de 50 V, o 24 V en alumbrado exterior, locales húmedos e intemperie.
- Los diferenciales (UNE-EN 61008-1, 61009-1, 62423 y 60947-2) disparan entre 0,5 y 1 × IΔn, con IΔn ≤ 2 × Ifuga.

| Esquema | Condición | Tiempos máximos de desconexión |
|---|---|---|
| TN | Zs × Ia ≤ U0 | 0,4 / 0,2 / 0,1 s (230 / 400 / > 400 V) |
| TT | RA × Ia ≤ U | 0,2 / 0,07 / 0,04 s (Tabla A, solo en la guía) |
| IT | RA × Id ≤ UL | Tabla 2 según neutro distribuido |

## Detalles

En TN las masas se unen con conductor de protección a la toma de tierra; en TT se interconectan a una misma toma con el neutro a tierra; en IT la instalación va aislada o con impedancia suficiente y el primer defecto no obliga al corte, por lo que se exige un controlador permanente de aislamiento. En el segundo defecto rigen las condiciones de TT si las masas se aterrizan por grupos y las de TN si se interconectan con conductor de protección.

Los cuatro anexos, sin equivalente en el texto del BOE, recogen la selección de diferenciales y de protecciones contra sobreintensidades según la accesibilidad BA1 a BA5, el rearme automático UNE-EN 50557, los tipos AC, A, F y B y el análisis de los disparos intempestivos (fugas de hasta 3,5 mA por aparato, alta frecuencia del 5 % de la corriente nominal, fuga acumulada bajo el 30 % de IΔn).

El aislamiento doble o reforzado admite canalizaciones de la ITC-BT-20 e ITC-BT-21 con conductores de 300/500 V en tubos UNE-EN 61386. En locales no conductores se exigen 2 m entre elementos (1,25 m fuera del volumen de accesibilidad), ensayo de 2.000 V, fuga ≤ 1 mA y paredes de 50 kΩ o 100 kΩ.

## Divergencias con la ITC-BT-24

- Guía 1: la edición de 2019 remite a la UNE-HD 60364-4-41; la ITC-BT-24 del BOE sigue citando la UNE 20.460-4-41. Prevalece la ITC-BT-24.
- Guía 4.1: la UNE 20.572-1 está anulada y la sustituye la UNE-IEC/TS 60479-1; la ITC-BT-24 la cita como referencia. Prevalece la ITC-BT-24.
- Guía 2: la UNE-HD 60364-4-41 fija la muy baja tensión en continua en 120 V, frente a los 75 V del REBT ([[itc-bt-36-instalaciones-a-muy-baja-tension]]). Prevalece la ITC-BT-24.
- Guía 4.1.1: la Tabla 1 se aplica solo a circuitos finales de hasta 63 A con tomas o 32 A con receptores fijos, admitiendo 5 s en distribución; la ITC la exige en general. Prevalece la ITC-BT-24.
- Guía 4.1.2: añade la Tabla A de desconexión en TT (0,2 / 0,07 / 0,04 s) y el límite de 1 s en distribución, ausentes del BOE. Prevalece la ITC-BT-24.
- Guía 4.1.3: desde 2010 los tiempos del IT con masas interconectadas son los de la Tabla 1 de TN; la ITC-BT-24 mantiene la Tabla 2 con neutro distribuido. Prevalece la ITC-BT-24.
- Guía 4.3 a 4.5: limita el emplazamiento no conductor, la equipotencialidad local y la separación eléctrica a instalaciones supervisadas por personas cualificadas o advertidas, condición que la ITC-BT-24 no impone. Prevalece la ITC-BT-24.

## Relacionado

- [[itc-bt-24-instalaciones-interiores-o-receptoras-proteccion-contra-los-contactos-directos-e-indirectos]]
- [[instalaciones-interiores-viviendas-bt]]
- [[reglament-electrotecnic-baixa-tensio]]
- [[itc-bt-08-sistemas-de-conexion-del-neutro-y-de-las-masas-en-redes-de-distribucion-de-energia-electrica]]
- [[itc-bt-36-instalaciones-a-muy-baja-tension]]
- [[itc-bt-25-instalaciones-interiores-en-viviendas-numero-de-circuitos-y-caracteristicas]]
