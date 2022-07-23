# Final Project 4 - Clustering

### Kelompok 03 - Introduction to Python for Data Science (Kampus Merdeka Batch 2)
1. Taufik Aji Putra<br>
2. Ari Sandy Kurniawan<br>
3. Muhammad Rizaldi

# Project Overview
Dataset yang digunakan pada projek ini adalah dataset publik yang tersedia di website kaggle, <a href="https://www.kaggle.com/arjunbhasin2013/ccdata"><b> klik disini</b></a>. Dataset ini berisi perilaku belanja dan data tidak berlabel yang berkaitan dengan transaksi kartu kredit. Tujuan utama dari penelitian ini adalah untuk menunjukkan segmentasi pelanggan yang paling sesuai dengan dataset ini dengan mengimplementasikan analisa clustering.Algoritma dan metode yang digunakan pada projek ini yaitu algoritma K-Means Clustering, pemilihan algoritma K-means clustering dikarenakan algoritma tersebut lebih efisien dalam menangani dataset yang besar, algoritma sederhana yang mudah untuk dimengerti dan diterapkan. Selain K-means, terdapat teknik lain yang akan digunakan yaitu Principal Component Analysis (PCA) sebagai reduction dimension dataset dengan mengidentifikasi pola untuk mengurangi dimensi dataset. Penggunaan metode PCA juga dapat membantu mengoptimalkan hasil cluster dari K-means clustering dengan mendeteksi cluster tambahan dibandingkan dengan jumlah optimal cluster pada K-means tanpa menggunakan PCA. Dataset ini memiliki dimensi yang tinggi dan variabel-variabel yang berkorelasi. Data ini berisi transaksi pengguna kartu kredit sebanyak 8950 transaksi selama 6 bulan, dataset kartu kredit ini memiliki 18 atribut. Berikut deskripsi dari dataset ini, yaitu :

#### Attribute Information:

- CUSTID - Identification of Credit Card holder (Categorical)
- BALANCE - Balance amount left in their account to make purchases (
- BALANCEFREQUENCY - How frequently the Balance is updated, score between 0 and 1 (1 = frequently updated, 0 = not frequently updated)
- PURCHASES - Amount of purchases made from account
- ONEOFFPURCHASES - Maximum purchase amount done in one-go
- INSTALLMENTSPURCHASES - Amount of purchase done in installment
- CASHADVANCE - Cash in advance given by the user
- PURCHASESFREQUENCY - How frequently the Purchases are being made, score between 0 and 1 (1 = frequently purchased, 0 = not frequently purchased)
- ONEOFFPURCHASESFREQUENCY - How frequently Purchases are happening in one-go (1 = frequently purchased, 0 = not frequently purchased)
- PURCHASESINSTALLMENTSFREQUENCY - How frequently purchases in installments are being done (1 = frequently done, 0 = not frequently done)
- CASHADVANCEFREQUENCY - How frequently the cash in advance being paid
- CASHADVANCETRX - Number of Transactions made with "Cash in Advance"
- PURCHASESTRX - Number of purchase transactions made
- CREDITLIMIT - Limit of Credit Card for user
- PAYMENTS - Amount of Payment done by user
- MINIMUM_PAYMENTS - Minimum amount of payments made by user
- PRCFULLPAYMENT - Percent of full payment paid by user
- TENURE - Tenure of credit card service for user

#### Link Heroku: https://h8-model-fp4-03.herokuapp.com/
