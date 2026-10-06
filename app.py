# Aplikasi Klasifikasi Gambar CIFAR-10
# Tugas Kelompok 2 - Artificial Intelligence (Session 21)
# Kelompok: Group-7

import streamlit as st
import numpy as np
from PIL import Image
from tensorflow import keras

# daftar nama kelas sesuai dataset CIFAR-10
class_names = ['pesawat', 'mobil', 'burung', 'kucing', 'rusa',
               'anjing', 'katak', 'kuda', 'kapal', 'truk']

st.title("Klasifikasi Gambar CIFAR-10")
st.write("Upload sebuah gambar, lalu klik tombol Prediksi untuk melihat hasilnya.")

# load model yang sudah dilatih (file harus sejajar dengan app.py)
model = keras.models.load_model('model_cifar10.h5')

# bagian upload gambar
uploaded_file = st.file_uploader("Pilih gambar...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Gambar yang diupload")

    if st.button("Prediksi"):
        # ubah ukuran gambar jadi 32x32 supaya sesuai input model
        img = image.resize((32, 32))
        img_array = np.array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)

        # prediksi
        hasil = model.predict(img_array)
        index = np.argmax(hasil)
        confidence = float(np.max(hasil)) * 100

        st.write("Hasil prediksi:", class_names[index])
        st.write("Tingkat keyakinan:", round(confidence, 2), "%")
