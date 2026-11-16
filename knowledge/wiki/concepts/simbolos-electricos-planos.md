---
title: Símbolos eléctricos normalizados en planos y esquemas
type: concept
tags: [simbolos-electricos, planos, esquemas-electricos, iec-60617, iec-81346]
sources: [articles/2026-11-16-simbolos-electricos-tabla-normalizada.md]
created: 2026-11-16
updated: 2026-11-16
---

# Símbolos eléctricos normalizados en planos y esquemas

Los símbolos eléctricos son el lenguaje gráfico normalizado con el que se representan componentes y conexiones en esquemas y planos. La referencia internacional es la **IEC 60617** (adoptada en Europa como **EN 60617**), mientras que en Estados Unidos se usa **ANSI Y32**; la designación de los elementos sigue la serie **IEC 81346**.

## Puntos clave

- Cada símbolo representa de forma simplificada un componente real: un interruptor manual, una línea inclinada que abre o cierra; un relé, contactos más una bobina.
- **Esquema multifilar**: dibuja cada conductor individual y todas las conexiones físicas. **Esquema unifilar**: resume el circuito en una sola línea por conductor, sin importar cuántos hilos físicos tenga.
- Los símbolos de un mismo componente **difieren entre unifilar y multifilar** (enchufe, interruptor, pulsador, contactos), por eso las tablas normalizadas suelen dar ambas columnas.
- Los contactos se dibujan **en su estado de reposo**: el contacto normalmente abierto (NA) sin conexión y el normalmente cerrado (NC) como conexión cerrada.
- En el magnetotérmico, el **cuadrado** indica protección térmica (sobrecargas) y la **flecha** protección magnética (cortocircuitos); en el diferencial, la **elipse** indica detección de fugas a tierra.
- La designación de elementos usa una **letra de función + número de orden** (`Q1`, `K1`, `S1`, `F2`) y puede estratificarse con los signos de aspecto `=`, `-`, `+` y `%` de la IEC 81346-1.
- Los bornes se marcan con reglas fijas (contactos principales `1-2`, `3-4`, `5-6`; auxiliares `1-2` NC y `3-4` NA; bobinas `A1`/`A2`), lo que evita errores de conexión.
- Se admiten símbolos no normalizados solo si son claros, se documentan en la leyenda del plano, se usan de forma consistente y respetan la IEC 60617 en la medida de lo posible.

## Detalles

### Unifilar frente a multifilar

El artículo distingue los dos tipos de esquema con los que se lee un plano de vivienda:

- **Multifilar**: cada conductor individual se dibuja con todos sus contactos y muestra todas las conexiones físicas entre componentes.
- **Unifilar**: representa el circuito de forma simplificada, con una sola línea por conductor, sin importar cuántos hilos físicos tenga.

Por eso el símbolo del enchufe, del interruptor o del pulsador cambia por completo de una representación a la otra. El plano de planta, en cambio, ubica los elementos sobre la arquitectura y suele unir cada símbolo con líneas discontinuas a su circuito en el cuadro general.

