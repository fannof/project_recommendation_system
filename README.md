# Laporan Proyek Machine Learning - Novan Nur Hidayat

# PENGEMBANGAN SISTEM REKOMENDASI MAKANAN DENGAN ALGORITMA _CONTENT BASED_ DAN _COLLABORATIVE FILTERING_

## Project Overview

- Latar belakang

  Makanan sangat penting bagi manusia, baik sebagai kebutuhan primer maupun sebagai komponen kehidupan sehari-hari seseorang. Kemerosotan ekonomi yang telah mempengaruhi beberapa industri telah menyebabkan peluang baru yang membuat industri kuliner, khususnya divisi _online_-nya, semakin sukses. Wisata kuliner menjadi hal terpenting di dunia kuliner. Memanfaatkan informasi yang tersedia di internet membuat banyak masyarakat lebih sulit untuk memilih kebutuhan mereka.

  _Overchoice_, juga dikenal sebagai _overload of choices_, adalah gangguan kognitif di mana orang merasa sulit untuk membuat keputusan ketika dihadapkan dengan sejumlah besar pilihan. Mereka sering memiliki banyak pilihan yang sangat melelahkan secara mental karena setiap opsi harus dipertimbangkan dengan cermat untuk memilih opsi terbaik. Selama periode kemajuan teknologi ini, setiap orang dihadapkan pada pilihan yang jumlahnya tak terbatas. Fenomena ini, yang dikenal sebagai _overload of choice_, semakin banyak terjadi dalam kehidupan sehari-hari, seperti memilih makanan di suatu restoran. Pelanggan disajikan dari berbagai pilihan menu, termasuk _snack_, _dessert_, _beverage_, dan makanan lainnya yang sesuai.

  Setiap item makanan dalam kategori tersebut memiliki rasa dan harga unik yang juga bervariasi. Pertimbangan-pertimbangan ini menciptakan kompleksitas dalam arti bahwa pengguna dipaksa untuk mengeluarkan lebih banyak waktu dan energi untuk mendapatkan makanan yang sesuai. Selain itu, akan timbul keraguan dan kecemasan yang akan  mengakibatkan  memilih makanan yang tidak  disukai dan takut  kecewa  akan  pilihannya. Berdasarkan masalah tersebut, Sistem Rekomendasi diperlukan untuk membantu dalam memilih makanan yang diinginkan.

  Sistem rekomendasi adalah sistem yang menyarankan informasi yang berguna atau menunjukkan apa yang perlu dilakukan oleh pengguna untuk mencapai tujuan, yang bisa berupa memilih produk yang diinginkan. Dengan demikian, pelanggan dapat memilih produk yang lebih mudah beradaptasi dan lebih efektif dalam mengevaluasi produk yang diperlukan. Secara umum, ada tiga sistem rekomendasi yang banyak digunakan yaitu: _Content Based (CB)_, _Collaborative Filtering (CF)_, dan _Hybrid_.

  Sistem rekomendasi _Content Based_ menyarankan produk yang mirip dengan produk yang disukai pengguna sebelumnya. Nilai item ditentukan dengan mempertimbangkan fitur yang ada di setiap konten. Sistem rekomendasi _knowledge-based_ menyarankan item berdasarkan pengetahuan domain pengguna tentang fitur apa yang tersedia dalam item dan bagaimana pengguna dapat memenuhi kebutuhan dan berguna bagi pengguna. Nilai kesamaan dihitung berdasarkan besarnya nilai kesamaan antara kebutuhan pengguna dan rekomendasi yang ada. Ada dua pendekatan yang tersedia dalam metode rekomendasi _knowledge-based_ yaitu _case based_ dan _constraint-based_. Kesamaan antara kedua pendekatan ini adalah bahwa pengguna harus mengirimkan permintaan sesegera mungkin.  Selanjutnya, sistem akan mengidentifikasi solusi yang paling sesuai dengan kebutuhan pengguna.

  Metode _Collaborative Filtering_ adalah teknik yang memberikan rekomendasi berdasarkan preferensi pengguna atau item serupa lainnya.  Dua jenis metode _Collaborative Filtering_ dibedakan menjadi: _User Based CF_ dan _Item Based CF_. _User-Based Collaborative Filtering_ menyatakan bahwa cara terbaik untuk menemukan item menarik bagi pengguna adalah dengan mencari pengguna lain yang memiliki minat atau kebutuhan yang sama. Algoritma _User Based CF_ dapat mengidentifikasi pengguna yang mirip satu sama lain _(user neighbor)_ dengan mengidentifikasi pengguna yang berbeda satu sama lain _(user similarity)_. Setiap rating yang didapatkan dari pengguna yang bertetangga kemudian akan dijadikan mesin rekomendasi bagi pengguna aktif.

  Di sisi lain, _Item-Based Collaborative Filtering_ memiliki struktur yang mirip dengan _User Based C_. Jika pemfilteran _user-based_ sebelumnya menunjukkan korelasi _user_ ke _user_, maka pemfilteran _item-based_ akan menunjukkan korelasi item yang diminati oleh sistem pengguna lain. Item-item akan terus terakumulasi. Salah satu keuntungan dari metode _item-based  collaborative  filtering_ adalah kemampuannya untuk mengeksplorasi jejaring sosial implisit, yang berpotensi meningkatkan akurasi rekomendasi yang dibuat.

