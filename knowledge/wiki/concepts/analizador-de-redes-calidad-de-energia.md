---
title: Analizador de redes y calidad de energía
type: concept
tags: [calidad-de-energia, armonicos, analizador-de-redes, thd, en-50160]
sources: [articles/2026-11-16-analizador-de-redes-calidad-de-energia.md]
created: 2026-11-16
updated: 2026-11-16
---

# Analizador de redes y calidad de energía

El analizador de redes eléctricas (*power quality analyzer*) es el instrumento que audita **cómo** se consume la energía, frente al contador, que solo registra **cuánta** se consume. Muestrea miles de veces por segundo para reconstruir la onda y detectar armónicos, huecos y elevaciones de tensión, desequilibrios de fase, *flicker* y transitorios.

## Puntos clave

- La diferencia con un contador es de objetivo y de resolución: el contador factura (kWh, kVArh, picos de demanda cada 15 minutos); el analizador diagnostica (THD, transitorios, *flicker*, huecos) con muestreo de milisegundos o microsegundos.
- Se usa en tres bloques: diagnóstico de fallas, mantenimiento predictivo (THD en el neutro, sobrecalentamientos) y auditoría/eficiencia energética.
- **THD<sub>V</sub>** mide el efecto (tensión deformada); **THD<sub>I</sub>** mide la causa (corriente distorsionada que extraen las cargas no lineales).
- Los armónicos de orden triple (*triplens*: 3.º, 9.º, 15.º…) **no se anulan entre sí** y se suman en el neutro, pudiendo superar la corriente de fase y sobrecalentarlo.
- El **cos φ** (DPF) solo describe el desfase fundamental; con cargas no lineales hace falta el **factor de potencia total (TPF)**, que incorpora la distorsión.
- Hueco (*sag*): tensión RMS por debajo del **90 %** del nominal durante 0,5 ciclos a 1 minuto. Elevación (*swell*): por encima del **110 %**. Referencias: IEEE 1159 / EN 50160.
- Marco normativo: **EN 50160 / IEEE 1159** evalúan la tensión suministrada por la red; **IEC 61000-4-30** clasifica los equipos (Clase A / Clase S); **IEEE 519** limita los armónicos de corriente inyectados por el usuario.
- Conectar un analizador en un cuadro en tensión exige EPIs contra arco eléctrico, categoría de seguridad mínima **CAT III 600 V o CAT IV 300 V**, conectar primero tierra/neutro y después las fases, y orientar la flecha de cada pinza **de la fuente hacia la carga**.

## Detalles

### Qué mide y para qué sirve

El equipo toma canales de tensión (puntas de prueba) y de corriente (pinzas o sondas flexibles) y reconstruye matemáticamente la señal. Sus tres usos operativos:

1. **Diagnóstico y resolución de fallas**: disparos de automáticos sin sobrecarga aparente, vibración en motores inductivos, fallo prematuro de electrónica sensible.
2. **Mantenimiento predictivo**: evaluar el THD que circula por el neutro para prevenir sobrecalentamientos e incendios en bandejas y canalizaciones.
3. **Auditoría y eficiencia energética**: dimensionar baterías de condensadores, filtrar reactiva, optimizar la facturación y certificar bajo ISO 50001.

