import streamlit as st

# Judul halaman
st.title("Halo dari Streamlit Community Cloud!")

# Paragraf penjelasan
st.write("""
Selamat datang di aplikasi Streamlit-mu yang sudah ter-deploy di Community Cloud.
Kamu bisa menambahkan widget, grafik, dan interaksi di sini.
""")

# Contoh widget sederhana
name = st.text_input("Siapa namamu?")
if name:
    st.success(f"Halo, {name}! 👋")
