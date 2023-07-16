# QR-Generator

El código que mencionas genera un código QR a partir de una URL ingresada por el usuario y lo guarda en un archivo llamado "qr-saved.png". Aquí está el desglose del código:

1. Importa los módulos `os` y `qrcode` para trabajar con archivos y generar códigos QR, respectivamente.
2. Solicita al usuario que ingrese una URL utilizando la función `input()` y la asigna a la variable `url`.
3. Verifica si el archivo "qr-saved.png" no existe utilizando la función `os.path.exists()`. Si el archivo no existe, continúa con los siguientes pasos.
4. Genera un código QR utilizando la función `qrcode.make()` y pasa la URL como parámetro. El resultado se asigna a la variable `img`.
5. Guarda el código QR en un archivo llamado "qr-saved.png" utilizando el método `save()` de la variable `img`.

En resumen, este código verifica si el archivo "qr-saved.png" ya existe y, si no existe, genera un código QR a partir de una URL ingresada por el usuario y lo guarda en ese archivo.
