# QR-Generator

El código que mencionas genera un código QR a partir de una URL ingresada por el usuario y lo guarda en un archivo llamado "qr-saved.png". Aquí está el desglose del código:

1. Importa los módulos `os` y `qrcode` para trabajar con archivos y generar códigos QR, respectivamente.
2. Solicita al usuario que ingrese una URL utilizando la función `input()` y la asigna a la variable `url`.
3. Verifica si el archivo "qr-saved.png" no existe utilizando la función `os.path.exists()`. Si el archivo no existe, continúa con los siguientes pasos.
4. Genera un código QR utilizando la función `qrcode.make()` y pasa la URL como parámetro. El resultado se asigna a la variable `img`.
5. Guarda el código QR en un archivo llamado "qr-saved.png" utilizando el método `save()` de la variable `img`.

En resumen, este código verifica si el archivo "qr-saved.png" ya existe y, si no existe, genera un código QR a partir de una URL ingresada por el usuario y lo guarda en ese archivo.

# English Desciption

The code you mention generates a QR code from a URL entered by the user and saves it in a file called "qr-saved.png". Here is the breakdown of the code:

1. imports the `os` and `qrcode` modules for working with files and generating QR codes, respectively.
2. Prompts the user to enter a URL using the `input()` function and assigns it to the `url` variable.
Checks if the file "qr-saved.png" does not exist using the `os.path.exists()` function. If the file does not exist, continue with the following steps.
Generate a QR code using the `qrcode.make()` function and pass the URL as a parameter. The result is assigned to the `img` variable.
5. Save the QR code in a file named `qr-saved.png` using the `save()` method of the `img` variable.

In short, this code checks if the file `qr-saved.png` already exists and, if it does not, generates a QR code from a URL entered by the user and saves it to that file.

Translated with www.DeepL.com/Translator (free version)
