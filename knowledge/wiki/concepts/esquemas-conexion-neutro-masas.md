---
title: Esquemas de conexión del neutro y de las masas (TT, TN, IT)
type: concept
tags: [rebt, baja-tension, esquemas, neutro, masas, tt, tn, it, itc-bt-08, itc-bt-24]
sources: [papers/2026-11-10-rebt-itc-bt-08-sistemas-de-conexion-del-neutro-y-de-las-masas-en-redes-de-distribucion-de-energia-electrica.md, papers/2026-11-10-guia-bt-08-sistema-de-conexion-del-neutro-y-de-las-masas-en-redes-de-distribucion-de-energi.md, papers/2026-11-10-rebt-itc-bt-24-instalaciones-interiores-o-receptoras-proteccion-contra-los-contactos-directos-e-indirectos.md, papers/2026-11-10-rebt-itc-bt-18-instalaciones-de-puesta-a-tierra.md]
created: 2026-11-14
updated: 2026-11-14
---

# Esquemas de conexión del neutro y de las masas (TT, TN, IT)

El esquema de conexión a tierra describe cómo se conectan a tierra la alimentación y las masas de la instalación receptora, y condiciona las protecciones contra contactos indirectos y sobreintensidades. Este artículo integra la nomenclatura y los tres esquemas de la ITC-BT-08 con las condiciones de protección que la ITC-BT-24 exige para cada uno.

## Puntos clave

- La designación usa **dos letras y una adicional**: la primera describe la alimentación respecto a tierra (T = conexión directa; I = aislamiento o conexión por impedancia), la segunda las masas (T = a tierra; N = al punto de la alimentación puesto a tierra) y la adicional el neutro y la protección (S = conductores separados; C = un solo conductor CPN).
- **TT**: alimentación y masas puestas a tierra de forma independiente. La red pública de baja tensión usa este esquema, así que un receptor alimentado directamente de ella es TT.
- **TN**: las masas se conectan al neutro de la alimentación. Todo defecto franco fase-masa es un cortocircuito con bucle exclusivamente metálico. Variantes TN-S, TN-C y TN-C-S según dónde se combinen neutro y protección.
- **IT**: alimentación aislada de tierra o unida por impedancia. El primer defecto fase-masa no debe generar tensiones peligrosas y se recomienda no distribuir el neutro.
- La condición de protección cambia con el esquema: en TN es Z_s × I_a ≤ U_0; en TT es R_A × I_a ≤ U; en IT el primer defecto solo exige señalización y el segundo se resuelve como TT o TN (ITC-BT-24).
- En TN la resistencia de tierra del neutro no supera **5 Ω** junto a la central o centro de transformación y en los 200 últimos metros de cada derivación, y la resistencia global de todas sus tomas no supera **2 Ω** (ITC-BT-08).

## Detalles

### Las letras

La primera letra se refiere a la alimentación: **T** cuando un punto está conectado directamente a tierra, **I** cuando las partes activas están aisladas de tierra o conectadas a través de una impedancia. La segunda se refiere a las masas de la instalación receptora: **T** cuando están conectadas directamente a tierra, **N** cuando se conectan al punto de la alimentación puesto a tierra, normalmente el neutro. La letra adicional distingue **S** (neutro y protección con conductores separados) de **C** (combinados en un solo conductor CPN).

### Los tres esquemas

**TT.** Alimentación y masas tienen tomas de tierra independientes. El defecto fase-masa puede ser inferior a la corriente de cortocircuito y, aun así, suficiente para producir tensiones peligrosas, porque el bucle incluye la resistencia de paso a tierra. El esquema sigue siendo TT aunque las tomas no sean independientes.

**TN.** Las masas se conectan al neutro de la alimentación. En TN-S el neutro y el conductor de protección son distintos en todo el esquema; en TN-C están combinados en todo el esquema; en TN-C-S solo en una parte. En TN-C no se admite diferencial y en TN-C-S no puede haber conductor CPN aguas abajo del diferencial (ITC-BT-24).

**IT.** La alimentación está aislada de tierra o unida por una impedancia. El primer defecto fase-masa es de valor reducido y no genera tensiones de contacto peligrosas, pero debe activar una señal acústica o visual; se recomienda no distribuir el neutro. En un segundo defecto se aplican las condiciones del TT (masas por grupos) o del TN (masas interconectadas).

### Condiciones de protección

La ITC-BT-24 fija la condición de corte automático para cada esquema:

- **TN:** Z_s × I_a ≤ U_0, donde Z_s es la impedancia del bucle de defecto e I_a la corriente que asegura el funcionamiento del dispositivo. Se admiten dispositivos de máxima corriente y diferenciales. Los tiempos máximos de interrupción son 0,4 s para 230 V, 0,2 s para 400 V y 0,1 s por encima de 400 V.
- **TT:** R_A × I_a ≤ U, con U de 50 V (24 V en alumbrado público) y las masas protegidas por un mismo dispositivo interconectadas a una misma toma de tierra. Se prefieren los diferenciales; los de máxima corriente solo si R_A es muy baja. La selectividad se logra con diferenciales temporizados tipo S de 1 s como máximo.
- **IT:** el primer defecto no exige corte pero debe señalizarse; la condición es R_A × I_d ≤ U_L. En el segundo defecto se aplican las condiciones del TT o del TN según cómo estén agrupadas las masas.

El desarrollo de la selectividad y del tipo de diferencial está en [[proteccion-diferencial-selectividad]].

### Resistencias de tierra del esquema TN

La ITC-BT-08 exige, para el esquema TN, una resistencia de tierra del neutro no superior a 5 Ω junto a la central o centro de transformación y en los 200 últimos metros de toda derivación, y una resistencia global de todas las tomas de tierra del neutro no superior a 2 Ω. La sección mínima del neutro se fija según la sección de las fases, con valores distintos para redes aéreas y subterráneas. Los criterios generales de electrodos y medición están en [[criterios-puesta-a-tierra]].

## Relacionado

- [[proteccion-diferencial-selectividad]] — diferenciales, selectividad y tiempos de desconexión
- [[criterios-puesta-a-tierra]] — electrodos, secciones y medición de la resistencia
- [[itc-bt-08-sistemas-de-conexion-del-neutro-y-de-las-masas-en-redes-de-distribucion-de-energia-electrica]] — texto consolidado de la instrucción
- [[guia-bt-08-sistema-de-conexion-del-neutro-y-de-las-masas-en-redes-de-distribucion-de-energi]] — criterio de la guía (sin divergencias)
- [[itc-bt-24-instalaciones-interiores-o-receptoras-proteccion-contra-los-contactos-directos-e-indirectos]] — condiciones de protección por esquema
- [[divergencias-guias-tecnicas-rebt-vs-itc-bt]] — mapa de las 223 divergencias y sus tipos
