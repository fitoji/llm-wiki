---
title: ITC-BT-06 — Redes Aéreas para Distribución en Baja Tensión
type: concept
tags: [rebt, baja-tension, itc-bt-06, redes-aereas, calculo-mecanico]
sources: [papers/2026-11-10-rebt-itc-bt-06-redes-aereas-para-distribucion-en-baja-tension.md]
created: 2026-11-10
updated: 2026-11-10
---

# ITC-BT-06 — Redes Aéreas para Distribución en Baja Tensión

Fija materiales, cálculo mecánico, ejecución e intensidades admisibles de las redes aéreas de distribución en baja tensión: conductores, apoyos, distancias, cruzamientos y neutro.

## Puntos clave

- Conductores preferentemente aislados, tensión asignada no inferior a 0,6/1 kV (UNE 21.030); secciones mínimas: 16 mm² en aluminio y 10 mm² en cobre.
- Conductores desnudos: carga de rotura mínima 410 daN; utilización de carácter excepcional y debidamente justificada, excluidas las zonas de arbolado o con peligro de incendio.
- Sobrecargas de viento: 50 daN/m² sobre conductores, 100 sobre superficies planas y 70 sobre superficies cilíndricas de apoyos.
- Hielo por zonas de altitud: A (< 500 m) nada; B (500-1000 m) 180√d g/m en desnudos y 60√d en haz; C (> 1000 m) 360√d y 120√d.
- Tracción máxima admisible: carga de rotura dividida por 2,5 en la hipótesis más desfavorable (viento a 15 ºC, o hielo/viento reducido a 0 ºC según la zona); sobre edificaciones o apoyos en fachada, un 25 % más.
- Flecha máxima: la mayor entre las dos hipótesis de zona y la de temperatura máxima previsible, nunca inferior a 50 ºC.
- Distancia mínima al suelo: 4 m en desnudos y cables tensados; 2,5 m en cable posado sobre fachada.

| Material del apoyo | Coeficiente |
|---|---|
| Metálico | 1,5 |
| Hormigón armado vibrado | 2,5 |
| Madera | 3,5 |
| Otros no metálicos | 2,5 |

Con ensayos en verdadera magnitud, pueden reducirse a 1,45 y 2.

## Detalles

**Cables posados sobre fachada.** Se fijan con abrazaderas resistentes a la intemperie. Distancias a aberturas: 0,30 m al borde superior de ventanas y balcones; 0,50 m al borde inferior y laterales de ventanas (1,00 m a los laterales del balcón); 0,05 m a elementos metálicos de fachada, salvo protección conforme a la ITC-BT-11. Bajo 2,5 m, protección según esa ITC, sin pasar delante de aberturas.

**Cables tensados.** Con neutro fiador, entre piezas especiales sobre apoyos o fachadas (el aislamiento no cuenta como elemento resistente); el resto, con fiador de acero de 800 daN mínimo. Los empalmes soportan el 90 % de la carga de rotura; sin soldadura ni torsión directa.

**Desnudos: separaciones y zona de protección.** Entre conductores de polaridad distinta: 0,10 m en vanos hasta 4 m, 0,15 m de 4-6 m, 0,20 m de 6-30 m y 0,30 m de 30-50 m; en vanos mayores, D = 0,55√F (F, flecha en metros); en apoyos de derivación, la mitad, mínimo 0,10 m. Los desnudos sobre apoyos en fachada quedan a 0,20 m como mínimo, sin invadir la zona de protección con fuertes vientos; y en redes que crucen sobre edificaciones o usen apoyos de fachada, la tracción admisible se reduce un 25 %. Zona de protección sobre edificaciones: tejados, plano a 1,80 m (1,50 m puestos a tierra; pendiente mayor de 45 grados, 1 m); terrazas y balcones, 3 m; fachadas, plano vertical a 0,20 m del muro sin aberturas y a 1 m de ventanas y balcones, con horizontal a 0,30 m sobre la abertura y 3 m bajo el antepecho.

**Neutro.** Sección mínima: la de fase con dos o tres conductores; con cuatro, la tabla 1 de la ITC-BT-07 (mínimo 10 mm² en cobre, 16 mm² en aluminio). No puede interrumpirse salvo con corte omnipolar simultáneo, conexión del neutro antes que las fases, o uniones amovibles señaladas y maniobrables solo con herramientas. Se pone a tierra en el centro de transformación y, en esquemas TT y TN (TN-S para el conductor de protección), al menos cada 500 m, prefiriendo los puntos de derivaciones importantes; en apoyo de madera, los soportes metálicos de los aisladores de fase se unen al neutro.

**Cruzamientos y paralelismos.** Con alta tensión, la baja tensión cruza por debajo, con distancia vertical d ≥ 1,5 + (U + L₁ + L₂)/100 (U en kV; L₁ y L₂, metros al apoyo más próximo); por encima exige autorización expresa. Con telecomunicación, la de desnudos cruza por encima (1 m, 0,50 m en apoyo común); por debajo, solo con haz de acero galvanizado a tierra entre ambas líneas o conductores 0,6/1 kV en el vano. Con carreteras y ferrocarriles no electrificados, altura mínima 6 m y sin empalmes (rotura ≥ 410 daN; 280 en acometidas aisladas); con ferrocarriles electrificados, tranvías y trolebuses, 2 m sobre la línea de contacto y 0,30 m mínimos al elemento de toma de corriente desconectado; con teleféricos, 2 m por encima o 3 m por debajo (apoyos adyacentes a tierra); con ríos navegables, H = G + 1 m (G, gálibo; sin gálibo, 6 m); con antenas, 1 m, y prohibido fijar antenas o tirantes en los apoyos; con agua o gas, 0,20 m (1 m en desnudas), sin cruzar por la vertical de juntas. En paralelismo con alta tensión, 1,5 veces la altura del mayor apoyo (2 m hasta 66 kV y 3 m por encima); con calles y carreteras, 6 m en zonas de circulación rodada y 5 m en el resto (4 m para aislados fuera de zonas rodadas); en arbolado, preferencia por cables en haz.

**Intensidades admisibles.** Para cables en haz XLPE (UNE 21.030) a 40 ºC valen las tablas de la instrucción. Factores de corrección: 0,9 o menor con radiación solar muy fuerte; por agrupación al aire, 1,00 / 0,89 / 0,80 / 0,75 para 1, 2, 3 y más de 3 cables (otras configuraciones, UNE 21.144-2-2); y por temperatura, de 1,18 (20 ºC) a 0,90 (50 ºC). Además, tablas de cortocircuito en kA según duración (0,1 a 3 s) y de densidades de corriente en A/mm² para desnudos de cobre y aluminio. Otros cables o sistemas: serie UNE 20.435 o cálculo según UNE 21.144.

## Relacionado

- [[itc-bt-07-redes-subterraneas-para-distribucion-en-baja-tension]]
- [[itc-bt-11-redes-de-distribucion-de-energia-electrica-acometidas]]
