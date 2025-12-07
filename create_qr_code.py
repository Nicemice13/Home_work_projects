import qrcode
import os


# Создание QR кода резюме. Для проекта нужна библиотека pillow и qrcode.
# Виртуальное окружение my_project_venv. Запуск создания QRcode происходет
# через команду в терминале "python Create_QRcode.py"


data = ("link") # Изменить переменную на ссылку

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_M,
    box_size=10,
    border=4,
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(
    fill_color="black",
    black_color="white"
)
img.show()

img.save("qr_code_CV.png")
os.system("eog qr_code.png")

print("✅ QR-код успешно создан!")
