import qrcode

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_L,
                   box_size=20,
                   border=2)

qr.add_data("https://elcruzo.github.io/my-diary/")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("advanced.png")






# img = qrcode.make("Hello, my name is ElCruzo. Welcome!")
# img.save("mycode.png")