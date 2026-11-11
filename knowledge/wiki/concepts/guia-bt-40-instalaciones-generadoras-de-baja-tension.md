---
title: Guía-BT-40 — Instalaciones generadoras de baja tensión: esquemas de conexión y protecciones
type: concept
tags: [rebt, guia-tecnica, baja-tension, itc-bt-40, generadores]
sources: [papers/2026-11-10-guia-bt-40-instalaciones-generadoras-de-baja-tension.md]
created: 2026-11-10
updated: 2026-11-10
---

# Guía-BT-40 — Instalaciones generadoras de baja tensión: esquemas de conexión y protecciones

La Guía-BT-40 es la guía técnica de aplicación del REBT editada por el Ministerio de Industria y Turismo (edición de septiembre, revisión 1) que desarrolla la ITC-BT-40. Recorre las condiciones de conexión, los cables, la forma de la onda, las protecciones, la puesta a tierra y la puesta en marcha de las instalaciones generadoras, y añade los esquemas de conexión y los ensayos que el reglamento no detalla. Es un documento de apoyo: la ITC-BT-40 del REBT (RD 842/2002, texto consolidado del BOE) tiene autoridad y ninguna interpretación de la guía deroga sus prescripciones.

## Puntos clave

- **Clasificación**: aisladas, asistidas e interconectadas, con los subtipos c1 (conexión en BT) y c2 (en AT, con transformador elevador) y los modos independiente y separado.
- **Esquemas**: 16 (1 y 2 aisladas y asistidas; 3 a 13 interconectadas c1; 14 a 16 c2), con titular, punto de conexión, funcionamiento, ubicación y tipo de medida.
- **Partes de la instalación generadora**, asimiladas a la ITC-BT-12: caja general de protección, línea general de conexión, interruptor general de maniobra, equipo de medida, línea individual del generador, interruptor de control de potencia, protecciones interiores y equipo generador.
- **Transferencia de carga sin corte** (asistidas): sólo con generadores de más de 100 kVA, conmutación en punto único junto a la medida e interconexión no superior a 5 segundos.
- **Potencia máxima interconectada**: 100 kVA en 3x400/230 V y 60 kVA en 3x220/127 V, sin exceder la mitad de la salida del centro de transformación; en eólicos, el 5 % de la potencia de cortocircuito del punto de conexión.
- **Sincronización**: diferencias admisibles de ±8 % en tensión, ±0,1 Hz en frecuencia y ±10º de fase.
- **Cables**: dimensionados para el 125 % de la máxima intensidad del generador, con caída de tensión no superior al 1,5 %.
- **Onda**: tensión prácticamente senoidal, con tasa máxima de armónicos de 4/n en los pares, 5 en el tercer armónico y 25/n en los impares de orden igual o superior a 5.
- **Puesta a tierra**: esquema TT con tierra de masas independiente de la del neutro de la red, redes de tierras independientes cuando la diferencia de tensión no supere 50 V y detección de la corriente de neutros que desconecta al superar el 50 % de la intensidad nominal.

| Protecciones mínimas (cap. 7) | Actuación |
|---|---|
| Sobreintensidad | Relé magnetotérmico directo o equivalente |
| Mínima tensión | Instantánea, entre fases y neutro, en menos de 0,5 s al llegar al 85 % |
| Sobretensión | Entre fase y neutro, en menos de 0,5 s al llegar al 110 % |
| Frecuencia | Máxima y mínima, entre fases, fuera de 49–51 Hz durante más de 5 períodos |

## Detalles

La guía se aplica a las instalaciones que transforman energía no eléctrica en eléctrica (motores de combustión, turbinas, fotovoltaicos, eólicos de BT, acumuladores, células de combustible) y define "Redes de Distribución Pública" y "Autogenerador" igual que la ITC-BT-40. En sus condiciones generales remite a la normativa sectorial de cada tecnología, a la UNE 20460-7-712, a la ITC-BT-30 para la intemperie y al RD 2267/2004 y al DB-SI (RD 314/2006) en edificios o establecimientos industriales: locales de uso exclusivo, bien ventilados y con conductos de gases incombustibles.

En las aisladas, la conexión a los receptores exige un dispositivo que permita conectar y desconectar la carga y, si varios generadores exigen sincronización, un equipo manual o automático salvo que el inversor ya la incorpore; los generadores portátiles llevan sus propias protecciones. En las asistidas, la conmutación entre red y generador puede hacerse en varios puntos, manual con enclavamiento mecánico o automática con enclavamiento eléctrico, e impide el acoplamiento simultáneo de ambas fuentes; las protecciones son precintables y la maniobra accesible al autogenerador.

En las interconectadas, la conexión no debe alterar la explotación, la protección ni el desarrollo de la red. La guía entiende por punto de conexión aquel en el que se instala el primer elemento de protección general visto desde la red, que no coincide necesariamente con el punto de medida; en el tipo c2 es un seccionador frontera conforme a la ITC 19 de la MIE-RAT y al PO 12.2. En modo separado, sobre configuración IT, TN o TT, debe cumplirse la ITC-BT-24 para cualquier combinación de fuentes.

