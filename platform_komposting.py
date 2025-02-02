import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Membaca file CSV
panduan = pd.read_csv('panduan_takakura.csv')

# Gambar untuk mempercantik tampilan
st.image("https://desabanjarejo.gunungkidulkab.go.id/assets/files/artikel/sedang_1594734509Kompos%20Takakura.jpg", caption="Metode Takakura", use_column_width=True)

# Judul aplikasi
st.title("🌱 **Panduan Pengolahan Sampah Organik dengan Metode Takakura** 🌿")

# Subjudul
st.subheader("Ikuti langkah-langkah berikut untuk mengolah sampah organik menggunakan metode Takakura:")

# Menampilkan panduan langkah demi langkah
for index, row in panduan.iterrows():
    st.markdown(f"**Langkah {row['langkah']}**: {row['deskripsi']}")

# Menambahkan grafik untuk visualisasi proses komposting
st.subheader("📈 Proses Komposting (Perubahan Suhu dan Kelembaban)")

waktu = np.arange(0, 30, 1)  # 30 hari
suhu = 60 - 0.5 * waktu  # suhu turun selama 30 hari
kelembaban = 80 - 0.3 * waktu  # kelembaban turun selama 30 hari

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

# Menambahkan kolom untuk rekomendasi interaktif
st.subheader("🌿 Rekomendasi Pengolahan Sampah Organik")

# Pilihan interaktif untuk input pengguna
jenis_sampah = st.selectbox("Pilih jenis sampah organik", ["Sayuran", "Buah", "Sisa Makanan"])

if jenis_sampah == "Sayuran":
    st.write("Rekomendasi: Gunakan bahan kering (seperti daun kering) untuk mempercepat proses komposting.")
elif jenis_sampah == "Buah":
    st.write("Rekomendasi: Pastikan kelembaban tetap terjaga selama proses komposting.")
else:
    st.write("Rekomendasi: Campurkan dengan bahan kering untuk mengurangi bau dan mempercepat penguraian.")

# Menggunakan kolom untuk membagi tampilan
col1, col2 = st.columns(2)

with col1:
    st.image("https://via.placeholder.com/400x400?text=Komposting", caption="Proses Komposting", use_column_width=True)

with col2:
    st.image("https://via.placeholder.com/400x400?text=Kompos+Jadi", caption="Kompos Jadi", use_column_width=True)

# Footer dengan kontak atau informasi lebih lanjut
st.markdown("---")
st.markdown("**Untuk informasi lebih lanjut, hubungi kami di**: [email@example.com](mailto:email@example.com)")

