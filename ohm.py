import streamlit as st
import random

st.set_page_config(page_title="Praktikum Virtual Tak-Presisi Hukum Ohm", layout="centered")

st.title("Alat Ukur Tak Presisi - Hukum Ohm")
st.header("Amperemeter", divider=True)

# Slider input tegangan (V)
v = st.slider('Pilih Tegangan (V)', 0.0, 12.0, 0.0)
st.write('Tegangan (V):', v, 'Volt')

# Slider input resistor (R)
r = st.slider('Pilih Nilai Resistor (Ω)', 100, 1000, 371)
st.write('Resistor (R):', r, 'Ohm')

# Hitung arus (I) dengan ketidakpresisian
i = (v + random.random() - 0.5) / r
st.write('Arus (I):', round(i, 4), 'A atau', round(i*1000, 2), 'mA')

# Tambahkan penjelasan singkat
st.markdown("""
Simulasi ini menampilkan nilai arus berdasarkan Hukum Ohm (I = V/R), dengan komponen acak untuk
mensimulasikan ketidakpresisian alat ukur.
""")
