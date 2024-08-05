import streamlit as st
import qrcode

filename = "qr_codes/qr_code.png"

def generar_qr_code(url, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

# Configuración de la página
st.set_page_config(page_title="Generador de QR", page_icon="🤍", layout="centered")

# Contenido de la aplicación
st.image("images/banner.jpg", use_column_width=True)
st.title("Generador de QR")
url = st.text_input("Introduce la URL de tu página")

if st.button("Generar QR"):
    generar_qr_code(url, filename)
    st.image(filename, use_column_width=True)
    with open(filename, "rb") as f:
        image_data = f.read()
    st.download_button(label="Descargar QR", data=image_data, file_name="qr_generated.png")
