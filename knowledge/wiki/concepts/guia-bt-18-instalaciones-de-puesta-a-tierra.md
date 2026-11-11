---
title: Guía-BT-18 — Instalaciones de puesta a tierra
type: concept
tags: [rebt, guia-tecnica, baja-tension, itc-bt-18, toma-de-tierra, electrodos]
sources: [papers/2026-11-10-guia-bt-18-instalaciones-de-puesta-a-tierra.md]
created: 2026-11-10
updated: 2026-11-10
---

# Guía-BT-18 — Instalaciones de puesta a tierra

La Guía-BT-18 (edición de octubre de 2005, revisión 1, Ministerio de Industria y Turismo) desarrolla la aplicación de la instrucción: electrodos, conductores de tierra y de protección, borne principal y resistencia. La [[itc-bt-18-instalaciones-de-puesta-a-tierra]] del BOE tiene autoridad y prevalece.

## Puntos clave

- Electrodos admisibles: barras y tubos, pletinas y conductores desnudos, placas, anillos o mallas, armaduras de hormigón no pretensadas y otras estructuras apropiadas; cobre de clase 2 (UNE 21.022) y profundidad no inferior a 0,50 m. La puesta a tierra limita la tensión de las masas metálicas y asegura la actuación de las protecciones.
- Conductores de tierra: sección no inferior a la de los conductores de protección y, si van enterrados, la de la tabla 1; la guía recomienda 35 mm² de cobre desnudo.

| Tipo | Protegido mecánicamente | No protegido |
|---|---|---|
| Con protección contra la corrosión | Según apartado 3.4 | 16 mm² Cu / 16 mm² acero galvanizado |
| Sin protección contra la corrosión | 25 mm² Cu / 50 mm² hierro | — |

- Conductores de protección: sección por la tabla 2 (S ≤ 16 → Sp = S; 16 < S ≤ 35 → 16 mm²; S > 35 → S/2) o por cálculo según la UNE 20.460-5-54; fuera de la canalización, cobre de 2,5 mm² con protección y 4 mm² sin ella.
- Borne principal de tierra con puente seccionador desmontable por útil, de sección igual a la del conductor de tierra.
- Tensión de contacto máxima: 24 V en local o emplazamiento conductor y 50 V en los demás casos; dos tomas son independientes si la que recibe la máxima corriente de defecto no supera 50 V. La resistencia se estima con las fórmulas de la tabla 5:

| Electrodo | Resistencia (Ω) |
|---|---|
| Placa enterrada | R = 0,8 ρ/P (P, perímetro en m) |
| Pica vertical | R = ρ/L (L, longitud en m) |
| Conductor horizontal | R = 2 ρ/L (ρ, resistividad en Ω·m) |

- Separación entre el centro de transformación y las masas de uso: 15 m con resistividad < 100 Ω·m o la distancia D = 2 ρ I_d / U (U = 1.200 V en redes TT con defecto en AT eliminado en ≤ 5 s; 250 V en otro caso).
- Revisión: comprobación obligatoria al dar de alta la instalación, medición anual en la época más seca y descubrimiento de electrodos al menos cada cinco años.

## Detalles

Los materiales deben mantener la resistencia en el tiempo, dejar circular las corrientes de defecto y de fuga sin peligro térmico, mecánico ni eléctrico y contemplar los riesgos de electrólisis; las canalizaciones metálicas de otros servicios no pueden usarse como tomas de tierra.

En el esquema TN las funciones de protección y neutro pueden combinarse en un conductor CPN de 10 mm², o de 4 mm² en cobre concéntrico con conexiones duplicadas.

## Divergencias con la ITC-BT-18

- La guía (12) designa a «Director de la Obra o Instalador Autorizado»; la ITC-BT-18 exige «Director de la Obra o Empresa instaladora» (art. 7.1 del RD 560/2010). Prevalece la ITC-BT-18.
- La guía (3.2) recomienda 35 mm² de cobre enterrado y desnudo; la ITC-BT-18 fija 16 mm² o 25 mm² para el cobre. Prevalece la ITC-BT-18.
- La guía (3.4) añade las constantes k y la condición de tiempo de corte no superior a 5 s; la ITC-BT-18 solo remite a la UNE 20.460-5-54, apartado 543.1.1. Prevalece la ITC-BT-18.
- La guía (3.1) recomienda 0,8 m con heladas y fija dimensiones mínimas de electrodo con las UNE 21056 y 202006; la ITC-BT-18 solo fija 0,50 m y remite a la UNE 21.022, sustituida por la UNE-EN 60228. Prevalece la ITC-BT-18.
- La guía (3.3) exige que el puente seccionador tenga la sección del conductor de tierra; la ITC-BT-18 no la determina. Prevalece la ITC-BT-18.
- La guía (10 y 11) añade el procedimiento con electrodos auxiliares, R = 1,6 ρ/P, el coeficiente 0,5–0,6 de la UNE 207003 y los coeficientes k y n; la ITC-BT-18 fija 50 V, 15 m y D = 2 ρ I_d / U. Prevalece la ITC-BT-18.
- La guía incorpora un anexo 1 con las topologías de redes de tierras para equipos de tecnología de la información ausente de la ITC-BT-18. Prevalece la ITC-BT-18.

## Relacionado

- [[itc-bt-18-instalaciones-de-puesta-a-tierra]]
- [[toma-de-tierra-edificios-viviendas]]
- [[reglament-electrotecnic-baixa-tensio]]
- [[itc-bt-19-instalaciones-interiores-o-receptoras-prescripciones-generales]]
- [[itc-bt-24-instalaciones-interiores-o-receptoras-proteccion-contra-los-contactos-directos-e-indirectos]]
- [[itc-bt-26-instalaciones-interiores-en-viviendas-prescripciones-generales-de-instalacion]]
- [[itc-bt-02-normas-de-referencia-en-el-reglamento-electrotecnico-para-baja-tension]]
