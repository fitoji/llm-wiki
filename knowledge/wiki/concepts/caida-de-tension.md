---
title: Caída de tensión en baja tensión — límites, cálculo y compensación
type: concept
tags: [rebt, baja-tension, caidas-de-tension, secciones, itc-bt-19, itc-bt-25, guia-tecnica]
sources: [papers/2026-11-10-guia-rebt-anexo-2-calculos-de-caidas-de-tension.md, papers/2026-11-10-rebt-itc-bt-19-instalaciones-interiores-o-receptoras-prescripciones-generales.md, papers/2026-11-10-rebt-itc-bt-25-instalaciones-interiores-en-viviendas-numero-de-circuitos-y-caracteristicas.md, papers/2026-11-10-rebt-itc-bt-14-instalaciones-de-enlace-linea-general-de-alimentacion.md, papers/2026-11-10-rebt-itc-bt-15-instalaciones-de-enlace-derivaciones-individuales.md, papers/2026-11-10-guia-bt-25-instalaciones-interiores-en-viviendas-numero-de-circuitos-y-caracteristicas.md, papers/2026-11-10-guia-bt-19-instalaciones-interiores-o-receptoras-prescripciones-generales.md, papers/2026-11-10-guia-bt-14-linea-general-de-alimentacion.md, papers/2026-11-10-guia-bt-15-derivaciones-individuales.md]
created: 2026-11-13
updated: 2026-11-13
---

# Caída de tensión en baja tensión — límites, cálculo y compensación

La caída de tensión es uno de los tres criterios que, junto con el calentamiento y el cortocircuito, determinan la sección de los conductores en baja tensión. Este artículo integra los límites que fijan las ITC-BT-14, ITC-BT-15 e ITC-BT-19, el método de cálculo del [[guia-rebt-anexo-2-calculos-de-caidas-de-tension]], las tablas de longitudes máximas de la Guía-BT-25 y la regla de compensación entre la instalación interior y las derivaciones individuales. El detalle normativo y los ejemplos completos están en esos artículos; aquí se sintetiza el criterio transversal.

## Puntos clave

- La sección mínima normalizada debe satisfacer simultáneamente tres condiciones: intensidad máxima admisible (calentamiento, 70 °C termoplástico y 90 °C termoestable), caída de tensión y intensidad de cortocircuito (160 °C/250 °C en menos de 5 s). En baja tensión la caída de tensión suele ser el criterio determinante en líneas largas, por ejemplo en derivaciones individuales que alimentan los últimos pisos.
- Los límites de caída de tensión se fijan por tramos y por tipo de instalación (tabla 6 del Anexo 2; la LGA es siempre trifásica y los porcentajes se refieren a 400 V en trifásico o 230 V en monofásico):

| Parte de la instalación | Alimenta a | Caída máxima |
|---|---|---|
| LGA | Contadores totalmente concentrados | 0,5 % |
| LGA | Centralizaciones parciales de contadores | 1,0 % |
| Derivación individual | Suministro de un único usuario | 1,5 % |
| Derivación individual | Contadores totalmente concentrados | 1,0 % |
| Derivación individual | Centralizaciones parciales de contadores | 0,5 % |
| Circuitos interiores | Viviendas | 3 % |
| Circuitos interiores | Alumbrado que no sea viviendas | 3 % |
| Circuitos interiores | Fuerza que no sea viviendas | 5 % |

- Instalación industrial alimentada directamente en alta tensión con transformador de distribución propio: el origen de la instalación interior está en la salida del transformador y las caídas máximas son del 4,5 % para alumbrado y del 6,5 % para los demás usos.
- El cálculo se apoya en el circuito equivalente de línea corta (inferior a unos 50 km): ΔU = R·I·cos φ + X·I·sen φ. Hasta 120 mm² la contribución de la reactancia es despreciable y la sección se obtiene como S = c·ρ·P·L/ΔU (trifásico) o el doble en monofásico; el Anexo 2 detalla las fórmulas y las tablas de valores unitarios.
- La Guía-BT-25 publica la Tabla B de longitudes máximas de conductor para una caída del 3 %, 40 °C y cos φ = 1; sirve para dimensionar circuitos de vivienda sin repetir el cálculo.
- La caída de tensión se calcula considerando alimentados todos los aparatos susceptibles de funcionar simultáneamente y puede compensarse entre la instalación interior y las derivaciones individuales, de forma que la caída total sea inferior a la suma de los límites de ambas.

## Detalles

### Límites por tramos

Los límites proceden de la [[itc-bt-14-instalaciones-de-enlace-linea-general-de-alimentacion]] (LGA: 0,5 % con contadores totalmente centralizados y 1 % con centralizaciones parciales), la [[itc-bt-15-instalaciones-de-enlace-derivaciones-individuales]] (DI: 0,5 % con contadores concentrados en más de un lugar, 1 % con contadores totalmente concentrados y 1,5 % para suministros de un único usuario sin línea general de alimentación) y la [[itc-bt-19-instalaciones-interiores-o-receptoras-prescripciones-generales]] (3 % en viviendas; 3 % alumbrado y 5 % demás usos en otras instalaciones; 4,5 %/6,5 % en industrial alimentada directamente en alta tensión). El Anexo 2 los recopila en su tabla 6 con los valores equivalentes en voltios (por ejemplo, 0,5 % de 400 V = 2 V; 3 % de 230 V = 6,9 V). La ITC-BT-18 no fija límites de caída de tensión.

