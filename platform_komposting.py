import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


# Membaca data panduan Takakura
panduan = pd.read_csv('panduan_takakura.csv')

# Menampilkan judul aplikasi
st.title("Panduan Pengolahan Sampah Organik dengan Metode Takakura")

# Menampilkan panduan langkah demi langkah
st.write("Ikuti langkah-langkah berikut untuk mengolah sampah organik menggunakan metode Takakura:")

for index, row in panduan.iterrows():
    st.write(f"**Langkah {row['langkah']}**: {row['deskripsi']}")

# Data suhu dan kelembaban dalam proses komposting
waktu = np.arange(0, 30, 1)  # 30 hari
suhu = 60 - 0.5 * waktu  # suhu turun selama 30 hari
kelembaban = 80 - 0.3 * waktu  # kelembaban turun selama 30 hari

# Membuat grafik
fig, ax1 = plt.subplots()

ax1.set_xlabel('Hari')
ax1.set_ylabel('Suhu (°C)', color='tab:red')
ax1.plot(waktu, suhu, color='tab:red', label='Suhu')
ax1.tick_params(axis='y', labelcolor='tab:red')

ax2 = ax1.twinx()
ax2.set_ylabel('Kelembaban (%)', color='tab:blue')
ax2.plot(waktu, kelembaban, color='tab:blue', label='Kelembaban')
ax2.tick_params(axis='y', labelcolor='tab:blue')

fig.tight_layout()
st.pyplot(fig)

# Input jenis sampah dari pengguna
jenis_sampah = st.selectbox("Pilih jenis sampah organik", ["Sayuran", "Buah", "Sisa Makanan"])

# Input lokasi atau kondisi lainnya
lokasi = st.selectbox("Pilih lokasi", ["Taman", "Dapur", "Luar Ruangan"])

# Memberikan rekomendasi berdasarkan input
if jenis_sampah == "Sayuran":
    st.write("Rekomendasi: Gunakan bahan kering (seperti daun kering) untuk mempercepat proses komposting.")
elif jenis_sampah == "Buah":
    st.write("Rekomendasi: Pastikan kelembaban tetap terjaga selama proses komposting.")
else:
    st.write("Rekomendasi: Campurkan dengan bahan kering untuk mengurangi bau dan mempercepat penguraian.")



