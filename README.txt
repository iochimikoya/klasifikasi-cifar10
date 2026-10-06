# Cara Menjalankan Aplikasi

## 1. Siapkan file model
Model CNN dilatih di Google Colab (Tugas Practicum 2). Untuk memakai model
tersebut di aplikasi ini:
1. Buka notebook Practicum 2 di Colab
2. Tambahkan cell baru di paling bawah, isi dengan:
   model.save('model_cifar10.h5')
3. Run cell tersebut, lalu download file model_cifar10.h5
4. Taruh file model_cifar10.h5 di folder yang sama dengan app.py

## 2. Install library yang dibutuhkan
pip install -r requirements.txt

## 3. Jalankan aplikasi
streamlit run app.py

Aplikasi akan terbuka di browser (biasanya http://localhost:8501).

## 4. Cara pakai
1. Klik "Browse files" lalu pilih gambar (jpg/png)
2. Klik tombol "Prediksi"
3. Hasil prediksi dan tingkat keyakinannya akan muncul di bawah gambar

## 5. Deploy (opsional, sesuai pilihan di soal)
- Streamlit Cloud: upload folder ini ke GitHub, lalu hubungkan di share.streamlit.io
- Hugging Face Spaces: buat Space baru tipe Streamlit, upload app.py,
  requirements.txt, dan model_cifar10.h5
- Lokal: cukup jalankan streamlit run app.py di laptop sendiri

## Catatan
- Gambar otomatis diubah ke ukuran 32x32 sebelum diprediksi,
  karena itu ukuran input yang dipakai saat training model.
- Nilai pixel dibagi 255 supaya rentangnya 0-1, sama seperti
  preprocessing saat training.
