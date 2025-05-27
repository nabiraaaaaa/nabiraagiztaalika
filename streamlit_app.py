import streamlit as st

st.title("🫧 informatika")
st.write(
    "latihan informatika bersama pak Hendri."
)
st.image("IMG_4658.jpeg", width=200)



st.title("Aplikasi Sederhana ")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah Angka:", value=0, step=1)

if (angka % 2) == 0:
    st.writer(f"{angka} adalah Bilangan Genap")
else:
    st.write(f"{angka} adalah Bilangan Ganjil")
