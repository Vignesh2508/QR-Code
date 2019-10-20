import qrcode

qrc = qrcode.QRCode(version=1, box_size=10, border=5)

data = "https://www.youtube.com/"

qrc.add_data(data)

qrc.make(fit=True)

img = qrc.make_image(fill="black", back_color = "white")

img.save("1.png")