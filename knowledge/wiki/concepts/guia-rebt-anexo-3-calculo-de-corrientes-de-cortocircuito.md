---
title: Guía REBT Anexo 3 — Cálculo de corrientes de cortocircuito (edición sep 03, rev 1)
type: concept
tags: [rebt, guia-tecnica, baja-tension, cortocircuito]
sources: [papers/2026-11-10-guia-rebt-anexo-3-calculo-de-corrientes-de-cortocircuito.md]
created: 2026-11-10
updated: 2026-11-10
---

# Guía REBT Anexo 3 — Cálculo de corrientes de cortocircuito (edición sep 03, rev 1)

El Anexo 3 de las Guías Técnicas de Aplicación del REBT (edición sep 03, revisión 1) ofrece un método simplificado para estimar la intensidad de cortocircuito máxima en un punto de la instalación cuando se desconoce la impedancia del circuito de alimentación a la red. Es material de apoyo, no normativa: el REBT (RD 842/2002) y sus ITC-BT prevalecen sobre la guía, y la capacidad de corte de las protecciones se rige por la ITC-BT-22.

## Puntos clave

- Al desconocerse la impedancia del transformador, de la red de distribución y de la acometida, se admite que en el cortocircuito la tensión en el inicio de las instalaciones de los usuarios es 0,8 veces la tensión de suministro.
- Se toma el defecto fase-tierra como el más desfavorable y se supone despreciable la inductancia de los cables. La consideración es válida cuando el Centro de Transformación está fuera del edificio o lugar del suministro afectado; si está dentro, hay que considerar todas las impedancias.
- Fórmula simplificada: Icc = 0,8 · U / R, donde U es la tensión de alimentación fase neutro (230 V) y R la resistencia del conductor de fase entre el punto considerado y la alimentación.
- R debe recoger la suma de las resistencias de los conductores entre la Caja General de Protección y el punto considerado, por ejemplo el cuadro donde se instalan los dispositivos generales de mando y protección. Se calcula con los conductores a 20 ºC para obtener el valor máximo posible de Icc, con resistividad del cobre de 0,018 Ω·mm²/m y del aluminio de 0,029 Ω·mm²/m (R = ρ · L / S).
- Ejemplo de la guía: vivienda de grado de electrificación básico con derivación individual de 10 mm² de cobre y 15 m, y línea general de alimentación de 95 mm² con 25 m entre la CGP y la centralización de contadores. R(DI) = 0,054 Ω, R(LGA) = 0,0095 Ω, R = 0,0635 Ω e Icc = 0,8 · 230 / 0,0635 ≈ 2898 A.

## Detalles

En el ejemplo, la longitud que entra en la fórmula es el doble de la longitud real de cada tramo (15 · 2 m y 25 · 2 m), de modo que la resistencia considerada es la del camino que la corriente de cortocircuito recorre entre el punto de cálculo y la alimentación.

El resultado contrasta la capacidad de corte de las protecciones: la ITC-BT-22 exige que el dispositivo de protección contra cortocircuitos del origen de cada circuito tenga una capacidad de corte de acuerdo con la intensidad de cortocircuito que pueda presentarse en el punto de su conexión, y la ITC-BT-05 considera defecto grave la falta de protección adecuada contra cortocircuitos y sobrecargas.

El anexo acota el alcance de su simplificación: al despreciar la inductancia de los cables y sustituir la impedancia de la red por un factor fijo de 0,8, el valor es una estimación y no es válido si el Centro de Transformación de origen está dentro del edificio.

## Divergencias con el REBT

Sin divergencias detectadas con el texto consolidado del REBT (BOE).

## Relacionado

- [[reglament-electrotecnic-baixa-tensio]]
- [[itc-bt-22-instalaciones-interiores-o-receptoras-proteccion-contra-sobreintensidades]]
- [[itc-bt-05-verificaciones-e-inspecciones]]
