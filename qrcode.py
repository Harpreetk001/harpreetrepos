# Python script to generate QR code and save it as an image

import qrcode

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

if __name__ == "__main__":
    data = "https://example.com"  # Replace with your data
    filename = "qrcode.png"  # Replace with desired filename
    generate_qr_code(data, filename)