![Tabla de simbología eléctrica normalizada para planos IEC](https://circuitoelectrico.com/wp-content/uploads/2026/02/tabla-simbologia-electrica-normalizada-planos-iec-top.webp)

### Símbolos de vivienda

| Elemento | Símbolo en plano (IEC) | Función |
|---|---|---|
| Enchufe (toma de corriente) | ![Símbolo enchufe](https://circuitoelectrico.com/wp-content/uploads/2026/03/simbolo-enchufe-plano.jpg) | Conexión de receptores a la red |
| Interruptor simple | ![Símbolo interruptor](https://circuitoelectrico.com/wp-content/uploads/2026/03/simbolo-interruptor-plano.jpg) | Abrir o cerrar un circuito de luz |
| Conmutador | ![Símbolo conmutador](https://circuitoelectrico.com/wp-content/uploads/2026/03/simbolo-conmutador-plano.jpg) | Encender la luz desde dos puntos |
| Punto de luz (lámpara) | ![Símbolo lámpara](https://circuitoelectrico.com/wp-content/uploads/2026/03/simbolo-lampara-plano.jpg) | Iluminación del habitáculo |
| Magnetotérmico (PIA) | ![Símbolo PIA](https://circuitoelectrico.com/wp-content/uploads/2026/03/simbolo-magnetotermico-plano.jpg) | Protección contra sobreintensidades |

El símbolo del enchufe tiene como base geométrica estándar un **semicírculo** y varía según la potencia: enchufe básico con toma de tierra (16 A, base Schuko), toma de cocina/horno (25 A) y enchufe trifásico con toma de tierra. Los mecanismos de control (interruptor, conmutador, cruzamiento, pulsador) parten de un **círculo** del que salen una o varias líneas.

![Tabla de símbolos eléctricos básicos más utilizados](https://circuitoelectrico.com/wp-content/uploads/2024/12/Tabla-de-simbolos-electricos-basicos1.jpg)

### Contactos y accionamientos

Los contactos se representan **en estado de reposo**:

- **Normalmente abiertos (NA)**: dibujados sin conexión; el contacto abierto se dibuja hacia la izquierda.
- **Normalmente cerrados (NC)**: dibujados como conexión cerrada; el contacto cerrado se dibuja hacia la derecha.

![Símbolos de contactos normalmente abiertos](https://circuitoelectrico.com/wp-content/uploads/2024/12/Simbolo-contactos-normalmente-abiertos.jpg)

![Símbolo de contacto normalmente cerrado](https://circuitoelectrico.com/wp-content/uploads/2024/12/Simbolo-contacto-normalmente-cerrado.jpg)

Entre los accionamientos, el artículo distingue los **manuales directos** (pulsador, interruptor, seta de emergencia), los **automáticos** (interruptor de proximidad, de nivel, térmico, magnético, final de carrera) y los **manuales indirectos** (válvulas neumáticas o hidráulicas, motores con control manual), en los que el operador no aplica la fuerza directamente sobre la carga.

### Protecciones en el esquema

| Componente | Representación | Significado de los detalles |
|---|---|---|
| Magnetotérmico (PIA/IGA) | ![Símbolo magnetotérmico](https://circuitoelectrico.com/wp-content/uploads/2026/03/simbolo-magnetotermico-plano.jpg) | Cuadrado = protección térmica; flecha = protección magnética |
| Diferencial (ID) | ![Símbolo diferencial](https://circuitoelectrico.com/wp-content/uploads/2026/03/simbolo-unifilar-diferencial.jpg) | Elipse = detección de fugas a tierra |
| Cuadro general (CGMP) | ![Símbolo CGMP](https://circuitoelectrico.com/wp-content/uploads/2026/03/simbolo-unifilar-cuadro-general-cgmp.jpg) | Ubicación física de las protecciones en el plano |
| Limitador de sobretensiones | ![Símbolo limitador](https://circuitoelectrico.com/wp-content/uploads/2026/03/simbolo-unifilar-limitador-sobretensiones.jpg) | Protección contra picos de tensión |

Las tablas del catálogo cubren además fusibles unipolares, seccionadores de neutro, fusibles-interruptores, ICP, magnetotérmicos unipolares/bipolares/tripolares/tetrapolares, diferenciales bipolares y tetrapolares, descargadores de sobretensión monofásicos y trifásicos y relés térmicos de sobreintensidad, todos con su variante multifilar y unifilar.

### Designación de elementos: IEC 81346

La serie **IEC 81346** establece la estructuración e identificación de objetos: la parte 1 fija las reglas de designación y la parte 2 la clasificación y los códigos de letras. Sustituye a la serie **IEC 61346** (1996), que a su vez había sustituido a **IEC 60750** (1983). La edición de 2022 incorporó el **aspecto de tipo**.

La designación básica es **letra de función + número de orden**. Ejemplo: en un cuadro industrial, `Q1` es el interruptor automático principal, `K1` el relé de control, `S1` el pulsador de encendido y `F2` el fusible de protección de un motor. Las letras indican la función y los números distinguen dispositivos de la misma categoría.

La IEC 81346-1 permite identificar un objeto desde cuatro aspectos, cada uno con su signo:

| Signo | Aspecto | Ejemplo |
|---|---|---|
| `=` | Función | `=F1` función de protección de un circuito |
| `-` | Producto | `-Q1` interruptor automático, `-K1` contactor, `-M1` motor |
| `+` | Ubicación | `+A1` armario A1, `+A1-B2` subdivisión dentro del armario |
| `%` | Tipo | Identifica objetos que comparten especificación o tipología |

Una designación de un solo nivel como `-Q1` se lee: aspecto de producto, código de clasificación `Q`, identificador individual `1`. El número no indica posición física ni secuencia de funcionamiento, solo distingue el objeto. Una designación **multinivel** como `-A1-Q1` indica que `Q1` pertenece al conjunto `A1` dentro de la estructura de producto.

Clases de entrada de la IEC 81346-2 (una letra), con ejemplos eléctricos:

| Código | Objetivo | Ejemplos |
|---|---|---|
| B | Detección, medida | Detector de movimiento, fotoeléctrico, de posición |
| C | Almacenamiento de energía | Condensador, baterías |
| E | Suministro de energía radiada o térmica | Calentador, lámpara, luminaria |
| F | Protección directa de un flujo de energía | Fusible, pararrayos (FA), diferencial (FB) |
| G | Producción de flujo de energía | Generador, célula fotovoltaica, pila |
| K | Tratamiento de señales | Relé, contactor, autómata programable, temporizador |
| M | Suministro de energía mecánica | Motor eléctrico, bobina, accionador |
| P | Presentación de información | Amperímetro, voltímetro, vatímetro, led, timbre |
| Q | Conmutación controlada de flujo de energía | Disyuntor, contactor, interruptor-fusible |
| R | Limitación o estabilización | Diodo, inductancia, resistencia, limitador |
| S | Conversión de una operación manual en señal | Pulsador, conmutador, interruptor de control |
| T | Conversión de energía de la misma naturaleza | Transformador, rectificador, conversor de frecuencia |
| U | Mantener objetos en posición definida | Aislador, soporte |
| W | Guía o transporte de energía | Cable, conductor, juego de barras |
| X | Objetos que aseguran una conexión | Conector, borne, cajetín de bornes |

El artículo recuerda que la codificación tradicional de letras (IEC 60750 / IEC 61346) se conserva como referencia histórica, no como clasificación vigente: `F` protección, `K` relés y contactores, `Q` aparamenta de potencia, `S` mando manual, `M` motores, `T` transformadores, `X` bornas y clavijas, `R` resistencias, `C` condensadores, `G` generadores.

### Marcado de bornes

Los bornes son las partes metálicas que conectan el aparato con los conductores; su marcado uniforme (IEC 60947-1 y normas relacionadas) evita errores de conexión y facilita la lectura del esquema.

**Contactos principales** (interruptores de potencia, contactos principales de contactores y relés, automáticos, diferenciales):

| Circuito | Marcado |
|---|---|
| Primero | `1-2` entrada y salida |
| Segundo | `3-4` en dispositivos bipolares |
| Siguientes | `5-6` y sucesivos en tripolares o multipolares |

![Contactos principales de un contactor](https://circuitoelectrico.com/wp-content/uploads/2024/12/Contactos-principales-de-contactor.jpg)

![Contactos principales de un relé térmico](https://circuitoelectrico.com/wp-content/uploads/2024/12/Contactos-principales-de-rele-termico.jpg)

![Contactos principales de un magnetotérmico trifásico](https://circuitoelectrico.com/wp-content/uploads/2024/12/Contactos-principales-de-magnetotermico-trifasico.jpg)

**Contactos auxiliares** (contactores, relés, interruptores y pulsadores): el primer número es el orden del contacto dentro del aparato (no se indica si hay un solo contacto; `9` para relés térmicos) y el segundo indica el estado en reposo:

| Marcado | Significado |
|---|---|
| `1-2` | Contacto NC |
| `3-4` | Contacto NA |
| `5-6` | Contacto NC de temporizador o de protección |
| `7-8` | Contacto NA de temporizador o de protección |
| `1`, `2`, `4` | Común, NC y NA de un contacto conmutado |

Ejemplo: `13-14` es el primer contacto auxiliar de un contactor, normalmente abierto; `21-22` es el segundo, normalmente cerrado.

![Ejemplo de marcado de dos contactos auxiliares de un contactor](https://circuitoelectrico.com/wp-content/uploads/2024/12/Ejemplo-marcado-de-2-contactos-auxiliares-.jpg)

**Bobinas, lámparas, motores y transformadores**:

| Elemento | Marcado |
|---|---|
| Bobina de relé o contactor | `A1` alimentación principal o positivo; `A2` retorno o negativo |
| Lámpara | `X1` entrada de alimentación; `X2` salida o retorno |
| Motor monofásico | `U1-U2` bobina principal; `Z1-Z2` bobina auxiliar de arranque |
| Motor trifásico | `U1-U2`, `V1-V2`, `W1-W2` (entrada y salida de cada bobina) |
| Transformador monofásico | `P1-P2` primario; `S1-S2` secundario |
| Transformador trifásico | `U1-X1`, `V1-Y1`, `W1-Z1` primario; `U2-X2`, `V2-Y2`, `W2-Z2` secundario |

![Marcado de bornes de una bobina](https://circuitoelectrico.com/wp-content/uploads/2024/12/Marcado-bornes-de-bobinas.jpg)

![Marcado de bornes de un motor monofásico](https://circuitoelectrico.com/wp-content/uploads/2024/12/Marcado-bornes-de-motores-monofasicos.jpg)

![Marcado de bornes de un motor trifásico](https://circuitoelectrico.com/wp-content/uploads/2024/12/Marcado-bornes-de-motores-trifasicos.jpg)

![Marcado de bornes de un transformador monofásico](https://circuitoelectrico.com/wp-content/uploads/2024/12/Marcado-bornes-de-transformadores-monofasicos.jpg)

![Marcado de bornes de un transformador trifásico](https://circuitoelectrico.com/wp-content/uploads/2024/12/Marcado-bornes-de-transformadores-trifasicos.jpg)

### Símbolos no normalizados

El artículo admite símbolos adaptados o propios en esquemas de distribución en planta, con cuatro condiciones: explicarlos en la leyenda del plano, usarlos de forma consistente en todos los documentos, que sean intuitivos para quien consulta el plano y respetar las normas existentes (IEC 60617) en la medida de lo posible.

> Nota de la fuente: el recorte es un artículo divulgativo de circuitoelectrico.com. Las normas citadas (IEC 60617, EN 60617, ANSI Y32, IEC 81346, IEC 60947-1) son la referencia; ante un conflicto, prevalece el texto de la norma.

## Relacionado

- [[esquema-unifilar-bt-elc2]] — formulario ELEC-2 y representación unifilar de la instalación
- [[itc-bt-02-normas-de-referencia-en-el-reglamento-electrotecnico-para-baja-tension]] — normas UNE de referencia del REBT
- [[instalaciones-interiores-viviendas-bt]] — circuitos y elementos de la instalación de vivienda
- [[proteccion-diferencial-selectividad]] — diferenciales y selectividad
- [[guia-bt-23-proteccion-contra-sobretensiones]] — protectores contra sobretensión
