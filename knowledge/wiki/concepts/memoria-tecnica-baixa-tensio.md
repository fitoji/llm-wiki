---
title: Memoria técnica de baja tensión (modelo ELEC-3)
type: concept
tags: [rebt, baixa-tensio, catalunya, formularis, memoria-tecnica]
sources: [papers/2026-11-10-memoria-tecnica-elc3.md, papers/2026-11-10-rebt-itc-bt-20-instalaciones-interiores-o-receptoras-sistemas-de-instalacion.md, papers/2026-11-10-rebt-itc-bt-21-instalaciones-interiores-o-receptoras-tubos-y-canales-protectoras.md, papers/2026-11-10-rebt-itc-bt-07-redes-subterraneas-para-distribucion-en-baja-tension.md]
created: 2026-11-10
updated: 2026-11-17
---

# Memoria técnica de baja tensión (modelo ELEC-3)

Documento técnico que acompaña a determinadas instalaciones. Formulario G146NSIN-157-00.

## Puntos clave
- Recoge titular, uso, emplazamiento, localidad, ampliación, empresa distribuidora, características del edificio y superficie del local.
- Datos de la instalación: potencia máxima admisible (máxima que puede soportar el conjunto de la instalación), potencia a instalar, tensión, intensidad del interruptor general, sensibilidad y circuitos del interruptor diferencial, sección de la derivación individual y resistencia de tierra de protección.
- **Graella de derivaciones** (estructura más abajo): carga simultánea, potencia, cos ϕ, intensidad, sección por fase, longitud, momento eléctrico, caída de tensión, características del conductor, tipo de canalizaciones, aislamiento de la instalación y secciones de neutro y de protección.
- Observaciones sobre el grado de protección de la aparamenta y receptores en locales especiales.

## Estructura de la graella

**Filas.** Una fila `Derivació individual (A — B)` seguida de las filas `DERIVACIONS`, rotuladas por tramos: `C — D`, `E — F`, `G — H`, `I — J`, `K — L`, `M — N`, …

**Columnas** (cabeceras literales del formulario):

| Columna | Subcolumnas |
|---|---|
| `Càrrega simultàn. (%)` | — |
| `Potència kW.` | — |
| `cos ϕ` | — |
| `Intens. A` | — |
| `Secció per fase mm2` | — |
| `Long. m` | — |
| `Moment elec. kW. · m` | — |
| `Caiguda de tensió` | `parcial (%)`, `total (%)` |
| `Caract. conduct.` | `TIPUS`, `tensió nominal d'aïllam.` |
| `Tipus de canalitzacions` | `sense tub protector (sistema)`, `sota tub: ∅ en mm.` (`encastat` / `sense encas.`), `conduct. enterrat. prof. m.` |
| `Aïllam. Instal·l. kΩ` | — |
| `Conduc. Neutre mm2` | — |
| `Conduc. Protec. mm2` | — |

### Las cuatro columnas de `Tipus de canalitzacions`

| # | Cabecera literal | Qué se escribe | Fuente REBT |
|---|---|---|---|
| 1 | `sense tub protector (sistema)` | el **nombre** del sistema de instalación | [[itc-bt-20-instalaciones-interiores-o-receptoras-sistemas-de-instalacion]], apartado 2.2 |
| 2 | `sota tub: ∅ en mm.` → `encastat` | **Ø exterior del tubo en mm**, montaje empotrado | [[itc-bt-21-instalaciones-interiores-o-receptoras-tubos-y-canales-protectoras]], **Tabla 5** |
| 3 | `sota tub: ∅ en mm.` → `sense encas.` | **Ø exterior del tubo en mm**, montaje superficial | [[itc-bt-21-instalaciones-interiores-o-receptoras-tubos-y-canales-protectoras]], **Tabla 2** |
| 4 | `conduct. enterrat. prof. m.` | **profundidad de enterramiento en m** | [[itc-bt-07-redes-subterraneas-para-distribucion-en-baja-tension]]: 0,60 m en acera, 0,80 m en calzada |

Dos avisos:

- **El orden importa:** `encastat` va a la izquierda y `sense encas.` a la derecha. Intercambiados, los diámetros quedan cambiados (6 mm² con 3 conductores: empotrado 25 mm, superficial 20 mm).
- **La columna 1** admite cualquiera de los sistemas de la ITC-BT-20 que **no** llevan tubo protector: fijado directamente a pared (2.2.2), empotrado directamente en estructura (2.2.4), aéreo (2.2.5), hueco de la construcción (2.2.6), canal protectora (2.2.7), moldura (2.2.8), bandeja (2.2.9) y canalización prefabricada (2.2.10). Los sistemas que **no** caen aquí son el 2.2.1 (bajo tubo → columnas 2 y 3) y el 2.2.3 (enterrado → columna 4).

## Detalles
Se exige para las instalaciones que figuran en la lista de clase P1 (ver [[classificacio-p1-p2]]). La firma del instalador y el sello de la empresa instaladora autorizada cierran el documento.

## Relacionado
- [[reglament-electrotecnic-baixa-tensio]]
- [[certificat-installacio-electrica-bt]]
- [[classificacio-p1-p2]]
- [[itc-bt-20-instalaciones-interiores-o-receptoras-sistemas-de-instalacion]] — sistemas de instalación (columna 1)
- [[itc-bt-21-instalaciones-interiores-o-receptoras-tubos-y-canales-protectoras]] — diámetros de tubo (columnas 2 y 3)
- [[itc-bt-07-redes-subterraneas-para-distribucion-en-baja-tension]] — profundidad de enterramiento (columna 4)
