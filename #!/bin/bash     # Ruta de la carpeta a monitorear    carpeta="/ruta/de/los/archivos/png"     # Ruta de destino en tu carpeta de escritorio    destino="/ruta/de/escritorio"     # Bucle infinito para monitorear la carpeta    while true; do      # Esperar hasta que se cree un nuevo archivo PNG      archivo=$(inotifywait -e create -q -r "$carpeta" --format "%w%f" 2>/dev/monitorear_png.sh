#!/bin/bash

   # Ruta de la carpeta a monitorear
   carpeta="/QR-Generator"

   # Ruta de destino en tu carpeta de escritorio
   destino="~/Desktop"

   # Bucle infinito para monitorear la carpeta
   while true; do
     # Esperar hasta que se cree un nuevo archivo PNG
     archivo=$(inotifywait -e create -q -r "$carpeta" --format "%w%f" 2>/dev/null)

     # Copiar el archivo PNG al destino
     cp "$archivo" "$destino"
   done
