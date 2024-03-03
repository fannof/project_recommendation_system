# Laporan Proyek Machine Learning - Novan Nur Hidayat

# PENGEMBANGAN SISTEM REKOMENDASI MAKANAN DENGAN ALGORITMA _CONTENT BASED FILTERING_ DAN _COLLABORATIVE FILTERING_

## Project Overview

- Latar belakang

  Makanan sangat penting bagi manusia, baik sebagai kebutuhan primer maupun sebagai komponen kehidupan sehari-hari seseorang. Kemerosotan ekonomi yang telah mempengaruhi beberapa industri telah menyebabkan peluang baru yang membuat industri kuliner, khususnya divisi _online_-nya, semakin sukses. Wisata kuliner menjadi hal terpenting di dunia kuliner. Memanfaatkan informasi yang tersedia di internet membuat banyak masyarakat lebih sulit untuk memilih kebutuhan mereka.

  _Overchoice_, juga dikenal sebagai _overload of choices_, adalah gangguan kognitif di mana orang merasa sulit untuk membuat keputusan ketika dihadapkan dengan sejumlah besar pilihan. Mereka sering memiliki banyak pilihan yang sangat melelahkan secara mental karena setiap opsi harus dipertimbangkan dengan cermat untuk memilih opsi terbaik. Selama periode kemajuan teknologi ini, setiap orang dihadapkan pada pilihan yang jumlahnya tak terbatas. Fenomena ini, yang dikenal sebagai _overload of choice_, semakin banyak terjadi dalam kehidupan sehari-hari, seperti memilih makanan di suatu restoran. Pelanggan disajikan dari berbagai pilihan menu, termasuk _snack_, _dessert_, _beverage_, dan makanan lainnya yang sesuai.

  Setiap item makanan dalam kategori tersebut memiliki rasa dan harga unik yang juga bervariasi. Pertimbangan-pertimbangan ini menciptakan kompleksitas dalam arti bahwa pengguna dipaksa untuk mengeluarkan lebih banyak waktu dan energi untuk mendapatkan makanan yang sesuai. Selain itu, akan timbul keraguan dan kecemasan yang akan  mengakibatkan  memilih makanan yang tidak  disukai dan takut  kecewa  akan  pilihannya. Berdasarkan masalah tersebut, Sistem Rekomendasi diperlukan untuk membantu dalam memilih makanan yang diinginkan.

  Sistem rekomendasi adalah sistem yang menyarankan informasi yang berguna atau menunjukkan apa yang perlu dilakukan oleh pengguna untuk mencapai tujuan, yang bisa berupa memilih produk yang diinginkan. Dengan demikian, pelanggan dapat memilih produk yang lebih mudah beradaptasi dan lebih efektif dalam mengevaluasi produk yang diperlukan. Secara umum, ada tiga sistem rekomendasi yang banyak digunakan yaitu: _Content Based (CB)_, _Collaborative Filtering (CF)_, dan _Hybrid_.

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

  Data yang digunakan dalam proyek ini bersumber dari [Kaggle-Food Recommendation System](https://www.kaggle.com/schemersays/food-recommendation-system)

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

### Variabel-variabel pada _Food Recommendation System_ adalah sebagai berikut:

Dataset _foods.csv_

- id_makanan : Nomor id dari masing-masing makanan.
- nama_makanan : Nama dari masing-masing makanan dari sebuah restoran ('summer squash salad' 'chicken minced salad' 'sweet chilli almonds'
 'tricolour salad' 'christmas cake' 'japanese curry arancini with barley salsa' 'chocolate nero cookies' etc).
- jenis_makanan : Jenis makanan apakah makanan tersebut termasuk 'Healthy_Food' 'Snack' 'Dessert' 'Japanese' 'Indian' 'French' 'Mexican'
 'Italian' 'Chinese' 'Beverage' 'Thai' 'Korean' 'Vietnames' 'Nepalese' 'Spanish'.
- veg_non : Mengidentifikasi apakah makanan tersebut termasuk dalam Vegan atau Non-Vegan.
- deskripsi : Deskripsi komposisi dari makanan.

Dataset _ratings.csv_

- user_id : Nomor id pelanggan yang memberikan rating pada makanan.
- id_makanan : Nomor id dari masing-masing makanan.
- rating : Rating dari pelanggan tentang makanan tersebut.

### Exploratory Data Analysis

- Menghapus _missing value_

  Dari hasil output, terlihat bahwa baris terakhir dataset _ratings.csv_ memiliki nilai _missing value_. Dengan menggunakan teknik _dropna_, sekarang _DataFrame_ ratings tidak mengandung baris dengan _missing value_.

  Tabel 6. Dataset sudah bersih dari _missing value_

  |     | user_id | id_makanan | rating |
  |----:|--------:|-----------:|-------:|
  |  0  |     1.0 |       88.0 |    4.0 |
  |  1  |     1.0 |       46.0 |    3.0 |
  |  2  |     1.0 |       24.0 |    5.0 |
  |  3  |     1.0 |       25.0 |    4.0 |
  |  4  |     2.0 |       49.0 |    1.0 |
  | ... |     ... |        ... |    ... |
  | 506 |    99.0 |       65.0 |    7.0 |
  | 507 |    99.0 |       22.0 |    1.0 |
  | 508 |   100.0 |       24.0 |   10.0 |
  | 509 |   100.0 |      233.0 |   10.0 |
  | 510 |   100.0 |       29.0 |    7.0 |

## Data Preparation

- Menggabungkan dataset _foods.csv_ dan _ratings.csv_

  Menggunakan _library pandas_ dan fungsi _merge()_ untuk menggabungkan dataset dengan kolom id_makanan sebagai acuan penggabungan.

  Tabel 7. Dataset setelah digabung

  |     | id_makanan |                                      nama_makanan | jenis_makanan | veg_non |                                          dskripsi | user_id | rating |
  |----:|-----------:|--------------------------------------------------:|--------------:|--------:|--------------------------------------------------:|--------:|--------|
  |  0  |          1 |                               summer squash salad |  Healthy_Food |     veg | white balsamic vinegar, lemon juice, lemon rin... |    49.0 |    5.0 |
  |  1  |          1 |                               summer squash salad |  Healthy_Food |     veg | white balsamic vinegar, lemon juice, lemon rin... |    71.0 |   10.0 |
  |  2  |          2 |                              chicken minced salad |  Healthy_Food | non-veg | olive oil, chicken mince, garlic (minced), oni... |     9.0 |    3.0 |
  |  3  |          2 |                              chicken minced salad |  Healthy_Food | non-veg | olive oil, chicken mince, garlic (minced), oni... |    22.0 |    5.0 |
  |  4  |          2 |                              chicken minced salad |  Healthy_Food | non-veg | olive oil, chicken mince, garlic (minced), oni... |    39.0 |   10.0 |
  | ... |        ... |                                               ... |           ... |     ... |                                               ... |     ... |    ... |
  | 597 |        396 |                                      Kimchi Toast |        Korean |     veg |  cream cheese, chopped kimchi, scallions,count... |     NaN |    NaN |
  | 598 |        397 | Tacos de Gobernador (Shrimp, Poblano, and Chee... |       Mexican | non-veg | poblano chiles, bacon, shrips, red salsa, garl... |     NaN |    NaN |
  | 599 |        398 |   Melted Broccoli Pasta With Capers and Anchovies |        French | non-veg |  broccoli,Bread Crumbs, anchovy fillets, garli... |     NaN |    NaN |
  | 600 |        399 |                 Lemon-Ginger Cake with Pistachios |       Dessert | non-veg | egg yolks,lemon juice, unsalted butter, all pu... |     NaN |    NaN |
  | 601 |        400 |                       Rosemary Roasted Vegetables |  Healthy_Food |     veg | kosher salt, rosemary, garlic, potato, olive o... |     NaN |    NaN |

    Pada tabel 7, setelah membuat _DataFrame_ baru bernama _foods_all_ yang terdiri gabungan dari dataset _foods.csv_ dan _ratings_csv_ ternyata terdapat total 91 _missing value_ pada fitur 'user_id' dan 'rating'. Langkah selanjutnya yaitu membersihkan _missing value_ tersebut dengan fungsi _dropna()_. Hasil dapat dilihat pada tabel 8 dengan total data yang tersisa sebanyak 511 baris.

  Tabel 8. Dataset _foods_all_ sudah bersih dari _missing value_

  |     | id_makanan |          nama_makanan | jenis_makanan | veg_non |                                         deskripsi | user_id | rating |
  |----:|-----------:|----------------------:|--------------:|--------:|--------------------------------------------------:|--------:|--------|
  |  0  |          1 |   summer squash salad |  Healthy_Food |     veg | white balsamic vinegar, lemon juice, lemon rin... |    49.0 |    5.0 |
  |  1  |          1 |   summer squash salad |  Healthy_Food |     veg | white balsamic vinegar, lemon juice, lemon rin... |    71.0 |   10.0 |
  |  2  |          2 |  chicken minced salad |  Healthy_Food | non-veg | olive oil, chicken mince, garlic (minced), oni... |     9.0 |    3.0 |
  |  3  |          2 |  chicken minced salad |  Healthy_Food | non-veg | olive oil, chicken mince, garlic (minced), oni... |    22.0 |    5.0 |
  |  4  |          2 |  chicken minced salad |  Healthy_Food | non-veg | olive oil, chicken mince, garlic (minced), oni... |    39.0 |   10.0 |
  | ... |        ... |                   ... |           ... |     ... |                                               ... |     ... |    ... |
  | 506 |        305 |            sunga pork |      Japanese |     veg |                                             curry |    56.0 |    9.0 |
  | 507 |        306 |          banana chips |         Snack |     veg | dried slices of bananas (fruits of herbaceous ... |    80.0 |    8.0 |
  | 508 |        307 |           bhurji- egg |        Indian | non-veg | made using indian spices, onion, tomatoes, gre... |    71.0 |    1.0 |
  | 509 |        308 | flattened rice / poha |        Indian |     veg | dehusked rice which is flattened into flat lig... |    97.0 |    3.0 |
  | 510 |        309 |           puffed rice |         Snack |     veg | grain made from rice; usually made by heating ... |    32.0 |    5.0 |

- Mengkonversi data pada kolom 'id_makanan', 'nama_makanan', dan 'jenis_makanan' menjadi bentuk _list_ dan membuat _dictionary_ untuk menentukan pasangan _key-value_ antara ketiga kolom tersebut. Hasil dapat dilihat pada tabel 9.

  Tabel 9. Data sudah siap untuk dimasukkan dalam permodelan

  |     | id_makanan |          nama_makanan | jenis_makanan |
  |----:|-----------:|----------------------:|--------------:|
  |  0  |          1 |   summer squash salad |  Healthy_Food |
  |  1  |          1 |   summer squash salad |  Healthy_Food |
  |  2  |          2 |  chicken minced salad |  Healthy_Food |
  |  3  |          2 |  chicken minced salad |  Healthy_Food |
  |  4  |          2 |  chicken minced salad |  Healthy_Food |
  | ... |        ... |                   ... |           ... |
  | 506 |        305 |            sunga pork |      Japanese |
  | 507 |        306 |          banana chips |         Snack |
  | 508 |        307 |           bhurji- egg |        Indian |
  | 509 |        308 | flattened rice / poha |        Indian |
  | 510 |        309 |           puffed rice |         Snack |

- _TF-IDF Vectorizer_

  Teknik untuk pembobotan kata-kata disebut _Term Frequency-Inverse Document Frequency (TF-IDF)_, yang menentukan seberapa sering sebuah kata muncul di setiap dokumen serta di semua dokumen. _Term Frequency (TF)_ dan _Inverse Document Frequency (IDF)_ membentuk TF-IDF. Nilai yang disebut "_Term Frequency_" menunjukkan seberapa sering istilah tertentu muncul dalam dokumen. Berat istilah meningkat seiring dengan berapa kali istilah tersebut muncul dalam dokumen. Tujuan dari _Inverse Document Frequency (IDF)_ adalah untuk mengurangi bobot istilah jika muncul di setiap dokumen. Berbeda dengan _TF_, nilainya meningkat dengan menurunnya frekuensi kata dalam dokumen. Setelah _TF-IDF_ diterapkan pada 'nama_makanan' dan 'jenis_makanan', hasilnya terdapat pada tabel 10.

  Tabel 10. _Output_ matriks _TF-IDF_

  |                                            | japanese | italian | mexican | chinese | snack | beverage | indian | dessert | thai | healthy_food |
  |-------------------------------------------:|---------:|--------:|--------:|--------:|------:|---------:|-------:|--------:|-----:|--------------|
  |                               nama_makanan |          |         |         |         |       |          |        |         |      |              |
  |             malabari fish curry            |      0.0 |     0.0 |     0.0 |     0.0 |   0.0 |      0.0 |    1.0 |     0.0 |  0.0 |          0.0 |
  | mustard-parmesan whole roasted cauliflower |      0.0 |     0.0 |     0.0 |     0.0 |   0.0 |      0.0 |    0.0 |     0.0 |  0.0 |          1.0 |
  |           banana walnut smoothie           |      0.0 |     0.0 |     0.0 |     0.0 |   0.0 |      0.0 |    0.0 |     0.0 |  0.0 |          1.0 |
  |            chicken gilafi kebab            |      0.0 |     0.0 |     0.0 |     0.0 |   0.0 |      0.0 |    1.0 |     0.0 |  0.0 |          0.0 |
  |               fish ambultiyal              |      0.0 |     0.0 |     0.0 |     0.0 |   0.0 |      0.0 |    1.0 |     0.0 |  0.0 |          0.0 |
  |               easy bread poha              |      0.0 |     0.0 |     0.0 |     0.0 |   0.0 |      0.0 |    1.0 |     0.0 |  0.0 |          0.0 |
  |                 fish curry                 |      0.0 |     0.0 |     0.0 |     0.0 |   0.0 |      0.0 |    0.0 |     0.0 |  1.0 |          0.0 |
  |                red rice poha               |      0.0 |     0.0 |     0.0 |     0.0 |   0.0 |      0.0 |    1.0 |     0.0 |  0.0 |          0.0 |
  |           grilled lemon margarita          |      0.0 |     0.0 |     0.0 |     0.0 |   0.0 |      1.0 |    0.0 |     0.0 |  0.0 |          0.0 |
  |              broccoli souffle              |      0.0 |     1.0 |     0.0 |     0.0 |   0.0 |      0.0 |    0.0 |     0.0 |  0.0 |          0.0 |
  |                    rice                    |      0.0 |     0.0 |     0.0 |     0.0 |   0.0 |      0.0 |    1.0 |     0.0 |  0.0 |          0.0 |
  |               beetroot modak               |      1.0 |     0.0 |     0.0 |     0.0 |   0.0 |      0.0 |    0.0 |     0.0 |  0.0 |          0.0 |
  |              sweet potato pie              |      0.0 |     0.0 |     0.0 |     0.0 |   0.0 |      0.0 |    0.0 |     1.0 |  0.0 |          0.0 |

  _Output_ matriks _TF-IDF_ pada tabel 10 menunjukkan makanan _mustard-parmesan whole roasted cauliflower_ memiliki kategori 'healthy_food'. Hal ini terlihat dari nilai matriks 1.0 pada kategori 'healthy_food'. Selanjutnya, makanan _chicken gilafi kebab_ termasuk dalam kategori 'indian'. Sedangkan, _makanan beetroot modak_ termasuk dalam kategori 'japanese'. Demikian seterusnya. 

- _Cosine Similarity_

  Kosinus sudut yang dibentuk oleh dua benda atau vektor dalam ruang dimensi-n ditentukan oleh skor _cosine similarity_. Sudut antara vektor riwayat berita pembaca pada data uji dan pembaca pada data pelatihan ditentukan dengan menggunakan skor _cosine similarity_. Kedua vektor identik jika sudutnya nol atau skor kosinus adalah 1. Sebaliknya, kedua vektor berbeda secara signifikan satu sama lain jika skor kosinus menampilkan -1, atau sudut 180 derajat. Pada tahap ini, dihitung _cosine similarity dataframe tfidf_matrix_ yang telah diperoleh pada tahapan sebelumnya. Dengan satu baris kode untuk memanggil fungsi _cosine similarity_ dari _library sklearn_, telah berhasil menghitung kesamaan _(similarity)_ antar makanan. Kode akan menghasilkan _output_ berupa matriks kesamaan dalam bentuk _array_. 

  Tabel 11. _Output_ hasil perhitungan _cosine similirarity_

   |                 nama_makanan | malabari fish curry | grilled lemon margarita | dahi chicken | chicken palwal | braised lamb shanks | hot chocolate | sweet potato and quinoa bowl | baked multigrain murukku | duo of chocolate and strawberry | lemon poppy seed cake | lamb korma | detox haldi tea | baked shankarpali | camel milk cake tart | holi special malai kofta |
  |-----------------------------:|--------------------:|------------------------:|-------------:|---------------:|--------------------:|--------------:|-----------------------------:|-------------------------:|--------------------------------:|----------------------:|-----------:|----------------:|------------------:|---------------------:|-------------------------:|
  |                 nama_makanan |                     |                         |              |                |                     |               |                              |                          |                                 |                       |            |                 |                   |                      |                          |
  |      bread chana basket      |                 1.0 |                     0.0 |          1.0 |            1.0 |                 0.0 |           0.0 |                          0.0 |                      0.0 |                             0.0 |                   0.0 |        1.0 |             0.0 |               0.0 |                  0.0 |                      1.0 |
  |     cream of almond soup     |                 0.0 |                     0.0 |          0.0 |            0.0 |                 0.0 |           0.0 |                          1.0 |                      0.0 |                             0.0 |                   0.0 |        0.0 |             0.0 |               0.0 |                  0.0 |                      0.0 |
  |    chocolate fudge cookies   |                 0.0 |                     0.0 |          0.0 |            0.0 |                 0.0 |           0.0 |                          0.0 |                      0.0 |                             1.0 |                   1.0 |        0.0 |             0.0 |               0.0 |                  1.0 |                      0.0 |
  |  moong dal kiwi coconut soup |                 1.0 |                     0.0 |          1.0 |            1.0 |                 0.0 |           0.0 |                          0.0 |                      0.0 |                             0.0 |                   0.0 |        1.0 |             0.0 |               0.0 |                  0.0 |                      1.0 |
  |  spicy creamy kadai chicken  |                 1.0 |                     0.0 |          1.0 |            1.0 |                 0.0 |           0.0 |                          0.0 |                      0.0 |                             0.0 |                   0.0 |        1.0 |             0.0 |               0.0 |                  0.0 |                      1.0 |
  |      bengali lamb curry      |                 1.0 |                     0.0 |          1.0 |            1.0 |                 0.0 |           0.0 |                          0.0 |                      0.0 |                             0.0 |                   0.0 |        1.0 |             0.0 |               0.0 |                  0.0 |                      1.0 |
  |    orange quinoa sevaiyan    |                 0.0 |                     0.0 |          0.0 |            0.0 |                 0.0 |           0.0 |                          1.0 |                      0.0 |                             0.0 |                   0.0 |        0.0 |             0.0 |               0.0 |                  0.0 |                      0.0 |
  |         hot chocolate        |                 0.0 |                     1.0 |          0.0 |            0.0 |                 0.0 |           1.0 |                          0.0 |                      0.0 |                             0.0 |                   0.0 |        0.0 |             1.0 |               0.0 |                  0.0 |                      0.0 |
  | sweet potato and quinoa bowl |                 0.0 |                     0.0 |          0.0 |            0.0 |                 0.0 |           0.0 |                          1.0 |                      0.0 |                             0.0 |                   0.0 |        0.0 |             0.0 |               0.0 |                  0.0 |                      0.0 |
  |    ragi oats ladoo (laddu)   |                 0.0 |                     0.0 |          0.0 |            0.0 |                 0.0 |           0.0 |                          0.0 |                      0.0 |                             1.0 |                   1.0 |        0.0 |             0.0 |               0.0 |                  1.0 |                      0.0 |
  |        chicken biryani       |                 1.0 |                     0.0 |          1.0 |            1.0 |                 0.0 |           0.0 |                          0.0 |                      0.0 |                             0.0 |                   0.0 |        1.0 |             0.0 |               0.0 |                  0.0 |                      1.0 | 

  Pada tabel 11, Angka 1.0 mengindikasikan bahwa makanan pada kolom X (horizontal) memiliki kesamaan dengan makanan pada baris Y (vertikal). Sebagai contoh, makanan _bread chana basket_ dan _moong dal kiwi coconut soup_ teridentifikasi sama (similar) dengan makanan _malabari fish curry_. Contoh lain, makanan _spicy creamy kadai chicken_ teridentifikasi mirip dengan makanan _dahi chicken_. 

- _Train-Test-Split_

  Proses membagi himpunan data menjadi data pelatihan dan pengujian adalah langkah yang diperlukan sebelum membuat model. Hal ini penting dilakukan untuk memperkuat semua data yang tersedia untuk menilai beberapa generalisasi model ke data baru. Tercatat bahwa setiap transformasi data yang dilakukan juga berfungsi sebagai komponen model. Karena data _test set_ (uji) mentah, semua transformasi harus dilakukan pada data latih. Data dibagi menjadi 80% data _training_ dan 20% data _testing_.

 [[ 35  19]
 [ 60 232]
 [ 66 244]
 ...
 [ 73  52]
 [ 30  64]
 [ 61 235]] [0.22222222 0.55555556 0.11111111 0.22222222 0.33333333 ... ] 

- Proses _encoding_

  Pada tahap ini diperlukan proses menyandikan _(encode)_ fitur ‘user_id’ dan ‘id_makanan’ ke dalam indeks integer. Memetakan ‘user_id’ dan ‘id_makanan’ ke _dataframe_ yang berkaitan. Mengecek beberapa hal dalam data seperti jumlah user, jumlah makanan, kemudian mengubah nilai rating menjadi float.

  - 100
  - 309
  - Number of User: 100, Number of Food: 309, Min Rating: 1.0, Max Rating: 10.0

### Penjelasan tahapan dan kenapa harus dilakukan proses tersebut

- Proses _data prepraration_

  Pertama adalah proses _train-test-split_. Data dibagi menjadi 80% _data training_ dan 20% _data testing_, karena jumlah seluruh data termasuk kecil, maka diperlukan lebih banyak data latih.

  Proses _standarisasi_ mengubah nilai mean menjadi 0 dan std menjadi 1. _StandardScaler_ melakukan proses _standardisasi_ parameter fitur terlebih dahulu dengan mengurangkan nilai _mean_ (nilai rata-rata) dan kemudian membandingkannya dengan standar deviasi untuk menentukan distribusi.  _StandardScaler_ menghasilkan distribusi dengan rata-rata 0 dan standar deviasi 1.

  Tahapan diatas penting dilakukan karena algoritma _machine learning_ memiliki performa lebih baik ketika dimodelkan pada data dengan skala relatif sama atau mendekati distribusi normal.

## Modeling

Model akan dikembangkan dengan 2 metode yang berbeda. Kedua metode tersebut adalah sebagai berikut:

1. _Content Based Filtering_

     Sistem rekomendasi _Content Based Filtering_ menyarankan produk yang mirip dengan produk yang disukai pengguna sebelumnya. Nilai item ditentukan dengan mempertimbangkan fitur yang ada di setiap konten. Sistem rekomendasi _knowledge-based_ menyarankan item berdasarkan pengetahuan domain pengguna tentang fitur apa yang tersedia dalam item dan bagaimana pengguna dapat memenuhi kebutuhan dan berguna bagi pengguna. Nilai kesamaan dihitung berdasarkan besarnya nilai kesamaan antara kebutuhan pengguna dan rekomendasi yang ada. Ada dua pendekatan yang tersedia dalam metode rekomendasi _knowledge-based_ yaitu _case based_ dan _constraint-based_. Kesamaan antara kedua pendekatan ini adalah bahwa pengguna harus mengirimkan permintaan sesegera mungkin.  Selanjutnya, sistem akan mengidentifikasi solusi yang paling sesuai dengan kebutuhan pengguna. Seperti yang terlihat pada gambar 3.

   Gambar 3. Metode _Content Based Filtering_

   ![CBF](https://github.com/fannof/project_recommendation_system/assets/99071605/7051df06-72cd-42cf-8e1a-7474475ec6d3)

   _(Sumber: https://www.google.com/url?sa=i&url=https%3A%2F%2Fdqlab.id)_

    Mendapatkan rekomendasi dengan metode _content based filtering_
  
     Setelah memiliki data similarity (kesamaan) antar makanan, tahap selanjutnya ialah menghasilkan sejumlah makanan yang akan direkomendasikan kepada pelanggan. Membuat fungsi food_recommendations dengan beberapa parameter sebagai berikut:

   - makanan : Nama makanan (index kemiripan dataframe).
   - Similarity_data : Dataframe mengenai similarity yang telah didefinisikan sebelumnya.
   - Items : Nama dan fitur yang digunakan untuk mendefinisikan kemiripan, dalam hal ini adalah ‘nama_makanan’ dan ‘jenis_makanan’.
   - k : Banyak rekomendasi yang ingin diberikan (dalam kasus ini adalah 5).
  
   Percobaan pertama adalah rekomendasi makanan yang mirip dengan _sweet potato pie_:
  
   Tabel 12. Mencari reomendasi yang mirip dengan makanan _sweet potato pie_

   |     | id_makanan |     nama_makanan | jenis_makanan |
   |----:|-----------:|-----------------:|---------------|
   | 413 |        225 | sweet potato pie |       Dessert |

   _sweet potato pie_ masuk dalam kategori jenis makanan dessert. Tentunya diharapkan rekomendasi yang diberikan adalah makanan dengan kategori yang mirip. Lalu panggil fungsi food_recommendations. Hasilnya dapat dilihat pada tabel 13.

   Tabel 13. Mendapatkan reomendasi yang mirip dengan makanan _sweet potato pie_

   |   |                      nama_makanan | jenis_makanan |
   |--:|----------------------------------:|--------------:|
   | 0 |           chocolate fudge cookies |       Dessert |
   | 1 |              homemade gulab jamun |       Dessert |
   | 2 | jalebi with fennel yogurt pudding |       Dessert |
   | 3 |   double chocolate easter cookies |       Dessert |
   | 4 |           eggless coffee cupcakes |       Dessert |

2. _Collaborative Filtering_

      Metode _Collaborative Filtering_ adalah teknik yang memberikan rekomendasi berdasarkan preferensi pengguna atau item serupa lainnya.  Dua jenis metode _Collaborative Filtering_ dibedakan menjadi: _User Based CF_ dan _Item Based CF_. _User-Based Collaborative Filtering_ menyatakan bahwa cara terbaik untuk menemukan item menarik bagi pengguna adalah dengan mencari pengguna lain yang memiliki minat atau kebutuhan yang sama. Algoritma _User Based CF_ dapat mengidentifikasi pengguna yang mirip satu sama lain _(user neighbor)_ dengan mengidentifikasi pengguna yang berbeda satu sama lain _(user similarity)_. Setiap rating yang didapatkan dari pengguna yang bertetangga kemudian akan dijadikan mesin rekomendasi bagi pengguna aktif. Seperti yang terlihat pada gambar 4.

   Gambar 4. _Collaborative Filtering_

   ![CF](https://github.com/fannof/project_recommendation_system/assets/99071605/5b839287-f715-4b06-abd4-bf1bce8759c4)

   _(Sumber: https://www.google.com/url?sa=i&url=https%3A%2F%2Fdqlab.id)_

   Di sisi lain, _Item-Based Collaborative Filtering_ memiliki struktur yang mirip dengan _User Based C_. Jika pemfilteran _user-based_ sebelumnya menunjukkan korelasi _user_ ke _user_, maka pemfilteran _item-based_ akan menunjukkan korelasi item yang diminati oleh sistem pengguna lain. Item-item akan terus terakumulasi. Salah satu keuntungan dari metode _item-based  collaborative  filtering_ adalah kemampuannya untuk mengeksplorasi jejaring sosial implisit, yang berpotensi meningkatkan akurasi rekomendasi yang dibuat.

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