### Cómo calcularla

El Anexo 2 ofrece dos itinerarios. El simplificado admite la temperatura máxima del aislamiento y es el habitual en baja tensión; el detallado estima la temperatura real del conductor y puede permitir secciones normalizadas inferiores. En ambos, la sección se despeja de la caída admisible y después se comprueba que soporta la intensidad prevista según las condiciones de instalación (tablas de intensidades admisibles de la ITC-BT-19 y de la Guía-BT-14, con los factores de reducción por agrupación). Cuando la reactancia no es despreciable se usa la expresión completa; hasta 120 mm² se simplifica al término resistivo. La segunda iteración estima la temperatura real con T = T₀ + (T_máx − T₀)·(I/I_máx)² y re comprueba la caída; el Anexo 2 también expone el cálculo por valores unitarios e_u = e/(L·I) y sus tablas 4 y 5.

### Tablas de longitudes máximas

La Guía-BT-25, en el apartado 3, publica la Tabla B: longitud máxima del conductor en función de su sección y de la intensidad nominal del dispositivo de protección, para una caída del 3 %, una temperatura estimada de 40 °C y cos φ = 1 (1,5 mm²: 27 m a 10 A; 2,5 mm²: 45 m a 10 A y 28 m a 16 A; 4 mm²: 45 m a 16 A y 36 m a 20 A; 6 mm²: 53 m a 20 A y 43 m a 25 A). Sirve para acotar el trazado de los circuitos de vivienda sin calcular cada línea. El texto consolidado de la [[itc-bt-25-instalaciones-interiores-en-viviendas-numero-de-circuitos-y-caracteristicas]] fija el límite del 3 % y la regla de compensación, pero no incluye esa tabla: es una divergencia de tipo `[ampliacion]` respecto a la ITC. La aplicación práctica a los circuitos C1–C13 está en [[instalaciones-interiores-viviendas-bt]].

### Compensación entre instalación interior y derivaciones individuales

La ITC-BT-19 (2.2.2) y la ITC-BT-25 (apartado 3) admiten compensar la caída entre la instalación interior y las derivaciones individuales, de forma que la caída total sea inferior a la suma de los valores límite especificados para ambas, según el tipo de esquema utilizado. La Guía-BT-19 aclara que la compensación puede hacerse en ambos sentidos: si sobra sección en la derivación y estorba la conexión con los mecanismos, se recomienda aumentar la caída en la instalación interior y sobredimensionar la derivación; en viviendas pequeñas, la caída interior inferior al límite se compensa con la de la derivación. La Guía-BT-15 recomienda, en general, minimizar la caída en la derivación individual para limitar la sección de los conductores en las instalaciones interiores.

### Relación con los otros criterios de dimensionado

El calentamiento suele gobernar las líneas cortas y la caída de tensión las largas; el cortocircuito, determinante en alta y media tensión, apenas lo es en baja tensión. Los tres criterios se verifican sobre la misma sección normalizada, de modo que el dimensionado final es el mayor de los que impone cada criterio. El detalle del criterio de cortocircuito está en [[guia-rebt-anexo-3-calculo-de-corrientes-de-cortocircuito]] y el de conductores y ejecución en [[conductores-y-ejecucion-instalacion-interior]].

## Relacionado

- [[guia-rebt-anexo-2-calculos-de-caidas-de-tension]] — método de cálculo, fórmulas, valores unitarios y ejemplos
- [[itc-bt-19-instalaciones-interiores-o-receptoras-prescripciones-generales]] — límites de interiores y compensación
- [[itc-bt-25-instalaciones-interiores-en-viviendas-numero-de-circuitos-y-caracteristicas]] — 3 % en viviendas y cálculo al punto más alejado
- [[itc-bt-14-instalaciones-de-enlace-linea-general-de-alimentacion]] — límites de la LGA
- [[itc-bt-15-instalaciones-de-enlace-derivaciones-individuales]] — límites de la derivación individual
- [[instalaciones-interiores-viviendas-bt]] — aplicación a los circuitos C1–C13 y Tabla B
- [[guia-bt-19-instalaciones-interiores-o-receptoras-prescripciones-generales]] — compensación en ambos sentidos
- [[guia-bt-14-linea-general-de-alimentacion]] — guía de aplicación de la LGA
- [[guia-bt-15-derivaciones-individuales]] — guía de aplicación de la DI y tablas de sección
- [[conductores-y-ejecucion-instalacion-interior]] — conductores y condiciones de instalación
- [[reglament-electrotecnic-baixa-tensio]] — REBT, RD 842/2002
