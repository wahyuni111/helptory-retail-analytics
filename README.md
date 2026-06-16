#  📦 HELPTORY – Smart Retail Inventory Analytics
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

## 📈 Dataset
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
Cluster 0
Cluster 1 

Tujuan:

Mengidentifikasi kelompok produk dengan karakteristik penjualan yang berbeda.

 4. StandardScaler
    Digunakan sebelum proses clustering untuk menormalkan skala fitur sehingga       setiap fitur memiliki kontribusi yang seimbang terhadap model.

## STRUKTUR PROJECT 
```HELPTORY
PROGRAM
│
├── app.py
├── models
│   ├── analytics.py
│   ├── inventory.py
│   └── clustering.py
│   ├── data
│       ├── sales_transactions.csv
│       └── inventory_stock.csv
│ ├── assets
│ └── README.md
```
## PIPELINE SISTEM 
## ⚙️ Pipeline Fast Moving Product

```text
sales_transactions.csv
        │
        ▼
Group By Product
        │
        ▼
Sum Quantity
        │
        ▼
Sort Descending
        │
        ▼
Top 10 Fast Moving Products
```

Pipeline ini digunakan untuk mengidentifikasi produk dengan jumlah penjualan tertinggi berdasarkan total kuantitas yang terjual.

---

## 📦 Pipeline Restock Recommendation

```
inventory_stock.csv
        │
        ▼
Current Stock
vs
Minimum Stock
        │
        ▼
Current Stock <= Minimum Stock
        │
        ▼
Restock Recommendation
```

Pipeline ini digunakan untuk mendeteksi produk yang memiliki stok lebih kecil atau sama dengan batas minimum sehingga perlu dilakukan restock.

---

## 🤖 Pipeline Machine Learning (K-Means Clustering)

```
sales_transactions.csv
        │
        ▼
Feature Engineering
        │
        ▼
Total Sold
Average Daily Sales
        │
        ▼
StandardScaler
        │
        ▼
K-Means Clustering
        │
        ▼
Cluster 0 / Cluster 1
        │
        ▼
Product Segmentation
```

Pipeline ini digunakan untuk mengelompokkan produk berdasarkan pola penjualannya menggunakan algoritma K-Means Clustering.

Input Model:
- Total Sold
- Average Daily Sales

Output Model:
- Cluster Produk

---

## 🔄 Pipeline Sistem HELPTORY

```
sales_transactions.csv          inventory_stock.csv
          │                               │
          ▼                               ▼
    Analytics Module               Inventory Module
          │                               │
          ▼                               ▼
 Fast Moving Product         Restock Recommendation
 Average Daily Sales
          │
          ▼
   Feature Engineering
          │
          ▼
     StandardScaler
          │
          ▼
   K-Means Clustering
          │
          ▼
 Product Segmentation
          │
          ▼
 Streamlit Dashboard
          │
          ▼
 Decision Support for Retail Owner
```

Pipeline ini menggambarkan keseluruhan alur kerja aplikasi HELPTORY mulai dari pembacaan data, proses analisis, machine learning, hingga visualisasi dashboard untuk mendukung pengambilan keputusan pemilik retail.
## 👥 Tim Pengembang

| Nama | NIM | Peran |
|--------|--------|--------|
| Geugeut Nyarikawanti | 103132400002 | Problem Identification & Feature Improvement |
| Wahyuni Salsabila | 103132400010 | Project Coordinator, System Development & Maintenance |
| Azizatul Ainy | 00001999 | Research & Business Requirement Analysis |
| Fembiana Dika Saputri | 0000111777 | UI/UX Design  |
| Ruhfaidah | XXXXX | Documentation & System Testing |

## 🛠️ Cara Menjalankan Aplikasi

### 1. Clone Repository

```bash
git clone https://github.com/username/repository.git
```

Masuk ke folder project:

```bash
cd Program
```

---

### 2. Install Dependency

Pastikan Python sudah terinstal pada perangkat.

Install seluruh library yang dibutuhkan:

```bash
pip install pandas
pip install streamlit
pip install plotly
pip install scikit-learn
```

---

### 3. Menjalankan Aplikasi

Jalankan aplikasi menggunakan perintah berikut:

```bash
streamlit run app.py
```

---

### 4. Akses Dashboard

Setelah aplikasi berhasil dijalankan, Streamlit akan membuka browser secara otomatis atau menampilkan alamat lokal seperti:

```text
http://localhost:8501
```

Dashboard HELPTORY akan ditampilkan dan siap digunakan untuk analisis inventori retail.

---

## 📌 Output Sistem

Aplikasi HELPTORY menghasilkan beberapa output utama sebagai berikut:

### 📊 Dashboard Analisis Penjualan
Menampilkan ringkasan data penjualan, distribusi kategori produk, tren transaksi harian, dan produk dengan performa penjualan tertinggi.

### 📦 Dashboard Analisis Inventori
Menampilkan informasi stok produk yang tersedia serta kondisi inventori secara keseluruhan.

### 🔄 Rekomendasi Restock Produk
Mengidentifikasi produk yang memiliki stok lebih kecil atau sama dengan batas minimum sehingga memerlukan restock.

### 🚀 Analisis Produk Terlaris
Menampilkan produk dengan jumlah penjualan tertinggi berdasarkan total kuantitas yang terjual.

### 📈 Analisis Rata-Rata Penjualan Harian
Menampilkan estimasi permintaan harian setiap produk berdasarkan rata-rata jumlah produk yang terjual per hari.

### 🤖 Segmentasi Produk Menggunakan K-Means Clustering
Mengelompokkan produk berdasarkan pola penjualan menggunakan algoritma K-Means Clustering dengan fitur:

- Total Sold
- Average Daily Sales

Hasil segmentasi digunakan untuk membantu pemilik retail memahami karakteristik produk berdasarkan performa penjualannya.

---

##  Manfaat Sistem

Dengan adanya HELPTORY, admin retail dapat:

- Memantau performa penjualan secara real-time.
- Mengidentifikasi produk yang paling diminati pelanggan.
- Mengetahui produk yang membutuhkan restock lebih cepat.
- Memahami pola penjualan produk menggunakan Machine Learning.
- Mendukung pengambilan keputusan bisnis berbasis data.