- Rumusan Masalah dan Solusi Permasalahan

  Banyaknya pilihan makanan yang tersedia di restoran dapat membuat pelanggan yang berkunjung merasa ragu untuk memilih makanan, dan fenomena _overchoice_ pun tidak dapat dihindari. Salah satu solusi untuk memastikan kepuasan pelanggan adalah pelayan atau pramusaji merekomendasikan item menu kepada pelanggan. Namun, ini juga menyebabkan mereka menjadi letih dan gagal mengenali preferensi setiap pelanggan. Tidak setiap pelanggan memiliki preferensi yang sama dengan pelayan atau pramusaji; Sebaliknya, setiap pelanggan memiliki preferensi unik yang berbeda dari pelanggan lain, serta lamanya waktu yang dibutuhkan oleh pelanggan yang mengalami fenomena _overchoice_, yang menyebabkan pelayan menjadi 'menyerah' ketika melayani pelanggan.

  Karena itu, sistem rekomendasi diperlukan untuk menyarankan makanan yang tersedia di restoran kepada pelanggan untuk membantu mereka dalam memilih makanan yang mereka inginkan, menghemat waktu mereka ketika pemesanan menu, dan membantu restoran dalam memahami perilaku pelanggan. Dalam  proyek ini, peneliti mengabaikan semua menu minuman pada restoran dikarenakan jumlah menu minuman yang tersedia pada restoran hanya tersedia beberapa buah menu minuman dan dianggap terlalu sedikit untuk dimasukkan kedalam sistem yang baru.

- Hasil Riset Terkait

  Dalam jurnal yang berjudul "SISTEM REKOMENDASI MENU MINUMAN DENGAN METODE _CONTENT–BASED FILTERING_ BERBASIS _ANDROID_ PADA MUBTADA KOPI" yang dipublikasikan oleh Kosim dan Reza Prihandi(2024) dijelaskan bahwa _Overchoice_ adalah gangguan kognitif di mana orang mengalami kesulitan membuat keputusan ketika dihadapkan dengan banyak pilihan, memiliki terlalu banyak pilihan yang setara sangat menguras mental karena setiap pilihan harus mempertimbangkan beberapa alternatif untuk memilih pilihan yang terbaik. Pada masa perkembangan teknologi  ini dimana setiap harinya semua orang dihadapkan oleh pilihan yang tidak terhingga jumlahnya, fenomena _overchoice_ ini kerap terjadi dalam kehidupan sehari–hari seperti memilih minuman pada salah satu kedai café, maka dari itu _Recommendation System_ diperlukan untuk membantu dalam memilih minuman yang ingin dipesan dan untuk membantu dalam memilih pilihan lainnya. Teknik _content–based filtering_ akan mencoba mengambil preferensi pengguna secara eksplisit yaitu meminta pengguna untuk memilih preferensi yang diinginkan pengguna dari ke-6 fitur yang sudah dibuat sebelumnya lalu dihitung kecocokan preferensi pengguna dengan ke-6 fitur pada masing-masing–masing item menggunakan rumus _dotmatrix_. Setelah mendapatkan hasilnya, angka tersebut akan dirubah menjadi sebuah rating agar sesuai dengan pendekatan _Recommendation System_ yaitu _best rated_ yang dibuat secara _non-personalized_. Rating ini merupakan indikasi kecocokan preferensi pengguna dengan item yang terdapat pada daftar menu Mubtada Kopi. Semakin besar ratingnya, semakin cocok dengan preferensi pengguna.

## Business Understanding

### Problem Statements

- Apakah sistem rekomendasi _hybrid_ dapat menjadi solusi yang efektif untuk merekomendasikan makanan kepada pelanggan yang sesuai dengan keinginannya?

- Bagaimana tahapan dalam pembuatan sistem rekomendasi _hybrid_ yang akan merekomendasikan makanan sesuai preferensi pelanggan?

### Goals

- Tujuan yang dimaksudkan adalah untuk membantu pelayan agar tidak bingung dalam merekomendasikan makanan, dikarenakan selera orang terkadang berbeda-beda. Solusi yang dihasilkan harus dapat memaksimalkan rekomendasi yang diberikan sekaligus memastikan rekomendasi tersebut dapat diterima dengan baik oleh pelanggan.

- Tujuan utamanya adalah untuk mengembangkan model atau sistem rekomendasi yang dapat mengidentifikasi dan merekomendasikan makanan untuk menyesuaikan dengan preferensi pelanggan. Tujuan proses rekomendasi ini adalah untuk memberikan lebih banyak makanan yang sesuai minat dan bagaimana mengidentifikasi karakteristik pelanggan, seperti makanan yang disukai sebelumnya dan kemiripan selera dengan pelanggan lain yang mempengaruhi nilai rekomendasi.

### Solution Approach

- Menggunakan pendekatan _Content Based Filtering_ untuk merekomendasikan makanan ke pelanggan sesuai minat sebelumnya dan _Collaborative Filtering_ untuk merekomendasikan makanan ke pelanggan sesuai persamaan kesukaan dengan pelanggan lain. Hal ini bertujuan untuk melakukan rekomendasi dengan memanfaatkan kekuatan masing-masing model. Evaluasi model dapat menggunakan metrik seperti _Root Mean Squared Error (RMSE)_ untuk mengukur seberapa baik model merekomendasi makanan.

## Data Understanding

