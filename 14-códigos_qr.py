import qrcode

# Función para generar código QR
def generar_qr(texto, nombre_archivo="codigo_qr.png"):
    qr = qrcode.QRCode(
        version=1,  # Tamaño del código QR
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Nivel de corrección
        box_size=10,  # Tamaño de cada cuadro
        border=4  # Bordes alrededor del código QR
    )
    qr.add_data(texto)  # Agregar datos al código QR
    qr.make(fit=True)

    # Crear imagen del código QR
    imagen = qr.make_image(fill="black", back_color="white")
    imagen.save(nombre_archivo)
    print(f"✅ Código QR guardado como {nombre_archivo}")

# Prueba del generador
texto_qr = input("Ingresa el texto o enlace para el código QR: ")
generar_qr(texto_qr)
