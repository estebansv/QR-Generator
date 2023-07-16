import qrcode, os

url = input("Digite la url o el texto a convertir a QR:\n")
filename = "qr-img.png"
counter = 1
while os.path.exists(filename):
    filename = f"qr-img_{counter}.png"
    counter += 1
img = qrcode.make(url)
img.save(filename)

