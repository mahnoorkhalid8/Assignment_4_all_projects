import qrcode

data = "Don't forget to subscribe"
qr = qrcode.QRCode(version = 1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
qr_img = qr.make_image(fill_color="black", back_color="white")
qr_img.save("C:/Users/SEVEN86 COMPUTES/OneDrive/Desktop/Assignment 4/PROJECTS/main_projects/project_10_qr_code/main.png")
