---
title: Guía REBT Anexo 2 — Cálculos de caídas de tensión (rev 2)
type: concept
tags: [rebt, guia-tecnica, baja-tension, caidas-de-tension, secciones]
sources: [papers/2026-11-10-guia-rebt-anexo-2-calculos-de-caidas-de-tension.md]
created: 2026-11-10
updated: 2026-11-10
---

# Guía REBT Anexo 2 — Cálculos de caídas de tensión (rev 2)

El Anexo 2 de las Guías Técnicas de Aplicación del REBT (revisión 2) desarrolla el cálculo de la sección de los conductores por caída de tensión: línea corta, sección mínima normalizada, límites reglamentarios y cinco ejemplos. Guía no vinculante: prevalecen el RD 842/2002 y sus ITC-BT, único texto vinculante (BOE).

## Puntos clave

- Tres criterios simultáneos: calentamiento (70 °C termoplástico, 90 °C termoestable), caída de tensión y cortocircuito (160 °C/250 °C en menos de 5 s), poco determinante en baja tensión.
- Línea corta (menos de 50 km): ΔU = R·I·cos φ + X·I·sen φ [1]; ΔU = (R + X·tan φ)·(P/U₁) [4] en trifásico y ΔU = 2·(R + X·tan φ)·(P/U₁) [5] en monofásico.
- Hasta 120 mm² la reactancia es despreciable (0,15R a 150 mm², 0,20R a 185 mm², 0,25R a 240 mm²): ΔU = R·P/U₁ [6] y ΔU = 2·R·P/U₁ [7].
- R = c·ρ·L/S con c ≈ 1,02 por efecto piel y proximidad; resistividad a 20/70/90 °C: cobre 0,018/0,021/0,023 y aluminio 0,029/0,033/0,036 Ω·mm²/m.
- S = c·ρ·P·L/ΔU [13] y S = 2·c·ρ·P·L/ΔU [14]; simplificado con conductividad γ (cobre 56/48/44, aluminio 35/30/28 m/Ω·mm² a 20/70/90 °C): S = P·L/(γ·e·U) [15] y S = 2·P·L/(γ·e·U) [16].
- Temperatura real T = T₀ + (T_máx − T₀)·(I/I_máx)² [17] (25 °C enterrado, 40 °C al aire) para una segunda iteración; valores unitarios e_u = e/(L·I) [18] en V/(A·km), tablas 4 (450/750 V) y 5 (0,6/1 kV).
- Límites reglamentarios (tabla 6 del anexo; la LGA es siempre trifásica; e = porcentaje de 400 V o 230 V):

| Parte | Alimenta a | Caída máxima |
|---|---|---|
| LGA | Contadores concentrados | 0,5 % |
| LGA | Centralización parcial | 1,0 % |
| DI | Usuario único | 1,5 % |
| DI | Contadores concentrados | 1,0 % |
| DI | Centralización parcial | 0,5 % |
| Interiores | Viviendas | 3 % |
| Interiores | Alumbrado (no viviendas) | 3 % |
| Interiores | Fuerza (no viviendas) | 5 % |

## Detalles

El anexo ofrece dos itinerarios: el simplificado, que admite la temperatura máxima del aislamiento, y el detallado, que estima la temperatura real y permite secciones normalizadas inferiores. En una LGA de 145 kW y 40 m se obtienen 232,5 A y 240 mm² a 46 °C.

En una vivienda de electrificación básica (5750 W, 25 A) las DI necesitan 6, 10 y 16 mm² para 10, 22 y 35 m; en electrificación elevada (40 A), 10, 16 y 35 mm². El circuito interior C2 (16 A, 30 m) exige 4 mm².

Las intensidades admisibles proceden de la tabla 1 de la ITC-BT-19 (modo B) y de la tabla A de la guía BT-14 para cables enterrados; los factores de reducción por agrupación se aplican salvo conductores por debajo del 30 % de su carga nominal.

## Divergencias con el REBT

- Derivación individual de un único usuario: la tabla 6 asigna un 1,5 % sin condición; la ITC-BT-15 lo condiciona a «suministros para un único usuario en que no existe línea general de alimentación». Prevalece la ITC-BT-15.
- Instalación industrial alimentada en alta tensión: la tabla 6 omite el supuesto de la ITC-BT-19 (2.2.2), con caídas admisibles del 4,5 % en alumbrado y del 6,5 % en los demás usos. Prevalece la ITC-BT-19.
- Compensación entre tramos: el anexo fija límites aislados para LGA, DI y circuitos interiores, mientras la ITC-BT-19 (2.2.2) y la ITC-BT-25 (apartado 3) admiten compensar la caída entre instalación interior y derivaciones individuales. Prevalece la ITC-BT-19.

La ITC-BT-18 (puesta a tierra) no fija límites de caída de tensión: el anexo los atribuye a las ITC-BT-14, ITC-BT-15 e ITC-BT-19.

## Relacionado

- [[reglament-electrotecnic-baixa-tensio]]
- [[guia-rebt-anexo-3-calculo-de-corrientes-de-cortocircuito]]
- [[ITC-BT-14]]
- [[ITC-BT-15]]
- [[ITC-BT-19]]
- [[ITC-BT-25]]
