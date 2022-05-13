# Final Project 2 - Logistic Regression and SVM

### Kelompok 01 - Introduction to Python for Data Science (Kampus Merdeka Batch 2)
1. Taufik Aji Putra<br>
2. M. Ihwanul Iqbal

# Project Overview
Dataset yang digunakan pada projek ini adalah dataset publik yang tersedia diwebsite kaggle, untuk mendapatkan dataset dapat ditemukan melalui link <a href="https://www.kaggle.com/jsphyg/weather-dataset-rattle-package"><b> klik disini</b></a>.  Dataset ini memiliki 23 atribut yang berisi informasi mengenai record 145460 data hujan harian selama 10 tahun di Australia. Tujuan utama dari penelitian ini adalah untuk memprediksi cuaca apakah hari selanjutnya hujan atau tidak dengan mengimplementasikan analisa prediction menggunakan algoritma Logistic Regression dan Support Vector Machine (SVM). Sebelum melakukan modeling perlu dilakukan processing data agar model prediksi yang dihasilkan memiliki tingkat akurasi yang optimal.

#### Final Project 2 ini dibuat guna mengevaluasi konsep Regression sebagai berikut:
* Mampu memahami konsep Classification dengan Logistic Regression dan SVM
* Mampu mempersiapkan data untuk digunakan dalam model  Logistic Regression dan SVM
* Mampu mengimplementasikan  Logistic Regression dan SVM untuk membuat prediksi

#### Attribute Information:
- Date - tanggal hari itu
- Location - lokasi, nama kota di Australia
- MinTemp - temperatur terendah hari itu dalam celcius
- MaxTemp - temperatur tertinggi hari itu dalam celcius
- Rainfall - jumlah curah hujan hari itu dalam mm
- Evaporation - jumlah evaporasi dalam mm dari Class A pan selama 24 jam
- sebelum jam 9 pagi hari itu
- Sunshine - jumlah jam hari itu cerah dengan cahaya matahari
- WindGustDir - arah kecepatan angin yang paling tinggi selama 24 jam sebelum
- jam 12 malam hari itu
- WindGustSpeed - kecepatan angin yang paling tinggi dalam km/jam selama 24
- jam sebelum jam 12 malam hari itu
- WindDir9am - arah angin jam 9 pagi
- WindDir3pm - arah angin jam 3 sore
- WindSpeed9am - kecepatan angin jam 9 pagi dalam km/jam dihitung dari
- rata-rata kecepatan angin 10 menit sebelum jam 3 sore
- WindSpeed3pm - kecepatan angin jam 3 sore dalam km/jam dihitung dari
- rata-rata kecepatan angin 10 menit sebelum jam 3 sore
- Humidity9am - humiditas jam 9 pagi dalam persen
- Humidity3pm - humiditas jam 3 sore dalam persen
- Pressure9am - tekanan udara jam 9 pagi dalam hpa
- Pressure3pm - tekanan udara jam 3 sore dalam hpa
- Cloud9am - persentase langit yang tertutup awan jam 9 pagi. dihitung dalam
- oktas, unit 1⁄8, menghitung berapa unit 1⁄8 dari langit yang tertutup awan. Jika 0,
- langit cerah, jika 8, langit sepenuhnya tertutup awan.
- Cloud3pm - persentase langit yang tertutup awan jam 3 sore
- Temp9am - temperatur jam 9 pagi dalam celcius
- Temp3pm - temperatur jam 3 sore dalam celcius
- RainToday - apakah hari ini hujan: jika curah hujan 24 jam sebelum jam 9 pagi
- melebihi 1mm, maka nilai ini adalah 1, jika tidak nilai nya 0
- RainTomorrow - variable yang mau di prediksi
