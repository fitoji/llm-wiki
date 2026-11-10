---
title: Instalaciones a muy baja tensión
type: concept
tags: [rebt, baja-tension, itc-bt-36, mbts, mbtp, transformador-seguridad]
sources: [papers/2026-11-10-rebt-itc-bt-36-instalaciones-a-muy-baja-tension.md]
created: 2026-11-10
updated: 2026-11-10
---

# Instalaciones a muy baja tensión

La ITC-BT-36 del REBT regula las instalaciones a muy baja tensión, que se dividen en tres tipos: Muy Baja Tensión de Seguridad (MBTS), Muy Baja Tensión de Protección (MBTP) y Muy Baja Tensión Funcional (MBTF). Todas ellas tienen como límite común una tensión nominal no superior a 50 V en corriente alterna o 75 V en corriente continua.

## Puntos clave

- La tensión nominal de MBTS, MBTP y MBTF no excede de **50 V en c.a. o 75 V en c.c.**
- **MBTS**: fuente con aislamiento de protección (transformador de seguridad según UNE-EN 60742 o UNE-EN 61558-2-4); circuitos con aislamiento de protección sin conexión a tierra y masas no conectadas intencionadamente a tierra ni a conductor de protección.
- **MBTP**: igual que MBTS, pero por razones funcionales los circuitos y/o masas están conectados a tierra o a un conductor de protección; la puesta a tierra puede hacerse conectando al conductor de protección del circuito primario.
- **MBTF**: no cumple los requisitos de MBTS ni MBTP (fuente sin aislamiento de protección o circuitos sin aislamiento de protección); su protección contra choques eléctricos se hace conforme a la [[itc-bt-24-instalaciones-interiores-o-receptoras-proteccion-contra-los-contactos-directos-e-indirectos]].
- La separación de protección entre circuitos MBTS/MBTP y cualquier otro se logra por separación física de los conductores, cubierta no metálica sobre el aislamiento principal, pantalla o vaina metálica puesta a tierra, o aislamiento para la tensión más alta en cables multiconductor.
- Las bases de toma de corriente deben impedir la introducción de conectores de otras tensiones; las bases MBTS no llevan contacto de protección, las MBTP sí pueden llevarlo. Un circuito MBTF se considera siempre como circuito de tensión diferente.
- No es necesario seguir la identificación de conductores de la [[itc-bt-19-instalaciones-interiores-o-receptoras-prescripciones-generales]] ni las distancias al suelo y separaciones de la [[itc-bt-06-redes-aereas-para-distribucion-en-baja-tension]].
- Cables enterrados entre dos capas de arena o tierra fina cribada de 10 a 15 cm de espesor; caída de tensión en alumbrado no superior al 5 %.
- Protection contra contactos directos exigida a partir de 25 V c.a. o 60 V c.c. sin ondulación (IP2X / IP XXB o aislamiento que soporte 500 V durante un minuto); la c.c. sin ondulación es la de ondulación ≤ 10 % del valor eficaz.

## Detalles

La instrucción distingue los tres tipos por la presencia de aislamiento de protección y la conexión a tierra. MBTS y MBTP comparten fuente (transformador de seguridad o fuente equivalente con separación equivalente, como un motor-generador), fuente electroquímica (pilas o acumuladores), otras fuentes independientes como el grupo electrógeno, o determinados dispositivos electrónicos en los que, en caso de primer defecto, la tensión de salida no supera los valores de muy baja tensión. Cuando la corriente de cortocircuito en los bornes del circuito de utilización es inferior a la intensidad admisible de sus conductores, no se requiere protección contra sobreintensidades en el origen.

En MBTS, las partes activas no deben conectarse a tierra ni a partes activas o conductores de protección de circuitos diferentes. Las masas tampoco, salvo la excepción para equipos con conexiones francas a elementos conductores cuando se asegura que éstos no alcanzan un potencial superior a 50 V c.a. o 75 V c.c. Si masas MBTS pueden ponerse en contacto con masas de otros circuitos, la protección deja de basarse exclusivamente en la medida MBTS y pasa a regirse por las medidas de esas masas.

Para tensiones superiores a 25 V c.a. o 60 V c.c. sin ondulación, la protección contra contactos directos se garantiza por barreras o envolventes con grado IP2X o IP XXB, o por un aislamiento que soporte 500 V durante un minuto. Por debajo de esos valores no se requiere protección, salvo determinadas condiciones de influencias externas.

En MBTP la protección contra contactos directos exige los mismos grados de protección, pero no es necesaria para equipos dentro de un edificio donde las masas y elementos conductores accesibles están conectados a la misma toma de tierra, si la tensión nominal no supera 25 V eficaces en c.a. o 60 V en c.c. sin ondulación (solo emplazamientos secos, sin contactos francos previstos), o 6 V eficaces en c.a. o 15 V en c.c. sin ondulación en los demás casos.

## Relacionado

- [[reglament-electrotecnic-baixa-tensio]]
- [[itc-bt-24-instalaciones-interiores-o-receptoras-proteccion-contra-los-contactos-directos-e-indirectos]]
- [[itc-bt-19-instalaciones-interiores-o-receptoras-prescripciones-generales]]
- [[itc-bt-06-redes-aereas-para-distribucion-en-baja-tension]]
