---
title: Instalaciones generadoras de baja tensión
type: concept
tags: [rebt, baja-tension, itc-bt-40, generacion, autoconsumo, red-distribucion]
sources: [papers/2026-11-10-rebt-itc-bt-40-instalaciones-generadoras-de-baja-tension.md]
created: 2026-11-10
updated: 2026-11-10
---

# Instalaciones generadoras de baja tensión

La ITC-BT-40 del REBT se aplica a las instalaciones generadoras, entendidas como las destinadas a transformar cualquier tipo de energía no eléctrica en energía eléctrica. Clasifica las instalaciones según su funcionamiento respecto a la Red de Distribución Pública y fija las condiciones de conexión, cables, forma de onda, protecciones, puesta a tierra, puesta en marcha y los sistemas para evitar el vertido a la red (anexo I).

## Puntos clave

- **Clasificación**: aisladas (sin conexión eléctrica posible con la red), asistidas (conexión sin paralelo, con conmutación que impida el acoplamiento simultáneo) e interconectadas (trabajo normal en paralelo con la red).
- Las interconectadas para autoconsumo se adscriben a las modalidades con o sin excedentes de la Ley 24/2013 y del RD 244/2019.
- **Autoconsumo**: las instalaciones sin excedentes deben disponer de un sistema contra el vertido que cumpla el anexo I; no les aplican los apartados 4.3.1, 4.3.4 ni los requisitos de distribuidora del apartado 9.
- Conexión de producción próxima a consumo: cuadro con diferenciales **tipo A**, de **30 mA** si es accesible al público general o en zonas residenciales; en autoconsumo colectivo no cabe conectar la producción a la instalación interior de ningún consumidor asociado.
- Generadores con excedentes, y los sin excedentes de potencia superior a **800 VA**: circuito independiente y dedicado con diferencial tipo A (30 mA en viviendas). Generadores de viviendas sin circuito dedicado ni transformador de aislamiento: corriente de fuga a tierra **≤ 10 mA**.
- **Potencia máxima interconectada en BT**: 100 kVA en redes 3x400/230 V (y no más de la mitad de la capacidad de la salida del centro de transformación); 60 kVA en redes 3x220/127 V. Eólicos: no más del **5 %** de la potencia de cortocircuito en el punto de conexión.
- **Transferencia de carga sin corte** (asistidas): solo generadores > 100 kVA, conmutación en punto único junto a la medida, neutro del generador desconectado de tierra en la interconexión, protección contra envío de potencia a la red y equipo de sincronización; la interconexión no se mantiene más de **5 segundos**.
- **Sincronización de síncronos**: diferencias máximas de ±8 % de tensión, ±0,1 Hz de frecuencia y ±10º de fase.
- **Cables de conexión**: dimensionados para el 125 % de la máxima intensidad del generador y caída de tensión ≤ 1,5 %.
- **Factor de potencia**: asíncronos ≥ 0,86 a potencia nominal (con baterías de condensadores si hace falta); síncronos con capacidad de mantenerlo entre 0,8 y 1.
- **Protecciones mínimas** en circuitos de salida: sobreintensidad; mínima tensión (actúa < 0,5 s al llegar al 85 %); sobretensión (< 0,5 s al llegar al 110 %); máxima y mínima frecuencia (fuera de 49–51 Hz más de 5 períodos).
- **Puesta a tierra**: con red de neutro a tierra, esquema TT con tierras independientes del neutro de la red; en interconectadas se instala detección de la corriente por el neutro que desconecta si se supera el **50 %** de la intensidad nominal. En eólicos, la tierra de la torre es independiente.
- **Anexo I** (anti-vertido): dos principios (corte o limitación de corriente frente a regulación del balance generación-consumo); incumplimientos corregidos en **menos de 2 segundos**; la conformidad se evalúa con documentación completa incluido informe de ensayos de un laboratorio acreditado UNE-EN ISO/IEC 17025.

## Detalles

Los generadores y sus instalaciones complementarias (depósitos de combustible, canalizaciones de líquidos o gases) obedecen además a sus reglamentos específicos; los locales de las instalaciones alojadas en edificios o industrias son de uso exclusivo y cumplen la protección contra incendios, con ventilación suficiente en los locales con motores térmicos y conductos de evacuación de gases de combustión incombustibles hacia el exterior. La forma de la onda generada debe ser prácticamente senoidal con una tasa máxima de armónicos en cualquier condición de funcionamiento:

| Armónicos | Tasa máxima |
|---|---|
| De orden par | 4/n |
| De orden 3 | 5 |
| De orden impar (≥ 5) | 25/n |

La tasa se define como la relación, en %, entre el valor eficaz del armónico de orden n y el del fundamental. Para generadores asíncronos, la caída de tensión en la conexión no supera el 3 % de la tensión asignada (en eólicos, conexiones como máximo 3 por minuto y caída del 2 % durante 1 segundo); la conexión no se realiza hasta alcanzar entre el 90 y el 100 % de la velocidad de sincronismo.

El anexo I distingue instalaciones con medida de intercambio de energía con la red y con medida de consumo: en el primer caso la potencia en el punto de conexión a red debe mantenerse con saldo consumidor siempre que exista un consumo interno superior al valor de tolerancia del sistema de medida (suma de clases de exactitud del equipo de medida y de los transformadores o sondas); en el segundo, la potencia medida en el punto de consumo debe superar siempre a la generada por encima de la misma tolerancia. Los ensayos comprenden tolerancia en régimen permanente, respuesta ante desconexiones de carga y ante incrementos de potencia de generación (reajuste en menos de 2 segundos), actuación ante pérdida de comunicaciones (parada en menos de 2 segundos) y determinación del número máximo de generadores a partir de los tiempos de respuesta con uno y dos generadores.

## Relacionado

- [[reglament-electrotecnic-baixa-tensio]]
- [[itc-bt-08-sistemas-de-conexion-del-neutro-y-de-las-masas-en-redes-de-distribucion-de-energia-electrica]]
- [[itc-bt-04-documentacion-y-puesta-en-servicio-de-las-instalaciones]]
