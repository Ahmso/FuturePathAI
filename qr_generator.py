import qrcode


def generate_qr(text):

    qr = qrcode.make(text)

    file_name = "student_qr.png"

    qr.save(file_name)

    return file_name