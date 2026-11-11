---
title: Instalaciones de puesta a tierra
type: concept
tags: [rebt, baja-tension, itc-bt-18, toma-de-tierra, electrodos]
sources: [papers/2026-11-10-rebt-itc-bt-18-instalaciones-de-puesta-a-tierra.md]
created: 2026-11-10
updated: 2026-11-10
---

# Instalaciones de puesta a tierra

La ITC-BT-18 regula las instalaciones de puesta a tierra: objeto, partes (tomas de tierra, conductores de tierra, bornes y conductores de protección), secciones, resistencia, independencia y revisiones.

## Puntos clave
- Las puestas a tierra limitan la tensión respecto a tierra de las masas metálicas, aseguran la actuación de las protecciones y eliminan o disminuyen el riesgo de avería; son la unión eléctrica directa, sin fusibles ni protección, mediante electrodos enterrados en el suelo.
- Electrodos admisibles: barras o tubos; pletinas y conductores desnudos; placas; anillos o mallas; armaduras de hormigón enterradas (excepto pretensadas); u otras estructuras enterradas apropiadas. Profundidad nunca inferior a 0,50 m.
- Las canalizaciones metálicas de otros servicios (agua, líquidos o gases inflamables, calefacción central, etc.) no deben utilizarse como tomas de tierra.
- Sección de los conductores de tierra (tabla 1):

| Tipo | Protegido mecánicamente | No protegido mecánicamente |
|---|---|---|
| Protegido contra la corrosión | Según apartado 3.4 | 16 mm² Cu / 16 mm² acero galvanizado |
| No protegido contra la corrosión | 25 mm² Cu / 50 mm² hierro | (indicado en la instrucción) |

- En toda instalación se preve un borne principal de tierra al que se unen los conductores de tierra, de protección, de unión equipotencial principal y de puesta a tierra funcional; con un dispositivo desmontable por útil para medir la resistencia.
- Sección de los conductores de protección (tabla 2):

| Sección de fase S (mm²) | Sección mínima Sp (mm²) |
|---|---|
| S ≤ 16 | S |
| 16 < S ≤ 35 | 16 |
| S > 35 | S/2 |

- Conductores de protección fuera de la canalización de alimentación: de cobre, mínimo 2,5 mm² con protección mecánica y 4 mm² sin ella; ningún aparato intercalado en el conductor de protección y las masas no se conectan en serie en el circuito de protección.
- En el esquema TN, funciones de neutro y protección pueden combinarse (CPN/PEN) si el conductor es de al menos 10 mm² en cobre o aluminio y la parte común no está protegida por diferencial residual; excepción de 4 mm² para cable concéntrico de cobre con conexiones duplicadas.
- Conductor principal de equipotencialidad: al menos la mitad de la sección del conductor de protección mayor de la instalación, con mínimo de 6 mm² (reducible a 2,5 mm² si es de cobre); el suplementario entre masa y elemento conductor, la mitad del conductor de protección unido a esa masa.
- Resistencias: la tensión de contacto no superará 24 V en local o emplazamiento conductor y 50 V en los demás casos; dos tomas son independientes cuando, circulando por una la máxima corriente de defecto prevista, la otra no supere 50 V respecto a un punto de potencial cero.
- Revisión: comprobación obligatoria al dar de alta la instalación; medición de la resistencia al menos una vez al año en la época en que el terreno esté más seco; en terrenos no favorables, descubrir electrodos y conductores de enlace al menos cada cinco años.

## Detalles
Las puestas a tierra se establecen por razones de protección (esquemas TN, TT e IT conforme a la ITC-BT-24; con protección por sobreintensidades, el conductor de protección va en la misma canalización que los activos o en su proximidad inmediata), por razones funcionales o combinadas; en este último caso prevalecen las prescripciones de protección. La elección de materiales debe mantener el valor de la resistencia en el tiempo, permitir el paso de las corrientes de defecto y de fuga sin peligro térmico, mecánico ni eléctrico, y contemplar los riesgos de electrólisis.

Las envolventes de conjuntos montados en fábrica o canalizaciones prefabricadas con envolvente metálica pueden servir como conductor de protección si su continuidad eléctrica no resulta afectada por deterioros, su conductibilidad es la exigida y permiten conectar otros conductores en toda derivación predeterminada; los conductos de agua, gas u otros tipos y estructuras metálicas no pueden usarse como conductores de protección.

Para estimar la resistencia a tierra, la instrucción da valores orientativos de resistividad del terreno (tabla 3) y valores medios aproximados (tabla 4):

| Naturaleza del terreno | Resistividad media (Ω·m) |
|---|---|
| Terrenos cultivables y fértiles, terraplenes compactos y húmedos | 50 |
| Terrenos cultivables poco fértiles y otros terraplenes | 500 |
| Suelos pedregosos desnudos, arenas secas permeables | 3.000 |

Tabla 5. Fórmulas orientativas: placa enterrada, R = 0,8 ρ/P (P, perímetro en m); pica vertical, R = ρ/L; conductor enterrado horizontalmente, R = 2 ρ/L (L, longitud en m; ρ, resistividad en Ω·m).

En instalaciones de utilización con centro de transformación, las masas y sus conductores de protección no se unen a la toma de tierra de las masas del centro de transformación; puede considerarse independencia cuando no exista canalización metálica que una ambas zonas, la distancia entre tomas sea al menos de 15 metros para terrenos de resistividad baja (<100 Ω·m) —calculándose por la fórmula reglamentaria con la resistividad y la corriente de defecto en terrenos muy mal conductores, con U = 1200 V para redes TT si el defecto en alta tensión se elimina en ≤5 s y 250 V en caso contrario— y el centro de transformación esté aislado o eléctricamente separado de los locales de utilización. La unión de ambas puestas a tierra sólo se permite si la resistencia de la toma única hace que la tensión de defecto (Vd = Id·Rt) sea menor que la tensión de contacto máxima admisible.

## Relacionado
- [[guia-bt-18-instalaciones-de-puesta-a-tierra]] — guía técnica de aplicación (no vinculante: prevalece la ITC-BT-18)
- [[itc-bt-18-instalaciones-de-puesta-a-tierra]]
- [[itc-bt-24-instalaciones-interiores-o-receptoras-proteccion-contra-los-contactos-directos-e-indirectos]]
- [[toma-de-tierra-edificios-viviendas]]
- [[reglament-electrotecnic-baixa-tensio]]
