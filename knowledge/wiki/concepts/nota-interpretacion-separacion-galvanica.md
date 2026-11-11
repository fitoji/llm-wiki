---
title: Nota de Interpretación Técnica — Equivalencia de la Separación Galvánica
type: concept
tags: [rebt, guia-tecnica, baja-tension, generacion, separacion-galvanica]
sources: [papers/2026-11-10-guia-nota-interpretacion-separacion-galvanica.md]
created: 2026-11-10
updated: 2026-11-10
---

# Nota de Interpretación Técnica — Equivalencia de la Separación Galvánica

Nota de Interpretación Técnica del Ministerio de Industria, Comercio y Turismo emitida ante las consultas recibidas sobre la conexión de instalaciones generadoras a redes de baja tensión, donde la legislación aplicable exige separación galvánica mediante un transformador o sistema equivalente. Se apoya en los requisitos técnicos de la ITC-BT-40 del REBT (RD 842/2002). Es interpretación oficial del ministerio, no norma: el REBT y sus ITC-BT prevalecen sobre ella.

## Puntos clave

- Equivalencia: donde la legislación exija separación galvánica, por transformador de aislamiento o por otro medio con las mismas funciones, las funciones del transformador de aislamiento de baja frecuencia son las tres de la tabla siguiente. Con convertidores electrónicos pueden usarse transformadores de separación o no usarlos, siempre que se cumplan esas tres funciones.

| Función | Condición que la nota considera suficiente | ITC que la toca |
|---|---|---|
| 1. Aislar la instalación generadora | Transferencia de defectos resuelta, cualquiera que sea el convertidor, si se cumple el esquema prescrito, aplicado por separado a cada parte de la instalación (convertidor y elementos del generador; en fotovoltaica, inversores y cada panel), salvo que estén unidos. Las notas al pie fijan dos condiciones: unión equipotencial entre tierras de edificios distintos (ITC-BT-26, apartado 3.1) y protectores de sobretensión entre fases y tierra con tensión de funcionamiento continuo mayor que la tensión asignada al aislamiento | ITC-BT-40 |
| 2. Proporcionar seguridad personal | La instalación debe cumplir lo que establece la ITC-BT-24 | ITC-BT-24 |
| 3. Evitar la inyección de corriente continua | No superará el 0,5 % de la corriente nominal de la red. Con transformador separador entre el inversor y el punto de conexión se asume cubierto el requisito; con transformador de alta frecuencia o sin transformador hay que demostrarlo mediante el ensayo de cuatro pasos descrito abajo, válido si la componente continua medida en una ventana de al menos 10 segundos es menor que el 0,5 % del valor eficaz de la corriente nominal de salida del inversor | ITC-BT-40 |

- Pasos del ensayo de la función 3: conectar el inversor a una red cuya componente de tensión continua sea despreciable a efectos de medida; ajustar la potencia de salida entre el 25 % y el 100 % de la nominal; esperar el régimen estacionario térmico (variación inferior a 2 ºC en 15 minutos); medir la componente continua inyectada.

Clasificación por topología de conexión a la red:

| Tipo | Definición en la nota |
|---|---|
| a) Instalaciones aisladas | Uso exclusivo de alimentar cargas o circuitos de baja tensión |
| b) Instalaciones generadoras independientes de la red | Uso exclusivo de alimentación de cargas o circuitos de baja tensión, que pueden estar alternativamente alimentados por la red o por el generador |
| c1) Interconectadas en baja tensión | Punto de conexión en la red de distribución de baja tensión en la que hay otros circuitos e instalaciones conectados, en paralelo con la red, tanto si la finalidad es vender energía como alimentar cargas |
| c2) Interconectadas en alta tensión | Punto de conexión en la red de alta tensión mediante transformador elevador, sin otras redes de baja tensión que alimenten cargas ajenas |

- En las instalaciones de tipo c), con la red desconectada pueden alimentarse cargas propias si se cumplen las condiciones de desconexión y conexión del capítulo 4 de la ITC-BT-40.
- Punto de conexión: punto en que la instalación generadora se conecta a la red de la empresa distribuidora, delimitando la extensión de la instalación; no tiene por qué coincidir con el punto de medida de energía, pero es donde se instalan las protecciones generales.

## Detalles

La nota clasifica las instalaciones por su topología porque cada tipo tiene condiciones distintas, y ese es el procedimiento para aplicar las tres funciones. El tipo c2) queda incluido en las condiciones del REBT, aunque por conectarse directamente a la red de alta tensión exige condiciones especiales de conexión, atendiendo a la reglamentación vigente sobre protecciones y conexión en alta tensión.

Las condiciones de aislamiento se aplican por separado a cada parte de la instalación, de modo que la inversión y los paneles de una instalación fotovoltaica se tratan como elementos independientes mientras no estén unidos. La referencia a la ITC-BT-26 apartado 3.1 para la unión equipotencial entre tierras de edificios distintos es coherente con esa instrucción, que contempla unir los anillos de toma de tierra de construcciones próximas.

## Divergencias con el REBT

- La nota parte de que la ITC-BT-40 establece la necesidad de separación galvánica. El texto consolidado de esa instrucción en el BOE no la contiene: clasifica las instalaciones en aisladas, asistidas e interconectadas y, en su apartado 4.3, exige dispositivos que limiten la inyección de corriente continua y la generación de sobretensiones e impidan el funcionamiento en isla. Prevalece la ITC-BT-40.
- La nota fija el límite de inyección de corriente continua en el 0,5 % de la corriente nominal y un ensayo de cuatro pasos. El apartado 4.3 de la ITC-BT-40 solo exige dispositivos que limiten esa inyección, sin fijar valor ni procedimiento. Prevalece la ITC-BT-40.
- La nota introduce el tipo c2), con punto de conexión en alta tensión mediante transformador elevador. La clasificación del apartado 2 de la ITC-BT-40 se limita a aisladas, asistidas e interconectadas, sin ese desglose; la propia nota lo reconoce y remite a la reglamentación de alta tensión. Prevalece la ITC-BT-40.

## Relacionado

- [[reglament-electrotecnic-baixa-tensio]]
- [[itc-bt-40-instalaciones-generadoras-de-baja-tension]]
- [[itc-bt-24-instalaciones-interiores-o-receptoras-proteccion-contra-los-contactos-directos-e-indirectos]]
- [[itc-bt-26-instalaciones-interiores-en-viviendas-prescripciones-generales-de-instalacion]]