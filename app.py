import qrcode, os

url = input("Digite la url o el texto a convertir a QR:\n")
filename = "qr-img.png"
counter = 1
while os.path.exists(filename):
    filename = f"qr-img_{counter}.png"
    counter += 1
img = qrcode.make(url)
img.save(filename)
 

print(f"Se ha generado el archivo {filename} en la siguiente ruta:")
print(os.path.abspath(filename))

os.system(f"open {filename}")
