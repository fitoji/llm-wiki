---
description: Guarda una fuente nueva (URL o archivo) en knowledge/raw/
---

Guarda la fuente indicada en `knowledge/raw/` con su frontmatter. Fuente: $ARGUMENTS

## Pasos

1. Decide el tipo:
   - Vídeo de YouTube -> `knowledge/raw/transcripts/`
   - Artículo o página web -> `knowledge/raw/articles/`
   - Paper o PDF -> `knowledge/raw/papers/`

2. Obtén el contenido:
   - URL de artículo: descarga la página y conviértela a markdown limpio (sin menús ni publicidad).
   - URL de YouTube: obtén la transcripción. Si hay `yt-dlp` instalado, usa
     `yt-dlp --skip-download --write-auto-subs --sub-langs "es,en" --convert-subs srt -o "/tmp/%(id)s" URL`
     y limpia los tiempos y duplicados del subtítulo para dejar texto continuo.
   - Ruta de archivo local: léelo y conviértelo a markdown.
   Si no puedes obtener el contenido, dilo claramente y pide al usuario que lo pegue o lo guarde manualmente. No inventes contenido.

3. Guarda el archivo con nombre `AAAA-MM-DD-titulo-corto.md` (minúsculas, guiones, sin acentos), con este frontmatter:

```
---
title: Título de la fuente
source: URL o ruta original
author: Autor o canal (si se conoce)
date: fecha de publicación (si se conoce) o fecha de hoy
tags: []
compiled: false
---
```

4. Confirma con la ruta del archivo creado y sugiere ejecutar `/wiki-compile`.