En el arranque, la caída de tensión de un generador asíncrono no supera el 3 % de la tensión asignada; en eólicos, 3 conexiones por minuto con una caída del 2 % durante 1 segundo, y conexión tras alcanzar el 90–100 % de la velocidad de sincronismo. En los síncronos, de uso acordado con la distribuidora, los puntos sin equipo de sincronismo llevan enclavamiento. La calidad de onda añade las normas UNE-EN 61000-3-2, -3-12, -6-3 y -6-4 y dos ensayos del RD 1699/2011: la inyección de corriente continua, que no debe superar el 0,5 % de la corriente nominal, y la generación de sobretensiones, con dos grupos de límites (tipo c1 y tipo c2) verificados a más del 50 % de la potencia asignada.

El capítulo de protecciones desarrolla los elementos exigidos por el RD 1699/2011: corte general con seccionamiento, diferencial que no puede ser de tipo AC si existe corriente continua de defecto y, en viviendas, 30 mA; las protecciones no convencionales se verifican con informe de laboratorio acreditado, que evalúa también el precintado. La reconexión tras una pérdida de red exige tensión y frecuencia normales durante tres minutos, y la detección de isla se verifica según la EN 62116 con factor de calidad Q = 1 + 0,05 y desconexión en menos de 2 segundos, con un ensayo adicional para dos inversores en paralelo.

La puesta a tierra asegura los valores de la MIE-RAT 13 y evita transferencias de defectos a la red; donde la legislación exija separación galvánica, la guía identifica las tres funciones del transformador de aislamiento (aislar, dar seguridad personal, evitar la inyección de corriente continua) y admite otras soluciones con convertidores electrónicos. Para la puesta en marcha, asistidas e interconectadas presentan a la distribuidora el proyecto de las partes que afectan al acoplamiento y la seguridad, y el certificado de superación de pruebas incorpora los informes de laboratorio sobre calidad de onda, protecciones y conmutación.

## Divergencias con la ITC-BT-40

- **Apartado 4.3.3 derogado**: la guía desarrolla íntegramente "Equipos de maniobra y medida a disponer en el punto de interconexión" (interruptor automático en punto único y accesible, protecciones que deben actuar sobre él, precintado, contacto auxiliar de neutro, equipo de medida y contador de energía reactiva) y remite a ese apartado desde los capítulos 4.2.A y 7. El texto consolidado del BOE lo muestra como "(Derogado)", por el RD 244/2019. Prevalece la ITC-BT-40.
- **Régimen de autoconsumo ausente en la guía**: el apartado 4.3 del texto consolidado exige que toda instalación de autoconsumo interconectada, sea cual sea su potencia, limite la inyección de corriente continua y la generación de sobretensiones y que impida el funcionamiento en isla; impone a las de autoconsumo sin excedentes un sistema que evite el vertido conforme al anexo I, las exime de los apartados 4.3.1 y 4.3.4 y de los requisitos con la distribuidora del apartado 9, y obliga a entregar con el certificado la documentación de conformidad del anexo I.4. La guía, anterior a esa modificación, no menciona ni el autoconsumo ni el anexo I. Prevalece la ITC-BT-40.
- **Condiciones de conexión de la producción próxima a consumo**: el apartado 4.3 del texto consolidado exige cuadro de mando y protección con diferencial tipo A y 30 mA si la instalación es accesible al público general o está en zonas residenciales, admite tres puntos de conexión y prohíbe conectar la producción directamente a la instalación interior de los consumidores en autoconsumo colectivo, obliga a circuito independiente y dedicado con diferencial tipo A a los generadores con excedentes y a los sin excedentes de potencia instalada superior a 800 VA, y limita a 10 mA la corriente de fuga a tierra de los generadores en viviendas sin circuito dedicado ni transformador de aislamiento. La guía no recoge ninguno de esos valores. Prevalece la ITC-BT-40.
- **Carácter condicional de las protecciones mínimas**: el apartado 7 de la ITC-BT-40 introduce la lista de protecciones mínimas con la cláusula "con independencia de que estos ajustes podrían verse modificados por la normativa del sector eléctrico en función del generador al que aplique"; la guía reproduce la misma lista sin esa cláusula y la completa después con los tiempos y ajustes del RD 1699/2011. Prevalece la ITC-BT-40.

Nota de alcance: las referencias de la guía al RD 1699/2011, al RD 661/2007, a los procedimientos de operación P.O. 12.2 y P.O. 12.3, a la MIE-RAT, al RD 1955/2000 y a la OM de 5 de septiembre de 1985 no son divergencias: regulan la conexión al sistema eléctrico, un ámbito distinto del REBT. Sólo serían divergencia si contradijeran valores del reglamento.

## Relacionado

- [[itc-bt-40-instalaciones-generadoras-de-baja-tension]]
- [[reglament-electrotecnic-baixa-tensio]]
- [[itc-bt-24-instalaciones-interiores-o-receptoras-proteccion-contra-los-contactos-directos-e-indirectos]]
- [[guia-bt-18-instalaciones-de-puesta-a-tierra]]
- [[guia-bt-23-proteccion-contra-sobretensiones]]
