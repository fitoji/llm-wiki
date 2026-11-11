---
title: Guía-BT-22 — Protección contra sobreintensidades
type: concept
tags: [rebt, guia-tecnica, baja-tension, itc-bt-22, sobreintensidades, proteccion]
sources: [papers/2026-11-10-guia-bt-22-proteccion-contra-sobreintensidades.md]
created: 2026-11-10
updated: 2026-11-10
---

# Guía-BT-22 — Protección contra sobreintensidades

La Guía-BT-22 (edición de octubre de 2005, revisión 1) desarrolla las medidas de protección contra sobreintensidades: criterios de selección de dispositivos, valores de ajuste y un método gráfico para las derivaciones. Acompaña a la [[itc-bt-22-instalaciones-interiores-o-receptoras-proteccion-contra-sobreintensidades]] del BOE, que tiene autoridad y prevalece.

## Puntos clave

- Todo circuito se protege frente a sobrecargas, cortocircuitos y descargas atmosféricas, con un IA de corte omnipolar o fusibles calibrados; en el origen de cada circuito se sitúa la protección contra cortocircuitos.
- Poder de corte igual o mayor que la intensidad de cortocircuito máxima en el punto de instalación; la guía fija 4500 A como mínimo para el IGA.
- Sobrecargas: In ≤ Ib ≤ 1,45 In, con Ib = 1,45 In (UNE-EN 60898 y 61009) o 1,30 In (UNE-EN 60947-2) y, en fusibles gG, If = 1,60 In (In ≥ 16 A), 1,90 In (4 A < In < 16 A) o 2,10 In (In ≤ 4 A).
- Cortocircuitos: S ≥ k·√t con los valores de k por aislamiento y material del conductor, y la condición alternativa I_m > I_cc,mín (I_m = 10 In en un IA doméstico de curva C).

| Aislamiento | T. inicial/final | k cobre | k aluminio |
|---|---|---|---|
| PVC 70 ºC ≤ 300 mm² | 70/160 | 115 | 76 |
| PVC 70 ºC > 300 mm² | 70/140 | 103 | 68 |
| PVC 90 ºC ≤ 300 mm² | 90/160 | 100 | 66 |
| PR/EPR | 90/250 | 143 | 94 |
| Mineral con PVC | 70/160 | 115 | — |

La tabla de la guía añade PVC 90 ºC > 300 mm² (86 y 57), goma 60 ºC (141 y 93) y mineral desnudo (135).

- Posición: los dispositivos se sitúan donde se reduce la corriente admisible; la protección contra sobrecargas puede omitirse en circuitos de excitación de máquinas, electroimanes de elevadores, extinción de incendios, servicios de seguridad y secundarios de transformadores de corriente.
- Método gráfico: triángulo de protecciones con L = (0,8·U·S·γ/(1+m))·(1/Im); el ejemplo de la guía da L = 53,7 m, L' = 32,2 m y α = 31º.

## Detalles

La sección 1.1 reproduce los apartados 432 a 436 de la UNE 20.460-4-43 y admite un poder de corte inferior al cortocircuito máximo si hay un dispositivo aguas arriba suficiente y ambos quedan coordinados: la protección serie o de acompañamiento.

El disparo magnético de los IA es instantáneo y su curva térmica es de tiempo inverso; las clases magnéticas B (3 a 5 In), C (5 a 10 In) y D (10 a 20 In) se eligen según los transitorios previsibles, con D para arranques de motores.

Los fusibles se clasifican por su curva de fusión (g limita la corriente y protege de sobrecargas y cortocircuitos, a solo de cortocircuitos) y por categoría (M motores, Tr transformadores, B líneas largas, R semiconductores, D con retardo); el tipo a debe ir acompañado de protección contra sobrecargas.

La tabla 1, tomada de la UNE 20.460-4-473, resume por esquema (TN-C, TN-S, TT e IT) y por circuito (3F+N, 3F, F+N y 2F) dónde debe preverse el dispositivo de protección y dónde puede omitirse, con seis notas sobre el neutro: corte y conexión simultáneos con las fases y protección diferencial con IΔn ≤ 0,15·In del neutro.

## Divergencias con la ITC-BT-22

- La guía (1.1) fija el ajuste contra sobrecargas y el magnetotérmico exclusivo de los domésticos; la ITC-BT-22 admite fusibles calibrados en toda instalación. Prevalece la ITC-BT-22.
- La guía (1.1) fija 4500 A como poder de corte mínimo del IGA; la ITC-BT-22 solo exige ajustarlo al cortocircuito del punto de conexión. Prevalece la ITC-BT-22.
- La guía (1.1) añade los valores k de S = k·√t, basados en la UNE 211003-1 (ausente del listado de referencia del BOE), y la condición I_m > I_cc,mín; la ITC-BT-22 no los contiene. Prevalece la ITC-BT-22.
- La guía (1.1) recomienda proteger los circuitos secundarios frente a cortocircuitos por continuidad de servicio; la ITC-BT-22 no lo recomienda. Prevalece la ITC-BT-22.
- La guía (1.2) añade las reglas de posición de los dispositivos, los casos de omisión de sobrecargas y el método gráfico del triángulo; la ITC-BT-22 se limita a la tabla 1. Prevalece la ITC-BT-22.
- La guía (1.1) añade una tabla de producto y norma que la ITC-BT-22 no recoge; el listado vigente precisa UNE-EN 60898-1/-2 y UNE-HD 60269-2/-3. Prevalece la ITC-BT-22.
- La guía y la ITC-BT-22 remiten a UNE 20.460-4-43 y -4-473; el listado del BOE ([[itc-bt-02-normas-de-referencia-en-el-reglamento-electrotecnico-para-baja-tension]], Resolución de 20 de marzo de 2025) ya cita UNE-HD 60364-4-43: 2024. Prevalece la ITC-BT-22.

## Relacionado

- [[itc-bt-22-instalaciones-interiores-o-receptoras-proteccion-contra-sobreintensidades]]
- [[reglament-electrotecnic-baixa-tensio]]
- [[itc-bt-17-instalaciones-de-enlace-dispositivos-generales-e-individuales-de-mando-y-proteccion-interruptor]]
- [[itc-bt-19-instalaciones-interiores-o-receptoras-prescripciones-generales]]