Pasar _real estate_, seperti yang ada di Seattle, Washing, USA, menghadirkan peluang menarik bagi analis data untuk menganalisis dan memprediksi ke mana harga properti bergerak. Prediksi harga properti menjadi semakin penting dan menguntungkan. Harga properti merupakan indikator yang baik dari kondisi pasar secara keseluruhan dan kesehatan ekonomi suatu negara. Mempertimbangkan data yang diberikan, dalam memperdebatkan sejumlah besar catatan penjualan properti yang disimpan dalam format yang tidak diketahui dan dengan masalah kualitas data yang tidak diketahui.

  Data yang digunakan dalam proyek ini bersumber dari [Kaggle-Food Recommendation System](https://www.kaggle.com/samuelcortinhas/schemersays/food-recommendation-system)

  Jumlah data pada dataset _foods.csv_ sebanyak 400 data, yang terbagi dalam 5 kolom. Kolom pertama yaitu 'Food_ID' yang di _rename_ menjadi 'id_makanan' memiliki 400 data unik bertipe _integer_, kolom 'Name' yang di _rename_ menjadi 'nama_makanan' memiliki 400 data unik bertipe _object_, kolom 'C_Type' yang di _rename_ menjadi 'jenis_makanan' memiliki 400 data bertipe _object_ dengan 16 jenis makanan yang unik, kolom 'Veg_Non' yang di _rename_ menjadi 'veg_non' memiliki 400 data bertipe _object_, kolom 'Describe' yang di _rename_ menjadi 'deskripsi' memiliki 400 data unik bertipe _object_. Dataset dapat lebih lanjut dilihat pada Tabel 1 dan 2.

Tabel 1. Dataset _foods.csv_ sebelum di _rename_

|     | Food_ID |                                              Name |       C_Type | Veg_Non | Describe                                          |
|----:|--------:|--------------------------------------------------:|-------------:|--------:|---------------------------------------------------|
|  0  |       1 |                               summer squash salad | Healthy Food |     veg | white balsamic vinegar, lemon juice, lemon rin... |
|  1  |       2 |                              chicken minced salad | Healthy Food | non-veg | olive oil, chicken mince, garlic (minced), oni... |
|  2  |       3 |                              sweet chilli almonds |        Snack |     veg | almonds whole, egg white, curry leaves, salt, ... |
|  3  |       4 |                                   tricolour salad | Healthy Food |     veg | vinegar, honey/sugar, soy sauce, salt, garlic ... |
|  4  |       5 |                                    christmas cake |      Dessert |     veg | christmas dry fruits (pre-soaked), orange zest... |
| ... |     ... |                                               ... |          ... |     ... |                                               ... |
| 395 |     396 |                                      Kimchi Toast |       Korean |     veg |  cream cheese, chopped kimchi, scallions,count... |
| 396 |     397 | Tacos de Gobernador (Shrimp, Poblano, and Chee... |      Mexican | non-veg | poblano chiles, bacon, shrips, red salsa, garl... |
| 397 |     398 |   Melted Broccoli Pasta With Capers and Anchovies |       French | non-veg |  broccoli,Bread Crumbs, anchovy fillets, garli... |
| 398 |     399 |                 Lemon-Ginger Cake with Pistachios |      Dessert | non-veg | egg yolks,lemon juice, unsalted butter, all pu... |
| 399 |     400 |                       Rosemary Roasted Vegetables | Healthy Food |     veg | kosher salt, rosemary, garlic, potato, olive o... |

Tabel 2. Dataset _foods.csv_ setelah di _rename_

|     | id_makanan |                                      nama_makanan | jenis_makanan | veg_non | deskripsi                                         |
|----:|-----------:|--------------------------------------------------:|--------------:|--------:|---------------------------------------------------|
|  0  |          1 |                               summer squash salad |  Healthy Food |     veg | white balsamic vinegar, lemon juice, lemon rin... |
|  1  |          2 |                              chicken minced salad |  Healthy Food | non-veg | olive oil, chicken mince, garlic (minced), oni... |
|  2  |          3 |                              sweet chilli almonds |         Snack |     veg | almonds whole, egg white, curry leaves, salt, ... |
|  3  |          4 |                                   tricolour salad |  Healthy Food |     veg | vinegar, honey/sugar, soy sauce, salt, garlic ... |
|  4  |          5 |                                    christmas cake |       Dessert |     veg | christmas dry fruits (pre-soaked), orange zest... |
| ... |        ... |                                               ... |           ... |     ... |                                               ... |
| 395 |        396 |                                      Kimchi Toast |        Korean |     veg |  cream cheese, chopped kimchi, scallions,count... |
| 396 |        397 | Tacos de Gobernador (Shrimp, Poblano, and Chee... |       Mexican | non-veg | poblano chiles, bacon, shrips, red salsa, garl... |
| 397 |        398 |   Melted Broccoli Pasta With Capers and Anchovies |        French | non-veg |  broccoli,Bread Crumbs, anchovy fillets, garli... |
| 398 |        399 |                 Lemon-Ginger Cake with Pistachios |       Dessert | non-veg | egg yolks,lemon juice, unsalted butter, all pu... |
| 399 |        400 |                       Rosemary Roasted Vegetables |  Healthy Food |     veg | kosher salt, rosemary, garlic, potato, olive o... |

  Jumlah data pada dataset _ratings.csv_ sebanyak 512 data, yang terbagi dalam 3 kolom. Kolom pertama yaitu 'User_ID' yang di _rename_ menjadi 'user_id' memiliki 512 data bertipe _integer_ dengan 101 data yang unik, kolom 'Food_ID' yang di _rename_ menjadi 'id_makanan' memiliki 512 data bertipe _integer_ dengan 310 data yang unik, kolom 'Rating' yang di _rename_ menjadi 'rating' memiliki 512 data bertipe _integer_. Terdapat 1 nilai NaN pada dataset ini. Dataset dapat lebih lanjut dilihat pada Tabel 3 dan 4.

Tabel 3. Dataset _ratings.csv_ sebelum di _rename_

|     | User_ID | Food_ID | Rating |
|----:|--------:|--------:|-------:|
|  0  |     1.0 |    88.0 |    4.0 |
|  1  |     1.0 |    46.0 |    3.0 |
|  2  |     1.0 |    24.0 |    5.0 |
|  3  |     1.0 |    25.0 |    4.0 |
|  4  |     2.0 |    49.0 |    1.0 |
| ... |     ... |     ... |    ... |
| 507 |    99.0 |    22.0 |    1.0 |
| 508 |   100.0 |    24.0 |   10.0 |
| 509 |   100.0 |   233.0 |   10.0 |
| 510 |   100.0 |    29.0 |    7.0 |
| 511 |     NaN |     NaN |    NaN |

Tabel 4. Dataset _ratings.csv_ setelah di _rename_

|     | user_id | id_makanan | rating |
|----:|--------:|-----------:|-------:|
|  0  |     1.0 |       88.0 |    4.0 |
|  1  |     1.0 |       46.0 |    3.0 |
|  2  |     1.0 |       24.0 |    5.0 |
|  3  |     1.0 |       25.0 |    4.0 |
|  4  |     2.0 |       49.0 |    1.0 |
| ... |     ... |        ... |    ... |
| 507 |    99.0 |       22.0 |    1.0 |
| 508 |   100.0 |       24.0 |   10.0 |
| 509 |   100.0 |      233.0 |   10.0 |
| 510 |   100.0 |       29.0 |    7.0 |
| 511 |     NaN |        NaN |    NaN |

Tabel 5. Deskripsi dataset _ratings.csv_

|       |    user_id | id_makanan |     rating |
|------:|-----------:|-----------:|-----------:|
| count | 511.000000 | 511.000000 | 511.000000 |
|  mean |  49.068493 | 125.311155 |   5.438356 |
|  std  |  28.739213 |  91.292629 |   2.866236 |
|  min  |   1.000000 |   1.000000 |   1.000000 |
|  25%  |  25.000000 |  45.500000 |   3.000000 |
|  50%  |  49.000000 | 111.000000 |   5.000000 |
|  75%  |  72.000000 | 204.000000 |   8.000000 |
|  max  | 100.000000 | 309.000000 |  10.000000 |

Pada tabel 5 untuk rata-rata rating yaitu berada pada angka 5,4 bintang dengan skala bintang dari 1-10.

### Variabel-variabel pada House Price Prediction dataset adalah sebagai berikut:

- beds : jumlah kamar tidur di properti.
- baths : Jumlah kamar mandi di properti. Catatan 0,5 sesuai dengan setengah bak mandi yang memiliki wastafel dan toilet tetapi tidak ada bak mandi atau pancuran.
- size : Total luas lantai properti.
- size_units : Unit pengukuran sebelumnya.
- lot_size : Total luas tanah tempat properti berada. Tanah itu milik pemilik rumah.
- lot_size_units : Unit pengukuran sebelumnya.
- zip_code : Kode pos. Ini adalah kode pos yang digunakan di AS.
- price : Harga properti dijual seharga _(dollar AS)_.

### Exploratory Data Analysis

- Menangani _missing value_

  Dari hasil output, terlihat bahwa kolom "lot_size" dan "lot_size_units" memiliki nilai yang hilang (NaN) sebanyak 347 data. Dengan menggunakan teknik _dropna_, sekarang _DataFrame_ rumah tidak mengandung baris dengan nilai yang hilang di kolom "lot_size" dan "lot_size_units".

  Tabel 3. Dataset sudah bersih dari _missing value_

  |      | beds | baths | size   | size_units | lot_size | lot_size_units | zip_code | price     |
  |-----:|-----:|-------|--------|------------|----------|----------------|----------|-----------|
  | 0    | 3    | 2.5   | 2590.0 | sqft       | 6000.00  | sqft           | 98144    | 795000.0  |
  | 1    | 4    | 2.0   | 2240.0 | sqft       | 0.31     | acre           | 98106    | 915000.0  |
  | 2    | 4    | 3.0   | 2040.0 | sqft       | 3783.00  | sqft           | 98107    | 950000.0  |
  | 3    | 4    | 3.0   | 3800.0 | sqft       | 5175.00  | sqft           | 98199    | 1950000.0 |
  | 5    | 2    | 2.0   | 1190.0 | sqft       | 1.00     | acre           | 98107    | 740000.0  |
  | ...  | ...  | ...   | ...    | ...        | ...      | ...            | ...      | ...       |
  | 2009 | 3    | 3.5   | 1680.0 | sqft       | 1486.00  | sqft           | 98126    | 675000.0  |
  | 2010 | 2    | 2.0   | 1400.0 | sqft       | 0.34     | acre           | 98199    | 699950.0  |
  | 2011 | 3    | 2.0   | 1370.0 | sqft       | 0.50     | acre           | 98112    | 910000.0  |
  | 2013 | 4    | 2.0   | 2140.0 | sqft       | 6250.00  | sqft           | 98199    | 1150000.0 |
  | 2015 | 3    | 2.0   | 1710.0 | sqft       | 4267.00  | sqft           | 98133    | 659000.0  |

- Menangani _outliers_

  Pada kasus ini, akan dideteksi _outliers_ dengan teknik visualisasi data _(boxplot)_. Kemudian, _outliers_ akan ditangani dengan teknik _IQR method_. setelah ditangani dengan metode _IQR method_, dataset yang tersisa menjadi 1682 data.

  Gambar 1. Deteksi _outliers_ pada kolom 'beds'

  ![beds](https://github.com/fannof/project_predictive_analysis/assets/99071605/30d6a272-05ce-40f2-b8f3-6b172301e2e0)


  Terlihat pada gambar 1, terdapat 4 _outliers_ di kolom 'beds'.

  Gambar 2. Deteksi _outliers_ pada kolom 'baths'

  ![image](https://github.com/fannof/project_predictive_analysis/assets/99071605/5e8ae48e-c7c4-4c26-8fd9-7829b2478f78)

  Terlihat pada gambar 2, terdapat 6 _outliers_ di kolom 'baths'

  Gambar 3. Deteksi _outliers_ pada kolom 'size'

  ![image](https://github.com/fannof/project_predictive_analysis/assets/99071605/f97ce15a-a3cc-49be-be23-00760a9470b2)

  Pada gambar 3, terdapat banyak sekali _outliers_, semua _outliers_ ini akan ditangani dengan metode _IQR Method_.

- _Univariate analysis_

  Selanjutnya, akan dilakukan proses analisis data dengan teknik _Univariate EDA_. Pertama, lakukan analisis pada fitur numerik.
Peningkatan harga rumah sebanding dengan penurunan jumlah sampel. Hal ini dapat dilihat jelas dari histogram "price" pada gambar 4, dimana grafiknya mengalami penurunan seiring dengan semakin banyaknya jumlah sampel (sumbu x).
Semakin tinggi 'size', jumlah 'beds', dan jumlah 'baths' dalam rumah, maka semakin mahal pula harga rumah.

  Gambar 4. Plot grafik masing-masing fitur

  ![image](https://github.com/fannof/project_predictive_analysis/assets/99071605/1d2c2658-3292-4522-a8a7-100deff8dd2b)

- _Multivariate analysis_

  Selanjutnya, akan dilakukan analisis data pada fitur numerik menggunakan teknik _Multivariate EDA_ menggunakan fungsi _pairplot()_ dan juga akan mengobservasi korelasi antara fitur numerik dengan fitur target menggunakan fungsi _corr()_.
  Pada gambar 5 yaitu pola sebaran data grafik _pairplot_, terlihat fitur "size" memiliki korelasi positif dengan fitur "price". Sedangkan kedua fitur "lot_size" dan "price" tidak memliki korelasi karena tidak membetuk pola.

  Gambar 5. Grafik korelasi antar fitur numerik dan fitur target

  ![image](https://github.com/fannof/project_predictive_analysis/assets/99071605/c38c6c64-e41a-45eb-9022-7a6d66971ff9)

  Gambar 6. Matrik korelasi antar fitur numerik

  ![image](https://github.com/fannof/project_predictive_analysis/assets/99071605/570e873b-5804-431d-b0f2-10efdbed5690)

  Pada gambar 6, grafik korelasi terlihat bahwa fitur 'beds', 'baths', dan 'size' memiliki skor korelasi yang besar dengan fitur target 'price'. Artinya, fitur 'price' berkorelasi tinggi dengan ketiga fitur tersebut. Sementara itu, fitur 'lot_size' dan 'zip_code' memiliki korelasi yang sangat kecil sehingga fitur tersebut dapat _di-drop_.

  Tabel 4. _Dataframe_ setelah fitur yang tidak dibutuhkan _di-drop_

  |   | beds | baths |   size |    price |
  |--:|-----:|------:|-------:|---------:|
  | 0 |    3 |   2.5 | 2590.0 | 795000.0 |
  | 1 |    4 |   2.0 | 2240.0 | 915000.0 |
  | 2 |    4 |   3.0 | 2040.0 | 950000.0 |
  | 5 |    2 |   2.0 | 1190.0 | 740000.0 |
  | 6 |    1 |   1.0 |  670.0 | 460000.0 |

  Gambar 7. Grafik plot antar fitur numerik setelah fitur yang tidak dibutuhkan _di-drop_

  ![image](https://github.com/fannof/project_predictive_analysis/assets/99071605/89e1a48b-9af0-426a-a357-16fcf9c87624)

## Data Preparation

- _Train-Test-Split_

  Proses membagi himpunan data menjadi data pelatihan dan pengujian adalah langkah yang diperlukan sebelum membuat model. Ini penting dilakukan untuk memperkuat semua data yang tersedia untuk menilai beberapa generalisasi model ke data baru. Tercatat bahwa setiap transformasi data yang dilakukan juga berfungsi sebagai komponen model. Karena data _test set_ (uji) mentah, semua transformasi harus dilakukan pada data latih. Data dibagi menjadi 80% data _training_ dan 20% data _testing_, karena jumlah seluruh data termasuk kecil, maka diperlukan lebih banyak data latih.

  Total sampel seluruh dataset: 1380

  Total sampel data latih: 1104

  Total sampel data uji: 276

- _Standarisasi_

  Ketika algoritma pembelajaran mesin diterapkan pada data dengan distribusi yang serupa atau menyimpang, mereka berkinerja lebih baik dan menyatu lebih cepat. Proses penskalaan dan _standardisasi_ membantu mengubah data menjadi format yang lebih mudah dipahami oleh algoritma.

  Tabel 5. Dataset setelah dilakukan _Standarisasi_

  |      |      beds |     baths |      size |
  |-----:|----------:|----------:|----------:|
  | 1779 | -1.973241 | -1.412389 | -1.635772 |
  |  316 |  0.014403 | -0.809653 | -0.143301 |
  | 1385 | -0.979419 |  0.395818 | -1.011919 |
  | 1666 | -1.973241 | -1.412389 | -1.416378 |
  | 2004 | -0.979419 | -0.206917 | -0.744767 |

  _Standardisasi_ adalah teknik transformasi yang paling umum digunakan dalam proses pembangunan model. Ini tidak akan mengubah fitur numerik menggunakan _encoding_. Teknik yang digunakan adalah _StandarScaler_ dari _library Scikit-learn_. Hasilnya dapat dilihat pada tabel 5.

  Tabel 6. Informasi dataset setalah dilakukan teknik _Standarisasi_

  |       |      beds | baths     | size      |
  |------:|----------:|-----------|-----------|
  | count | 1104.0000 | 1104.0000 | 1104.0000 |
  | mean  | 0.0000    | -0.0000   | 0.0000    |
  | std   | 1.0005    | 1.0005    | 1.0005    |
  | min   | -1.9732   | -2.0151   | -2.2029   |
  | 25%   | -0.9794   | -0.8097   | -0.7679   |
  | 50%   | 0.0144    | -0.2069   | -0.1209   |
  | 75%   | 1.0082    | 0.3958    | 0.6776    |
  | max   | 3.9897    | 3.4095    | 3.3342    |

  Dapat dilihat pada tabel 5, jumlah kolom setiap fitur memiliki sebanyak 1104 data. Dengan nilai minimal bernilai negatif (dibawah 0) dan nilai maksimal diantara angka 3 sampai 4.

### Penjelasan tahapan dan kenapa harus dilakukan proses tersebut

- Proses _data prepraration_

  Pertama adalah proses _train-test-split_. Data dibagi menjadi 80% _data training_ dan 20% _data testing_, karena jumlah seluruh data termasuk kecil, maka diperlukan lebih banyak data latih.

  Proses _standarisasi_ mengubah nilai mean menjadi 0 dan std menjadi 1. _StandardScaler_ melakukan proses _standardisasi_ parameter fitur terlebih dahulu dengan mengurangkan nilai _mean_ (nilai rata-rata) dan kemudian membandingkannya dengan standar deviasi untuk menentukan distribusi.  _StandardScaler_ menghasilkan distribusi dengan rata-rata 0 dan standar deviasi 1.

  Tahapan diatas penting dilakukan karena algoritma _machine learning_ memiliki performa lebih baik ketika dimodelkan pada data dengan skala relatif sama atau mendekati distribusi normal.

## Modeling

Model akan dikembangkan dengan 3 algoritma yang berbeda, dan mencari mana yang memiliki performa paling baik. Beberapa algoritma tersebut adalah sebagai berikut:

1. _k-NN_

   Merupakan algoritma _supervised learning_ yang mengklasifikasikan hasil instance yang baru dibuat berdasarkan mayoritas kategori k-tetangga terdekat.
   Tujuan algoritma ini adalah untuk mengklasifikasikan objek baru berdasarkan atribut dan data sampel-sampel dari set pelatihan.
   Algoritma _k-Nearest Neighbor_ menggunakan _Neighborhood Classification_ sebagai nilai prediksi yang berasal dari instance baru [3]. Seperti yang terlihat pada gambar 8.

   Gambar 8. Algoritma _k-NN_

   ![th](https://github.com/fannof/project_predictive_analysis/assets/99071605/2ac7ac6a-1790-4f6e-8a9b-82645c01735b)


    Langkah yang pertama, model _k-NN_ diinisialisasi dengan menentukan jumlah tetangga terdekat _(parameter n_neighbors)_. Contoh dalam kasus ini adalah _n_neighbors_ diatur ke 10, artinya model akan menggunakan 10 tetangga tetangga yang paling dekat untuk membuat prediksi.
    Setelah model diinisialisasi, langkah selanjutnya adalah melatih model menggunakan data latih. Untuk melatih model dengan fitur X_train dan target y_train, gunakan fungsi _fit(X_train, y_train)_.
    Setelah proses pelatihan selesai, model sudah dapat membuat prediksi pada data latih untuk mengevaluasi performa model. 
  
    Parameter yang digunakan pada model _k-NN_:

    - n_neighbors: Jumlah tetangga terdekat yang digunakan untuk membuat prediksi.

2. _Random Forest_

    _Random Forest_ menggunakan atribut kernel, sehingga dapat digunakan untuk membuat prediksi tentang data yang belum dihasilkan. Pendekatan _"divide and conquer"_ adalah apa yang dimaksud pohon keputusan sendiri ketika mempelajari suatu masalah berdasarkan kumpulan data independen yang ditampilkan dalam bagan pohon. Selain itu, pohon keputusan adalah kumpulan pertanyaan yang dijawab secara sistematis, di mana setiap pertanyaan yang diajukan menentukan jawaban berdasarkan nilai atribut dan didasarkan pada pohon daun, yang merupakan prediksi dari variabel kelas [4].

    Gambar 9. Algoritma _Random Forest_

    ![th](https://github.com/fannof/project_predictive_analysis/assets/99071605/6e665d4f-12da-4c6f-b42a-7dc4998c66d2)


    Model _Random Forest_ diinisialisasi dengan menentukan beberapa hyperparameter.
    Model _Random Forest_ dilatih menggunakan data latih (X_train dan y_train). Fungsi fit(X_train, y_train) digunakan untuk melatih model.
    Setelah pelatihan selesai, model sekarang dapat digunakan untuk membuat prediksi pada data latih. _RF.predict(X_train)_ menghasilkan prediksi target berdasarkan fitur pada data latih.
  
    Parameter yang Digunakan pada Model _Random Forest_:
  
    - n_estimators: Jumlah pohon keputusan dalam _ensemble_.
  
    - max_depth: Kedalaman maksimum setiap pohon keputusan.

    - random_state: Digunakan untuk memastikan hasil yang reproduktif.
  
    - n_jobs: Jumlah pekerjaan paralel yang akan dijalankan.

3. _Boosting Algorithm_

    Algoritma _boosting_ adalah algoritma iteratif yang menyediakan bot berbeda untuk distribusi data pelatihan setiap iterasi. Setiap iterasi peningkatan menambahkan bot ke setiap contoh masalah klasifikasi dan mengurangi bot ke contoh klasifikasi yang benar sehingga data pelatihan dapat didistribusikan secara efektif. Lebih efektif untuk mengatasi masalah ketidakseimbangan kelas, metode _Boosting (AdaBoost)_ yang diusulkan dengan _selective costing ensemble_ mampu meningkatkan identifikasi dari kelas minoritas yang sulit serta menjaga kemampuan klasifikasi dari _class_ mayoritas. Karena prevalensi metode pembelajaran _ensamble_ yang dapat mengurangi variasi, fenomena ini terjadi karena bias rata-rata metode _ensamble_ dalam mengurangi variasi dari satu set kriteria [5].

    Gambar 10. Algoritma _Boosting_

    ![ada3](https://github.com/fannof/project_predictive_analysis/assets/99071605/e8579d87-59f8-4e2e-84c2-e97fb3893bf1)


    Model _Boosting (AdaBoostRegressor)_ diinisialisasi dengan menentukan _hyperparameter_ tertentu. Parameter yang diatur adalah _learning_rate_ dengan nilai 0.05. _random_state_ digunakan untuk memastikan reproduktibilitas hasil.
    Model diarahkan untuk mempelajari hubungan antara fitur (X_train) dan target (y_train). Fungsi _fit(X_train, y_train)_ digunakan untuk melatih model dengan data latih.
    Setelah pelatihan selesai, sekarang model dapat digunakan untuk membuat prediksi pada data latih. _boosting.predict(X_train)_ menghasilkan prediksi target berdasarkan fitur pada data latih.
   
    Parameter yang Digunakan pada Model _Boosting (AdaBoostRegressor)_:
   
    - learning_rate: Menentukan sejauh mana model belajar dari kesalahan sebelumnya. Nilai yang lebih kecil akan memperbaiki konvergensi, tetapi memerlukan jumlah estimator (pohon       keputusan) yang lebih besar.
  
    - n_estimators: Jumlah estimator (pohon keputusan) yang digunakan.

    - base_estimator: Tipe model dasar yang digunakan. Secara default, digunakan pohon keputusan _(DecisionTreeRegressor)_.

    - random_state: Digunakan untuk memastikan hasil yang reproduktif.

  - Kelebihan dan kekurangan dari setiap algoritma yang digunakan:

    -- _k-NN_ memiliki _MSE_ yang tinggi pada data uji, mungkin karena model tidak dapat menangkap pola yang kompleks dalam data tersebut.

    -- _Random Forest_ memiliki _MSE_ yang rendah pada data latih, menunjukkan kemampuan baik dalam menyesuaikan dengan data latih. Namun, terdapat peningkatan yang signifikan pada _MSE_ pada data uji, mungkin menunjukkan adanya _overfitting_.

    -- _Boosting_ memberikan hasil yang cukup baik pada data uji, menunjukkan kemampuan model untuk mengatasi kompleksitas data.

  - Alasan memlilih Model _Boosting Algorithm_

    Dari ketiga model diatas, _Boosting_ memiliki _MSE_ yang relatif lebih rendah pada data uji, menunjukkan kinerja yang lebih baik dibandingkan dengan _k-NN_ dan _Random Forest_ dalam dataset harga rumah ini.

    Berdasarkan hasil tersebut, solusi terbaik pada kasus ini adalah menggunakan model _Boosting (AdaBoostRegressor)_ karena memberikan performa yang lebih baik dalam memprediksi harga rumah pada data yang belum pernah dilihat sebelumnya.

## Evaluation

- Metrik yang digunakan adalah _MSE_

  _Mean Squared Error (MSE)_ adalah salah satu metrik evaluasi yang umum digunakan dalam regresi untuk mengukur sejauh mana perbedaan antara nilai prediksi model dengan nilai aktual _(ground truth)_. _MSE_ dihitung dengan menjumlahkan kuadrat selisih antara setiap nilai prediksi dan nilai aktual, kemudian diambil rata-rata dari seluruh data. Nilai _MSE_ semakin kecil semakin baik. Nilai _MSE_ sama dengan nol berarti model memberikan prediksi yang sempurna sesuai dengan nilai aktual. Metrik evaluasi dapat dilihat pada tabel 7.

  Tabel 7. Metrik evaluasi berdasarkan jenis algoritma yang digunakan

  |          |           train | test            |
  |---------:|----------------:|-----------------|
  | KNN      | 44360753.266994 | 54239740.502329 |
  | RF       | 12390218.332403 | 58255407.24918  |
  | Boosting | 49336053.971147 | 51079691.292662 |

  Gambar 11. Plot metrik evaluasi perbandingan antar algoritma

  ![image](https://github.com/fannof/project_predictive_analysis/assets/99071605/5985c172-5ba8-49a3-b9d9-530935352cae)

- Hasil proyek berdasarkan metrik evaluasi
  1. _K-Nearest Neighbors (k-NN)_:

     - Data Latih _(Train)_: _MSE_ sekitar 44,360,753.27.

     - Data Uji _(Test)_: _MSE_ sekitar 54,239,740.50.

     - Interpretasi: Model _k-NN_ memiliki hasil yang lebih baik pada data latih dibandingkan dengan data uji, mungkin menunjukkan adanya _overfitting_ atau kurangnya kemampuan untuk menggeneralisasi pada data yang belum pernah dilihat sebelumnya.

  2. _Random Forest (RF)_:

     - Data Latih _(Train)_: _MSE_ sekitar 12,390,218.33.

     - Data Uji _(Test)_: _MSE_ sekitar 58,255,407.25.

     - Interpretasi: Model _Random Forest_ menunjukkan performa yang baik pada data latih, tetapi terdapat peningkatan yang signifikan pada _MSE_ pada data uji, mungkin mengindikasikan adanya _overfitting_.

  3. _Boosting_:

     - Data Latih _(Train_): _MSE_ sekitar 49,336,053.97.
     
     - Data Uji _(Test)_: _MSE_ sekitar 51,079,691.29.

     - Interpretasi: Model Boosting menunjukkan hasil yang relatif baik pada data uji dibandingkan dengan model _k-NN_ dan _Random Forest_. Meskipun _MSE_ pada data latih lebih tinggi dari _Random Forest_, kemampuan generalisasi pada data uji tampaknya lebih baik.
 
      Tabel 8. Hasil uji perbandingan antar algoritma yang dipakai

      |      |    y_true | prediksi_KNN | prediksi_RF | prediksi_Boosting |
      |-----:|----------:|-------------:|------------:|------------------:|
      | 1680 | 1725000.0 |    1285250.0 |   1316599.0 |         1306669.6 |

      _Mean Squared Error (MSE)_ dihitung brdasarkan formula:

      $$MSE = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2$$

      Dimana $\( n \)$ adalah angka observasi, $\( y_i \)$ adalah nilai aktual, dan $\( \hat{y}_i \)$ adalah nilai prediksi.

      - Cara Kerja:

        - _MSE_ mengukur rata-rata dari kuadrat selisih antara nilai prediksi dan nilai aktual.

      - Prosesnya melibatkan langkah-langkah berikut:

        - Menghitung selisih antara setiap nilai prediksi dan nilai aktual.

        - Mengkuadratkan setiap selisih.

        - Menjumlahkan semua nilai kuadrat.

        - Membagi jumlah nilai kuadrat dengan jumlah observasi (n) untuk mendapatkan rata-rata.

      - Interpretasi:

        - Semakin kecil nilai _MSE_, semakin baik model memperkirakan nilai aktual.

        - Kesalahan yang lebih besar akan memberikan kontribusi yang lebih besar terhadap nilai _MSE_ karena nilai diangkat ke kuadrat.
     
## REFERENCES

[1]	M. L. Mu’tashim, T. Muhayat, S. A. Damayanti, H. N. Zaki, and R. Wirawan, “Analisis Prediksi Harga Rumah Sesuai Spesifikasi Menggunakan Multiple Linear Regression,” Inform.  J. Ilmu Komput., vol. 17, no. 3, p. 238, 2021, doi: 10.52958/iftk.v17i3.3635.

[2]	A. Nata and Suparmadi, “Analisis Sistem Pendukung Keputusan Dengan Model Klasifikasi Berbasis Machine Learning Dalam Penentuan Penerima Program Indonesia Pintar,” J. Sci. Soc. Res., vol. 5, no. 3, p. 697, 2022, doi: 10.54314/jssr.v5i3.1041.

[3]	A. M. Ismail, “Cara Kerja Algoritma k-Nearest Neighbor ( k-NN ) Apa itu Algoritma k-Nearest Neighbor ?,” no. February, pp. 0–5, 2019.

[4]	N. L. Hanun and A. U. Zailani, “PENERAPAN ALGORITMA KLASIFIKASI RANDOM FOREST UNTUK PENENTUAN KELAYAKAN PEMBERIAN KREDIT DI KOPERASI MITRA SEJAHTERA,” J. Technol. Inf., vol. 5, no. 2, pp. 99–104, 2020.

[5]	A. Bisri and R. S. Wahono, “Penerapan Adaboost untuk Penyelesaian Ketidakseimbangan Kelas pada Penentuan Kelulusan Mahasiswa dengan Metode Decision Tree,” J. Intell. Syst., vol. 1, no. 1, pp. 27–32, 2015.
