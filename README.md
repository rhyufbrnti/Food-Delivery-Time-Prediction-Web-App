![Tampilan Aplikasi](Screenshot%202025-10-06%20203203.png)

# Food Delivery Time Prediction Web App

Aplikasi berbasis web untuk **analisis dan prediksi waktu pengiriman makanan** menggunakan metode **Multiple Linear Regression (Regresi Linear Berganda)**.  

---

## 📌 Latar Belakang
Latar belakang pembuatan web app ini adalah untuk memenuhi tugas mata kuliah *Praktikum Machine Learning*.  
Pada tugas ini, saya mengimplementasikan metode regresi linear berganda (*multiple linear regression*) untuk memprediksi lama waktu pengiriman makanan berdasarkan beberapa faktor yang memengaruhinya.  

---

## 🎯 Tujuan
- Mengimplementasikan algoritma regresi linear berganda dalam kasus nyata.  
- Memprediksi lama waktu pengiriman makanan berdasarkan faktor-faktor tertentu.  
- Menyediakan aplikasi sederhana berbasis web yang dapat digunakan untuk memasukkan data dan mendapatkan prediksi secara langsung.  

---

## ✨ Fitur Utama
- Input variabel faktor yang memengaruhi pengiriman.  
- Prediksi lama waktu pengiriman makanan.  
- Tampilan hasil analisis dalam bentuk yang sederhana dan mudah dipahami.  

---

## 🛠️ Teknologi yang Digunakan
- Python 3.x
- VSCode
- Railway
- Flask (Web Framework)
- Pandas (Data Processing)
- Matplotlib & Seaborn (Data Visualization)
- Statsmodels (Statistical Modeling - Multiple Linear Regression)
- Joblib (Model Serialization)
- io & base64 (Image Encoding untuk menampilkan grafik di web)


---

## 📊 Dataset
Dataset yang digunakan dalam project ini adalah **Food_Delivery_Times.csv**, yang berisi data lama waktu pengiriman makanan serta faktor-faktor yang memengaruhinya.  
Dataset ini digunakan untuk melatih model regresi linear berganda.  

---

## 🔬 Model Machine Learning

Model **Multiple Linear Regression** yang digunakan pada aplikasi ini dikembangkan terlebih dahulu di repository terpisah:  
👉 [Multiple-Linear-Regression](https://github.com/rhyufbrnti/Multiple-Linear-Regression)

Repository tersebut berisi:
- Notebook Jupyter untuk eksplorasi data dan analisis faktor-faktor yang memengaruhi waktu pengiriman makanan.
- Proses pembuatan dan evaluasi model regresi linear berganda.
- Dataset yang digunakan untuk pelatihan model.

Pada repository ini (**Food-Delivery-Time-Prediction-Web-App**), model hasil pelatihan tersebut diintegrasikan dengan **Flask** sehingga dapat digunakan secara interaktif oleh pengguna melalui antarmuka web.


---

## 🚀 Cara Instalasi & Menjalankan Aplikasi

1. Clone repository ini:
   ```bash
   git clone https://github.com/rhyufbrnti/Food-Delivery-Time-Prediction-Web-App.git
   cd Food-Delivery-Time-Prediction-Web-App
