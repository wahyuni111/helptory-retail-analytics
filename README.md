# HELPTORY – Smart Retail Inventory Analytics
## Deskripsi Aplikasi
HELPTORY (Helping Inventory) adalah aplikasi analisis inventori dan penjualan retail berbasis Python dan Streamlit yang dirancang untuk membantu pemilik toko dalam memantau stok produk, menganalisis performa penjualan, mengidentifikasi produk yang perlu dilakukan restock, serta melakukan segmentasi produk berdasarkan pola penjualannya menggunakan Machine Learning.
Aplikasi ini mengintegrasikan analisis data penjualan, manajemen inventori, dan algoritma K-Means Clustering untuk mendukung pengambilan keputusan yang lebih cepat dan berbasis data.

## Tujuan Aplikasi : 
- Membantu admin toko memonitor kondisi stok produk.
- Mengidentifikasi produk yang perlu dilakukan restock.
- Menampilkan produk dengan performa penjualan tertinggi.
- Mengelompokkan produk berdasarkan pola penjualan menggunakan Machine Learning.

## Fitur Utama 
1. Dashboard
   ### Product Category Distribution
   Menampilkan distribusi jumlah transaksi berdasarkan kategori produk dalam bentuk pie chart.
   ### Top Fast Moving Products
   Menampilkan 10 produk dengan total penjualan tertinggi.
   ### Daily Transaction Trend
   Menampilkan tren transaksi harian berdasarkan total nilai penjualan.
   ### Restock Recommendation
   Menampilkan daftar produk yang memiliki stok saat ini lebih kecil atau sama dengan batas minimum stok.
2. Analytics
   ### Product Performance Analysis
   Menampilkan visualisasi hubungan antara:
   - Total Sold
   - Average Daily Sales
  ### Average Daily Sales
  Menampilkan rata-rata jumlah produk yang terjual per hari.
  ### Product Classification
  Menampilkan hasil segmentasi produk berdasarkan model K-Means Clustering.

## Dataset
- sales_transaction.csv
  Dataset transaksi penjualan yang digunakan untuk analisis penjualan dan Machine Learning.
  Kolom utama:
  - Date
  - Product Name
  - Quantity
  - Total Amount
  - Retail Category
- inventory_stock.csv
  Dataset inventori yang digunakan untuk analisis stok.
  Kolom utama:
  - Product Name
  - Current Stock
  - Minimum Stock
  - Stock Status

  ## Algoritma
  1. Agregeaton analysis
     Digunakan untuk:
     - Menghitung total penjualan produk
      - Menghitung rata-rata penjualan harian
      - Menentukan produk terlaris
     ### Metode yang digunakan:
     - Grouping
     - Summation
     - Averaging
     - Sorting
    
  2. Threshold-Based Decision Algorithm
     Digunakan untuk menentukan kebutuhan restock.
     Rule:
     *Current Stock ≤ Minimum Stock*
     Output: *Restock Needed*

  3. K-Means Clustering
     Digunakan untuk mengelompokkan produk berdasarkan pola penjualan.
     Input fitur:
     - Total Sold
     - Average Daily Sales
     Jumlah cluster:
```Cluster 0
Cluster 1 ```

Tujuan:

Mengidentifikasi kelompok produk dengan karakteristik penjualan yang berbeda.

 4. StandardScaler