![Analizador de redes eléctricas para medir la calidad de la energía](https://circuitoelectrico.com/wp-content/uploads/2026/06/Analizador-redes-electricas-top.webp)

| Característica | Contador eléctrico (compañía) | Analizador de redes |
|---|---|---|
| Objetivo principal | Facturación comercial (cantidad) | Auditoría y diagnóstico técnico (calidad) |
| Parámetros medidos | kWh, kVArh y picos de demanda máxima | Armónicos (THD), transitorios, *flicker*, huecos |
| Frecuencia de muestreo | Baja (cada 15 minutos o mensual) | Muy alta (milisegundos o microsegundos) |
| Detección de anomalías | Nula (ignora la deformación de la onda) | Alta (captura perturbaciones y fallos de red) |

### Distorsión armónica (THD)

Los armónicos son corrientes o tensiones parásitas cuya frecuencia es un múltiplo entero de la fundamental (50 Hz en Europa, 60 Hz en América). Los generan las cargas no lineales: ordenadores, iluminación LED, variadores de frecuencia, cargadores de vehículo eléctrico.

**Distorsión armónica total de tensión** — indicador del efecto:

$$
THD_{V} \left(\%\right) = \frac{\sqrt{\sum_{h = 2}^{\infty} V_{h}^{2}}}{V_{1}} \cdot 100 = \frac{\sqrt{V_{2}^{2} + V_{3}^{2} + V_{4}^{2} + \cdots}}{V_{1}} \cdot 100
$$

**Distorsión armónica total de corriente** — indicador de la causa:

$$
THD_{I} \left(\%\right) = \frac{\sqrt{\sum_{h = 2}^{\infty} I_{h}^{2}}}{I_{1}} \cdot 100 = \frac{\sqrt{I_{2}^{2} + I_{3}^{2} + I_{4}^{2} + \cdots}}{I_{1}} \cdot 100
$$

**Riesgo en el neutro**: en sistemas trifásicos, los armónicos de orden triple (3.º, 9.º, 15.º…) no se cancelan entre fases y se suman algebraicamente en el conductor neutro, lo que puede generar corrientes de retorno superiores a la de fase.

### Factor de potencia: DPF y TPF

La potencia activa (P, kW) se transforma en trabajo útil; la reactiva (Q, kVAr) se intercambia con los campos eléctricos o magnéticos de motores y transformadores; la aparente (S, kVA) es la demanda total.

**Factor de potencia de desplazamiento (DPF o cos φ)** — solo desfase fundamental:

$$
FP = \cos \varphi = \frac{P}{S}
$$

**Factor de potencia total (TPF o FP<sub>D</sub>)** — incorpora la distorsión de corriente:

$$
FP_{D} = \frac{\cos \varphi}{\sqrt{1 + THD_{I}^{2}}}
$$

Una instalación puede tener un cos φ cercano a 1 y un factor de potencia total bajo por una corriente muy distorsionada. Si el cos φ es bajo predomina la reactiva convencional (motores, transformadores); si el cos φ es alto pero el TPF es bajo, el problema está en la distorsión armónica y no en la compensación de reactiva.

**Precaución con condensadores**: los condensadores pueden resonar con la impedancia de red y amplificar las corrientes armónicas, sobrecargando equipos. Antes de instalar una batería de condensadores con cargas no lineales conviene analizar el espectro armónico y la red; si hace falta, se usan baterías con reactancias de rechazo.

### Perturbaciones de tensión

| Perturbación | Definición |
|---|---|
| Hueco (*sag*) | Caída temporal de la tensión RMS por debajo del 90 % del nominal, de 0,5 ciclos a 1 minuto (IEEE 1159 / EN 50160) |
| Elevación (*swell*) | Aumento temporal de la tensión RMS por encima del 110 % del nominal, en el mismo intervalo |
| Transitorio impulsivo u oscilatorio | Sobretensión o pico brusco de alto voltaje en la escala de microsegundos, por descargas atmosféricas o conmutación de grandes cargas o capacitores |

Un hueco de pocos milisegundos explica reinicios de PLC o desconexiones de relés que un multímetro nunca detectaría; el analizador lo captura con fecha y hora.

### Desequilibrio de fases y flicker

En un trifásico ideal las tres tensiones y corrientes deberían ser idénticas, lo que exige equilibrar las cargas monofásicas en el diseño. El desequilibrio hace que los motores trifásicos reciban tensiones distintas, generen corrientes internas, se sobrecalienten y consuman más intensidad para mantener su rendimiento, con pérdida de vida útil.

El **flicker** es una fluctuación rápida y repetitiva de la tensión que produce parpadeo visible en la iluminación y fatiga visual.

### Marco normativo

| Norma | Qué regula |
|---|---|
| EN 50160 / IEEE 1159 | Características de la tensión suministrada por la red pública; límites que debe cumplir la compañía en la acometida |
| IEC 61000-4-30 | Algoritmos de medición y clases de analizadores |
| IEC 61000 (serie) | Armónicos de corriente y compatibilidad electromagnética |
| IEEE 519 | Límites de armónicos de corriente inyectados a la red por el usuario (referencia en América) |

El artículo cifra el límite de **THD<sub>V</sub> en el 8 %** según EN 50160, con límites individuales por armónico (3.º, 5.º y 7.º son los más destructivos). Distingue dos clases de analizador:

- **Clase A (IEC 61000-4-30)**: cumple estrictamente los algoritmos de medida; sus registros son defendibles ante un juez o una comercializadora. Es la herramienta de peritaje.
- **Clase S**: equipo de diagnóstico estadístico, más económico, para mantenimiento interno; sus registros no tienen peso legal ante disputas externas.

### Tipos de equipo

| Tipo | Uso |
|---|---|
| Portátil | Trabajo de campo y auditorías; se instala temporalmente (horas a un mes) en un cuadro general; batería de larga duración, pantalla a color y memoria robusta |
| Fijo (panel o riel DIN) | Monitorización continua 24/7 en puertas de cuadros o en el CGBT; conectividad Ethernet, Modbus o Wi-Fi hacia SCADA |

![Analizador de redes portátil para mantenimiento](https://circuitoelectrico.com/wp-content/uploads/2026/06/Analizador-redes-electricas-portatil.webp)

![Analizador de redes fijo de panel o carril DIN para monitorización 24/7](https://circuitoelectrico.com/wp-content/uploads/2026/06/Analizador-redes-electricas-fijo-panel-carril-DIN.webp)

### Conexión segura en un cuadro en tensión

El analizador debe conectarse con la instalación en tensión y a plena carga para registrar el comportamiento real, lo que lo convierte en una de las maniobras más delicadas del mantenimiento. Un destornillador que caiga entre dos fases o una pinza mal colocada puede provocar un arco eléctrico.

- **EPIs**: guantes dieléctricos con protector de cuero, pantalla facial contra arco eléctrico, ropa ignífuga con clasificación cal/cm² y calzado dieléctrico, según la categoría de riesgo del tablero (NFPA 70E / REBT).
- **Categoría del instrumento**: mínimo CAT III 600 V o CAT IV 300 V.
- **Orden de conexión**: primero tierra/neutro (referencia de potencial cero), después L1, L2 y L3 con pinzas aisladas.
- **Sentido de la pinza**: la flecha de la carcasa debe apuntar **de la fuente (suministro o transformador) hacia la carga**. Al revés, el equipo interpreta energía fluyendo hacia atrás y arruina potencias, factor de potencia y diagnóstico de armónicos.
- **Correspondencia**: el sensor 1 abraza la fase 1, el 2 la fase 2, etc.; cruzar sensores y fases produce lecturas erróneas.

### Criterios de elección

1. **Frecuencia de muestreo**: para transitorios ultrarrápidos hace falta capturar en el rango de microsegundos (MHz); con pocas docenas de muestras por ciclo los picos pasan desapercibidos.
2. **Sensores de corriente**: las pinzas rígidas son precisas para corrientes bajas (hasta 100 A o 400 A) y cables de sección pequeña, pero no cierran sobre embarrados anchos; las **bobinas Rogowski** flexibles rodean cables gruesos y pletinas, soportan hasta 3000 A o 6000 A sin saturarse y se recomiendan de al menos 60 cm.
3. **Memoria, conectividad y software**: ranuras SD de alta capacidad, Wi-Fi o Ethernet para ver los datos sin abrir el cuadro y software que genere informes automáticos contrastados con EN 50160, IEC 61000 e IEEE 519.

![Pinzas amperimétricas rígidas incluidas en un analizador de redes](https://circuitoelectrico.com/wp-content/uploads/2026/06/Pinzas-amperimetricas-rigidas-analizador-redes.webp)

![Bobina Rogowski, sensor flexible para analizador de redes](https://circuitoelectrico.com/wp-content/uploads/2026/06/Bobina-Rogowski-sensor-flexible-analizador-redes.webp)

> Nota de la fuente: el recorte es un artículo divulgativo de circuitoelectrico.com, no un texto normativo. Los límites citados (THD<sub>V</sub> ≤ 8 %, sag &lt; 90 %, swell &gt; 110 %) se atribuyen a EN 50160 / IEEE 1159; ante una disputa prevalece el texto de la norma.

## Relacionado

- [[itc-bt-02-normas-de-referencia-en-el-reglamento-electrotecnico-para-baja-tension]] — normas UNE de referencia del REBT
- [[guia-bt-23-proteccion-contra-sobretensiones]] — protección frente a sobretensiones transitorias
- [[esquemas-conexion-neutro-masas]] — esquemas TT, TN e IT y conductor neutro
- [[proteccion-diferencial-selectividad]] — diferenciales y coordinación
- [[caida-de-tension]] — caída de tensión y dimensionado de conductores
