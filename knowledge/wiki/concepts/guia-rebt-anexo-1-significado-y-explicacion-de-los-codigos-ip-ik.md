---
title: Guía REBT Anexo 1 — Significado y explicación de los códigos IP, IK (edición sep 03, rev 1)
type: concept
tags: [rebt, guia-tecnica, baja-tension, ip, ik]
sources: [papers/2026-11-10-guia-rebt-anexo-1-significado-y-explicacion-de-los-codigos-ip-ik.md]
created: 2026-11-10
updated: 2026-11-10
---

# Guía REBT Anexo 1 — Significado y explicación de los códigos IP, IK (edición sep 03, rev 1)

El Anexo 1 de las Guías Técnicas de Aplicación del REBT (edición sep 03, revisión 1) explica el sistema de clasificación por códigos IP e IK: qué garantiza cada cifra, qué norma respalda cada ensayo y cómo se marca el grado de protección de una envolvente. Es material de apoyo, no normativa: el REBT (RD 842/2002) y sus ITC-BT prevalecen sobre la guía.

## Puntos clave

- Dos sistemas con dos normas: el código IP (UNE 20324, equivalente a la EN 60529) recoge la protección frente al acceso a partes peligrosas, la penetración de cuerpos sólidos y la de agua; el código IK (UNE-EN 50102) recoge la protección frente a los impactos mecánicos exteriores.
- El IP se forma por dos cifras independientes tras las letras «IP»: la primera (0 a 6) protege a las personas y al equipo frente a cuerpos sólidos; la segunda (0 a 8) protege el interior frente al agua.
- Las letras opcionales A, B, C y D, tras las dos cifras, informan de la accesibilidad a partes peligrosas.

Primera cifra característica (personas y cuerpos sólidos):

| Cifra | Grado de protección | Objetos que no deben penetrar |
|---|---|---|
| 0 | No protegida | Sin protección particular |
| 1 | Sólidos de más de 50 mm | Diámetro superior a 50 mm |
| 2 | Sólidos de más de 12 mm | Diámetro superior a 12 mm |
| 3 | Sólidos de más de 2,5 mm | Diámetro superior a 2,5 mm |
| 4 | Sólidos de más de 1 mm | Diámetro superior a 1 mm |
| 5 | Contra la penetración de polvo | Polvo que no llegue a perjudicar el funcionamiento |
| 6 | Totalmente estanco al polvo | Ninguna entrada de polvo |

Segunda cifra característica (agua):

| Cifra | Grado de protección |
|---|---|
| 0 | No protegida |
| 1 | Caída vertical de gotas de agua |
| 2 | Gotas con inclinación máxima de 15º |
| 3 | Lluvia fina pulverizada (hasta 60º con la vertical) |
| 4 | Proyecciones de agua en todas direcciones |
| 5 | Chorros de agua con boquilla |
| 6 | Fuertes chorros de agua o mar gruesa |
| 7 | Efectos de la inmersión |
| 8 | Inmersión prolongada |

Letras adicionales:

| Letra | Accesibilidad a partes peligrosas que la envolvente impide |
|---|---|
| A | Una gran superficie del cuerpo humano, como la mano, pero no impide la penetración deliberada. Prueba: esfera de 50 mm |
| B | Dedos u objetos análogos de hasta 80 mm. Prueba: dedo de Φ12 mm y L = 80 mm |
| C | Herramientas, alambres, etc., de más de 2,5 mm. Prueba: varilla de Φ2,5 mm y L = 100 mm |
| D | Alambres o cintas de más de 1 mm. Prueba: varilla de Φ1 mm y L = 100 mm |

Grados IK (el número se escribe con dos cifras; la energía aumenta con el grado):

| Concepto | IK 00 | IK 01 | IK 02 | IK 03 | IK 04 | IK 05 | IK 06 | IK 07 | IK 08 | IK 09 | IK 10 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Energía (J) | — | 0,15 | 0,2 | 0,35 | 0,5 | 0,7 | 1 | 2 | 5 | 10 | 20 |
| Masa de la pieza de golpeo | — | 0,2 kg | 0,2 kg | 0,2 kg | 0,2 kg | 0,2 kg | 0,5 kg | 0,5 kg | 1,7 kg | 5 kg | 5 kg |
| Altura de caída | — | 70 mm | 100 mm | 175 mm | 250 mm | 350 mm | 200 mm | 400 mm | 295 mm | 200 mm | 400 mm |

- El ejemplo de la guía: IK 07 soporta el impacto de una pieza de poliamida o acero redondeada de 500 g caída desde 400 mm, en los puntos más débiles de la envolvente.

## Detalles

La definición de envolvente que usa el anexo procede del Vocabulario Electrotécnico Internacional (VEI 826-03-12) y la guía advierte que necesita aclaración: protege al material contra las influencias externas y en cualquier dirección y contra los contactos directos, e incluye toda tapa o accesorio que impida la penetración, salvo los que puedan quitarse sin herramienta o llave. La terminología de la ITC-BT-01 define la envolvente con un alcance equivalente.

Sobre el marcado: cuando una cifra característica no es necesaria o no ha sido ensayada, se sustituye por una «X» (IP2X indica protección frente a cuerpos sólidos, sin ensayo de penetración de agua). Si una envolvente ofrece dos grados según la posición de montaje, el fabricante debe indicarlo en sus instrucciones. El marcado habitual es el numérico, «IP 54», aunque las cifras pueden sustituirse por símbolos:

| Símbolo | Grado | Cifra que representa |
|---|---|---|
| Malla sin recuadro | IP5X | Primera |
| Malla con recuadro | IP6X | Primera |
| Una gota | IPX1 | Segunda |
| Una gota dentro de un cuadrado | IPX3 | Segunda |
| Una gota dentro de un triángulo | IPX4 | Segunda |
| Dos gotas, cada una dentro de un triángulo | IPX5 | Segunda |
| Dos gotas | IPX7 | Segunda |
| Dos gotas seguidas de la profundidad máxima de inmersión en metros | IPX8 | Segunda |

Los procedimientos de limpieza especializados no están cubiertos por los grados IP, y la guía remite a la CEI 60529 para que el fabricante informe de ellos; también admite la clasificación de envolventes vacías. En cuanto al IK, el grado se aplica a la envolvente entera salvo que alguna parte ofrezca otro, que debe indicarse en la documentación del fabricante.

## Divergencias con el REBT

- El anexo define el código IP por la UNE 20324 y el código IK por la UNE-EN 50102. La ITC-BT-02, en el listado consolidado del BOE, relaciona el código IP con la UNE-EN 60529 (ediciones 2018) y el código IK con la UNE-EN 62262 (2002; 2002/A1: 2022), que sustituye a la UNE-EN 50102:1996 y sus correcciones; la propia nota al pie 7 recuerda que «la referencia original en el texto reglamentario es UNE 20324». Prevalece la ITC-BT-02.

## Relacionado

- [[reglament-electrotecnic-baixa-tensio]]
- [[itc-bt-02-normas-de-referencia-en-el-reglamento-electrotecnico-para-baja-tension]]
- [[itc-bt-01-terminologia]]
- [[locales-banera-ducha-bt]]
