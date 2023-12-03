import qrcode


def main():
    print("Ссылка для qr: ")
    href = input()

    print("Имя для файла: ")
    fileName = input()

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(href)
    qr.make(fit=True)

    img = qr.make_image(fill_color="red", back_color="black")
    img.save(f'./output/{fileName}.png')



if __name__ == "__main__":
    main()
