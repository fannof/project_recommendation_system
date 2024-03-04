# Laporan Proyek Machine Learning - Novan Nur Hidayat

# PENGEMBANGAN SISTEM REKOMENDASI MAKANAN DENGAN ALGORITMA _CONTENT BASED FILTERING_ DAN _COLLABORATIVE FILTERING_

## Project Overview

- Latar belakang

  Makanan sangat penting bagi manusia, baik sebagai kebutuhan primer maupun sebagai komponen kehidupan sehari-hari seseorang. Kemerosotan ekonomi yang telah mempengaruhi beberapa industri telah menyebabkan peluang baru yang membuat industri kuliner, khususnya divisi _online_-nya, semakin sukses. Wisata kuliner menjadi hal terpenting di dunia kuliner. Memanfaatkan informasi yang tersedia di internet membuat banyak masyarakat lebih sulit untuk memilih kebutuhan mereka [1].

  _Overchoice_, juga dikenal sebagai _overload of choices_, adalah gangguan kognitif di mana orang merasa sulit untuk membuat keputusan ketika dihadapkan dengan sejumlah besar pilihan. Mereka sering memiliki banyak pilihan yang sangat melelahkan secara mental karena setiap opsi harus dipertimbangkan dengan cermat untuk memilih opsi terbaik. Selama periode kemajuan teknologi ini, setiap orang dihadapkan pada pilihan yang jumlahnya tak terbatas. Fenomena ini, yang dikenal sebagai _overload of choice_, semakin banyak terjadi dalam kehidupan sehari-hari, seperti memilih makanan di suatu restoran. Pelanggan disajikan dari berbagai pilihan menu, termasuk _snack_, _dessert_, _beverage_, dan makanan lainnya yang sesuai [2].

  Setiap item makanan dalam kategori tersebut memiliki rasa dan harga unik yang juga bervariasi. Pertimbangan-pertimbangan ini menciptakan kompleksitas dalam arti bahwa pengguna dipaksa untuk mengeluarkan lebih banyak waktu dan energi untuk mendapatkan makanan yang sesuai. Selain itu, akan timbul keraguan dan kecemasan yang akan  mengakibatkan  memilih makanan yang tidak  disukai dan takut  kecewa  akan  pilihannya. Berdasarkan masalah tersebut, Sistem Rekomendasi diperlukan untuk membantu dalam memilih makanan yang diinginkan [2].

  Sistem rekomendasi adalah sistem yang menyarankan informasi yang berguna atau menunjukkan apa yang perlu dilakukan oleh pengguna untuk mencapai tujuan, yang bisa berupa memilih produk yang diinginkan. Dengan demikian, pelanggan dapat memilih produk yang lebih mudah beradaptasi dan lebih efektif dalam mengevaluasi produk yang diperlukan. Secara umum, ada tiga sistem rekomendasi yang banyak digunakan yaitu: _Content Based (CB)_, _Collaborative Filtering (CF)_, dan _Hybrid_ [1].

- Rumusan Masalah dan Solusi Permasalahan

  Banyaknya pilihan makanan yang tersedia di restoran dapat membuat pelanggan yang berkunjung merasa ragu untuk memilih makanan, dan fenomena _overchoice_ pun tidak dapat dihindari. Salah satu solusi untuk memastikan kepuasan pelanggan adalah pelayan atau pramusaji merekomendasikan item menu kepada pelanggan. Namun, ini juga menyebabkan mereka menjadi letih dan gagal mengenali preferensi setiap pelanggan. Tidak setiap pelanggan memiliki preferensi yang sama dengan pelayan atau pramusaji. Sebaliknya, setiap pelanggan memiliki preferensi unik yang berbeda dari pelanggan lain, serta lamanya waktu yang dibutuhkan oleh pelanggan yang mengalami fenomena _overchoice_, yang menyebabkan pelayan menjadi 'menyerah' ketika melayani pelanggan.

  Karena itu, sistem rekomendasi _hybrid_ diperlukan untuk menyarankan makanan yang tersedia di restoran kepada pelanggan untuk membantu mereka dalam memilih makanan yang mereka inginkan, menghemat waktu mereka ketika pemesanan menu, dan membantu restoran dalam memahami perilaku pelanggan. Dalam  proyek ini, peneliti mengabaikan semua menu minuman pada restoran dikarenakan jumlah menu minuman yang tersedia pada restoran hanya tersedia beberapa buah menu minuman dan dianggap terlalu sedikit untuk dimasukkan kedalam sistem yang baru.

- Hasil Riset Terkait

  Dalam jurnal yang berjudul "SISTEM REKOMENDASI MENU MINUMAN DENGAN METODE _CONTENT–BASED FILTERING_ BERBASIS _ANDROID_ PADA MUBTADA KOPI" yang dipublikasikan oleh Kosim dan Reza Prihandi(2024) dijelaskan bahwa _Overchoice_ adalah gangguan kognitif di mana orang mengalami kesulitan membuat keputusan ketika dihadapkan dengan banyak pilihan, memiliki terlalu banyak pilihan yang setara sangat menguras mental karena setiap pilihan harus mempertimbangkan beberapa alternatif untuk memilih pilihan yang terbaik. Pada masa perkembangan teknologi  ini dimana setiap harinya semua orang dihadapkan oleh pilihan yang tidak terhingga jumlahnya, fenomena _overchoice_ ini kerap terjadi dalam kehidupan sehari–hari seperti memilih minuman pada salah satu kedai café, maka dari itu _Recommendation System_ diperlukan untuk membantu dalam memilih minuman yang ingin dipesan dan untuk membantu dalam memilih pilihan lainnya. Teknik _content–based filtering_ akan mencoba mengambil preferensi pengguna secara eksplisit yaitu meminta pengguna untuk memilih preferensi yang diinginkan pengguna dari ke-6 fitur yang sudah dibuat sebelumnya lalu dihitung kecocokan preferensi pengguna dengan ke-6 fitur pada masing-masing–masing item menggunakan rumus _dotmatrix_. Setelah mendapatkan hasilnya, angka tersebut akan dirubah menjadi sebuah rating agar sesuai dengan pendekatan _Recommendation System_ yaitu _best rated_ yang dibuat secara _non-personalized_. Rating ini merupakan indikasi kecocokan preferensi pengguna dengan item yang terdapat pada daftar menu Mubtada Kopi. Semakin besar ratingnya, semakin cocok dengan preferensi pengguna [2].

## Business Understanding

### Problem Statements

- Apakah sistem rekomendasi _hybrid_ dapat menjadi solusi yang efektif untuk merekomendasikan makanan kepada pelanggan yang sesuai dengan keinginannya?

- Bagaimana tahapan dalam pembuatan sistem rekomendasi _hybrid_ yang akan merekomendasikan makanan sesuai preferensi pelanggan?

### Goals

- Tujuan yang dimaksudkan adalah untuk membantu pelayan agar tidak bingung dalam merekomendasikan makanan, dikarenakan selera orang terkadang berbeda-beda. Solusi yang dihasilkan harus dapat memaksimalkan rekomendasi yang diberikan sekaligus memastikan rekomendasi tersebut dapat diterima dengan baik oleh pelanggan.

- Tujuan utamanya adalah untuk mengembangkan model atau sistem rekomendasi yang dapat mengidentifikasi dan merekomendasikan makanan untuk menyesuaikan dengan preferensi pelanggan. Tujuan proses rekomendasi ini adalah untuk memberikan lebih banyak makanan yang sesuai minat dan bagaimana mengidentifikasi karakteristik pelanggan, seperti makanan yang disukai sebelumnya dan kemiripan selera dengan pelanggan lain yang mempengaruhi nilai rekomendasi.

### Solution Approach

- Menggunakan pendekatan _Content Based Filtering_ untuk merekomendasikan makanan ke pelanggan sesuai minat sebelumnya dan _Collaborative Filtering_ untuk merekomendasikan makanan ke pelanggan sesuai persamaan kesukaan dengan pelanggan lain. Hal ini bertujuan untuk melakukan rekomendasi dengan memanfaatkan kekuatan masing-masing model. Evaluasi model dapat menggunakan metrik seperti _Precision_ dan _Root Mean Squared Error (RMSE)_ untuk mengukur seberapa baik model merekomendasi makanan.

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
- nama_makanan : Nama dari masing-masing makanan dari sebuah restoran.
- jenis_makanan : Jenis makanan apakah makanan tersebut termasuk 'Healthy_Food' 'Snack' 'Dessert' 'Japanese' 'Indian' 'French' 'Mexican'
 'Italian' 'Chinese' 'Beverage' 'Thai' 'Korean' 'Vietnames' 'Nepalese' 'Spanish'.
- veg_non : Mengidentifikasi apakah makanan tersebut termasuk dalam Vegan atau Non-Vegan.
- deskripsi : Deskripsi komposisi dari makanan.

Dataset _ratings.csv_

- user_id : Nomor id pelanggan yang memberikan rating pada makanan.
- id_makanan : Nomor id dari masing-masing makanan.
- rating : Rating dari pelanggan tentang makanan tersebut.

### Exploratory Data Analysis

- Variabel nama_makanan

  Setelah variabel nama_makanan dieskplorasi, terdapat total 400 jumlah data makanan yang unik, diantaranya adalah sebagai berikut:

  'summer squash salad' 'chicken minced salad' 'sweet chilli almonds' 'tricolour salad' 'christmas cake' 'japanese curry arancini with barley salsa' 'chocolate nero cookies' 'lamb and chargrilled bell pepper soup' 'cream of almond soup''broccoli and almond soup' 'coconut lime quinoa salad' 'lemon honey glazed sous vide corn on the cob' 'watermelon and strawberry smoothie' 'peach, raspberry and nuts smoothie' 'almond and cranberry poha' 'almond and raw banana galawat' etc.

- Variabel jenis_makanan

  Setelah variabel nama_makanan dieksplorasi, terdapat total 15 jumlah data jenis makanan yang unik, diantaranya adalah:

  'Healthy_Food' 'Snack' 'Dessert' 'Japanese' 'Indian' 'French' 'Mexican' 'Italian' 'Chinese' 'Beverage' 'Thai' 'Korean' 'Vietnames' 'Nepalese' 'Spanish'.

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

  Teknik untuk pembobotan kata-kata disebut _Term Frequency-Inverse Document Frequency (TF-IDF)_, yang menentukan seberapa sering sebuah kata muncul di setiap dokumen serta di semua dokumen. _Term Frequency (TF)_ dan _Inverse Document Frequency (IDF)_ membentuk TF-IDF. Nilai yang disebut "_Term Frequency_" menunjukkan seberapa sering istilah tertentu muncul dalam dokumen. Berat istilah meningkat seiring dengan berapa kali istilah tersebut muncul dalam dokumen. **Hal ini penting dilakukan** karena tujuan dari _Inverse Document Frequency (IDF)_ adalah untuk mengurangi bobot istilah jika muncul di setiap dokumen. Berbeda dengan _TF_, nilainya meningkat dengan menurunnya frekuensi kata dalam dokumen [3]. Setelah _TF-IDF_ diterapkan pada 'nama_makanan' dan 'jenis_makanan', hasilnya terdapat pada tabel 10.

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

  Kosinus sudut yang dibentuk oleh dua benda atau vektor dalam ruang dimensi-n ditentukan oleh skor _cosine similarity_. Sudut antara vektor riwayat berita pembaca pada data uji dan pembaca pada data pelatihan ditentukan dengan menggunakan skor _cosine similarity_. Kedua vektor identik jika sudutnya nol atau skor kosinus adalah 1. Sebaliknya, kedua vektor berbeda secara signifikan satu sama lain jika skor kosinus menampilkan -1, atau sudut 180 derajat. **Pada tahap ini, penting dilakukan** dengan menghitung _cosine similarity dataframe tfidf_matrix_ yang telah diperoleh pada tahapan sebelumnya. Dengan satu baris kode untuk memanggil fungsi _cosine similarity_ dari _library sklearn_, telah berhasil menghitung kesamaan _(similarity)_ antar makanan. Kode akan menghasilkan _output_ berupa matriks kesamaan dalam bentuk _array_ [3]. 

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

  Proses membagi himpunan data menjadi data pelatihan dan pengujian adalah langkah yang diperlukan sebelum membuat model. **Hal ini penting** dilakukan untuk memperkuat semua data yang tersedia untuk menilai beberapa generalisasi model ke data baru. Tercatat bahwa setiap transformasi data yang dilakukan juga berfungsi sebagai komponen model. Karena data _test set_ (uji) mentah, semua transformasi harus dilakukan pada data latih. Data dibagi menjadi 80% data _training_ dan 20% data _testing_.

   [[ 35  19]
  
   [ 60 232]
 
   [ 66 244]
 
   ...
 
   [ 73  52]
 
   [ 30  64]
 
   [ 61 235]] [0.22222222 0.55555556 0.11111111 0.22222222 0.33333333 ... ] 

- Proses _encoding_

  **Pada tahap ini diperlukan** proses menyandikan _(encode)_ fitur ‘user_id’ dan ‘id_makanan’ ke dalam indeks integer. Memetakan ‘user_id’ dan ‘id_makanan’ ke _dataframe_ yang berkaitan. Mengecek beberapa hal dalam data seperti jumlah user, jumlah makanan, kemudian mengubah nilai rating menjadi float.

  - 100
  - 309
  - Number of User: 100, Number of Food: 309, Min Rating: 1.0, Max Rating: 10.0

## Modeling

Model akan dikembangkan dengan 2 metode yang berbeda. Kedua metode tersebut adalah sebagai berikut:

1. _Content Based Filtering_

     Sistem rekomendasi _Content Based Filtering_ menyarankan produk yang mirip dengan produk yang disukai pengguna sebelumnya. Nilai item ditentukan dengan mempertimbangkan fitur yang ada di setiap konten. Sistem rekomendasi _knowledge-based_ menyarankan item berdasarkan pengetahuan domain pengguna tentang fitur apa yang tersedia dalam item dan bagaimana pengguna dapat memenuhi kebutuhan dan berguna bagi pengguna. Nilai kesamaan dihitung berdasarkan besarnya nilai kesamaan antara kebutuhan pengguna dan rekomendasi yang ada. Ada dua pendekatan yang tersedia dalam metode rekomendasi _knowledge-based_ yaitu _case based_ dan _constraint-based_. Kesamaan antara kedua pendekatan ini adalah bahwa pengguna harus mengirimkan permintaan sesegera mungkin.  Selanjutnya, sistem akan mengidentifikasi solusi yang paling sesuai dengan kebutuhan pengguna [1]. Seperti yang terlihat pada gambar 3.

   ![CBF](https://github.com/fannof/project_recommendation_system/assets/99071605/7051df06-72cd-42cf-8e1a-7474475ec6d3)

   Gambar 1. Metode _Content Based Filtering_

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

      Metode _Collaborative Filtering_ adalah teknik yang memberikan rekomendasi berdasarkan preferensi pengguna atau item serupa lainnya.  Dua jenis metode _Collaborative Filtering_ dibedakan menjadi: _User Based CF_ dan _Item Based CF_. _User-Based Collaborative Filtering_ menyatakan bahwa cara terbaik untuk menemukan item menarik bagi pengguna adalah dengan mencari pengguna lain yang memiliki minat atau kebutuhan yang sama. Algoritma _User Based CF_ dapat mengidentifikasi pengguna yang mirip satu sama lain _(user neighbor)_ dengan mengidentifikasi pengguna yang berbeda satu sama lain _(user similarity)_. Setiap rating yang didapatkan dari pengguna yang bertetangga kemudian akan dijadikan mesin rekomendasi bagi pengguna aktif [1]. Seperti yang terlihat pada gambar 4.

   ![CF](https://github.com/fannof/project_recommendation_system/assets/99071605/5b839287-f715-4b06-abd4-bf1bce8759c4)

   Gambar 2. Metode _Collaborative Filtering_

   _(Sumber: https://www.google.com/url?sa=i&url=https%3A%2F%2Fdqlab.id)_

   Di sisi lain, _Item-Based Collaborative Filtering_ memiliki struktur yang mirip dengan _User Based C_. Jika pemfilteran _user-based_ sebelumnya menunjukkan korelasi _user_ ke _user_, maka pemfilteran _item-based_ akan menunjukkan korelasi item yang diminati oleh sistem pengguna lain. Item-item akan terus terakumulasi. Salah satu keuntungan dari metode _item-based  collaborative  filtering_ adalah kemampuannya untuk mengeksplorasi jejaring sosial implisit, yang berpotensi meningkatkan akurasi rekomendasi yang dibuat.

   Mendapatkan rekomendasi makanan dengan metode _Collaborative Filtering_

   Tahap pertama yaitu ambil sampel user secara acak dan definisikan variabel food_not_displayed yang merupakan daftar makanan yang belum pernah dilihat oleh pelanggan. Hal ini dilakukan karena daftar food_not_displayed inilah yang akan menjadi makanan yang direkomendasikan.

    10/10 [==============================] - 0s 2ms/step
   
    Showing recommendations for users: 59.0
   
    ===========================

    Food with high ratings from user

    --------------------------------

    beetroot modak : Japanese

    spicy chicken masala : Indian

    corn pulao : Indian

    homemade gulab jamun : Dessert

    jalapeno cheese fingers : Mexican

    --------------------------------

    Top 10 food recommendation

    --------------------------------

    sweet potato and quinoa bowl : Healthy_Food

    corn and raw mango salad : Healthy_Food

    andhra pan fried pomfret : Indian

    christmas chocolate fudge cookies : Dessert

    chicken parmigiana with tomato sauce : Italian

    pesto fish kebabs : Indian

    crunchy vegetable dal sattu croquettes : Italian

    active charcoal modak : Japanese

    flax seed and beetroot modak : Japanese

    black rice : Healthy_Food

   Hasil di atas adalah rekomendasi untuk user dengan id 59. Dari _output_ tersebut, didapat perbandingan antara _food with high ratings from user_ dan _Top 10 food recommendation_ untuk user.

      Beberapa makanan rekomendasi menyediakan kategori jenis makanan yang sesuai dengan rating user. Diperoleh 2 rekomendasi makanan dengan kategori jenis makanan 'Indian', 3 rekomendasi makanan dengan kategori 'Healthy_Food', 1 rekomendasi makanan kategori 'Dessert', 2 rekomendasi makanan kategori 'Japanese', dan 2 makanan dengan kategori 'Italian'.

  - Kelebihan dan kekurangan _Content-Based Filtering_:

    -- Kelebihan : Personalisasi yang tinggi, metode ini menawarkan rekomendasi yang dipersonalisasi berdasarkan preferensi pengguna dan tidak memerlukan data eksternal, _Content-based filtering_ tidak memerlukan data eksternal atau informasi tentang pengguna lain.

    -- Kekurangan : Keterbatasan dalam diversifikasi, _Content-based filtering_ cenderung merekomendasikan item yang sangat mirip dengan item yang telah dipilih pengguna sebelumnya dan mempunyai keterbatasan representasi fitur, efektivitas _content-based filtering_ sangat bergantung pada kualitas representasi fitur item.

  - Kelebihan dan kekurangan _Collaborative Filtering_:

    -- Kelebihan : Tidak memerlukan informasi produk, metode ini tidak memerlukan informasi eksternal tentang item untuk memberikan rekomendasi dan dapat menganalisis interaksi pengguna, metode ini memanfaatkan interaksi pengguna dengan item untuk membuat rekomendasi. 

    -- Kekurangan : Masalah ketergantungan pada data historis, rekomendasi dalam _collaborative filtering_ sangat bergantung pada data historis interaksi pengguna dengan item dan permasalahan sparsitas data, _Collaborative filtering_ dapat mengalami kesulitan dalam memberikan rekomendasi jika data interaksi antara pengguna dan item sangat jarang. 

## Evaluation

- Metrik yang digunakan dalam metode _Content Based Filtering_ adalah _Precision_

  _Precision_ dihitung berdasarkan formula:

  $$Precision = \frac{Jumlah\ item\ relevan\ yang\ direkomendasikan}{Jumlah\ total\ item\ yang\ direkomendasikan}$$

  Di sini, "item relevan yang direkomendasikan" adalah item-item yang sesuai dengan preferensi atau karakteristik pengguna dan "jumlah total item yang direkomendasikan" adalah total item yang diberikan sebagai rekomendasi oleh sistem.

  Formula ini mengukur seberapa banyak item yang direkomendasikan oleh sistem yang memang relevan dengan preferensi atau karakteristik pengguna, dengan nilai precision berkisar dari 0 hingga 1, di mana 1 menunjukkan bahwa semua item yang direkomendasikan adalah relevan.
  
  Tabel 13. Mencari reomendasi yang mirip dengan makanan _sweet potato pie_

  |     | id_makanan |     nama_makanan | jenis_makanan |
  |----:|-----------:|-----------------:|---------------|
  | 413 |        225 | sweet potato pie |       Dessert |

  Tabel 14. Hasil sistem rekomendasi dengan metode _Content Based Filtering_

  |   |                      nama_makanan | jenis_makanan |
  |--:|----------------------------------:|--------------:|
  | 0 |           chocolate fudge cookies |       Dessert |
  | 1 |              homemade gulab jamun |       Dessert |
  | 2 | jalebi with fennel yogurt pudding |       Dessert |
  | 3 |   double chocolate easter cookies |       Dessert |
  | 4 |           eggless coffee cupcakes |       Dessert |

  Dari hasil rekomendasi pada tabel 14, diketahui bahwa _sweet potato pie_ termasuk ke dalam kategori _Dessert_. Dari 5 item yang direkomendasikan, 5 item memiliki kategori _Dessert_ (similar). Artinya, precision sistem tersebut sebesar 5/5 atau 100%. Dengan nilai _precision_ tersebut dapat disimpulkan bahwa sistem rekomendasi ini dapat menyelesaikan masalah preferensi pelanggan.

- Metrik yang digunakan dalam metode _Collborative Filtering_ adalah _RMSE_

  _Root Mean Squared Error (RMSE)_ adalah salah satu metrik evaluasi yang umum digunakan dalam regresi untuk mengukur seberapa baik model regresi memprediksi nilai target aktual dalam suatu dataset. Metrik ini memberikan gambaran tentang seberapa dekat prediksi model dengan nilai aktual yang diamati.

  ![RMSE](https://github.com/fannof/project_recommendation_system/assets/99071605/68163659-08f3-43c8-a378-3eb1eed18c38)

  Gambar 3. Plot akurasi metrik evaluasi _RMSE_

  Pada gambar 3, proses _training_ model cukup smooth dan model konvergen pada _epochs_ sekitar 100. Dari proses ini, diperoleh nilai _error_ akhir sebesar sekitar 0.19 dan _error_ pada data validasi sebesar 0.33. Nilai tersebut cukup bagus untuk sistem rekomendasi.

  _Root Mean Squared Error (RMSE)_ dihitung berdasarkan formula:

  $$RMSE = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}$$

  Dimana $\( n \)$ adalah angka observasi, $\( y_i \)$ adalah nilai aktual, dan $\( \hat{y}_i \)$ adalah nilai prediksi.

  - Cara Kerja:

    - Untuk setiap pasangan data dalam dataset, hitung selisih antara nilai prediksi yang diberikan oleh model dan nilai aktual yang diamati. Misalkan $\( y_i \)$ adalah nilai aktual, dan $\( \hat{y}_i \)$ adalah nilai prediksi yang diberikan oleh model untuk sampel ke-i dalam dataset, maka selisihnya adalah $e_i = y_i - \hat{y}_i$.

    - Setiap selisih $e_i$ di kuadratkan. Ini dilakukan untuk memastikan bahwa selisih positif dan negatif tidak saling menghapus satu sama lain. Hasilnya adalah $e_i^2$.

    - _Mean_ (rata-rata) dari selisih kuadrat tersebut dihitung. Ini dilakukan dengan menjumlahkan semua nilai $e_i^2$ dan dan membaginya dengan jumlah total sampel.

    - Mengambil akar kuadrat dari nilai rata-rata tersebut untuk mendapatkan nilai _RMSE_.

    _RMSE_ memberikan informasi tentang seberapa besar deviasi rata-rata antara prediksi model dan nilai aktual. Semakin kecil nilai _RMSE_, semakin baik performa model dalam memprediksi nilai target. Sebaliknya, nilai _RMSE_ yang lebih tinggi menunjukkan bahwa model cenderung memiliki kesalahan prediksi yang lebih besar.

    Dari hasil _Top 10 food recommendation_ untuk user pada tahap _Modeling_, sistem tersebut sudah mampu merekomendasikan 10 makanan top berdasarkan rating. Hasil ini sudah dapat membantu pelayan untuk merekomendasikan makanan yang cocok bagi pelanggan.
     
## REFERENCES

[1]	H. Hartatik, S. D. Nurhayati, and W. Widayani, “Sistem Rekomendasi Wisata Kuliner di Yogyakarta dengan Metode Item-Based Collaborative Filtering,” J. Autom. Comput. Inf. Syst., vol. 1, no. 2, pp. 55–63, 2021, doi: 10.47134/jacis.v1i2.8.

[2]	Kosim and R. Prihandi, “SISTEM REKOMENDASI MENU MINUMAN DENGAN METODE CONTENT – BASED FILTERING BERBASIS ANDROID PADA MUBTADA KOPI,” J. Comput. Sci. Artif. Intell., vol. 1, no. 1, pp. 43–69, 2024.

[3]	G. Yunanda, D. Nurjanah, and S. Meliana, “Recommendation System from Microsoft News Data using TF-IDF and Cosine Similarity Methods,” Build. Informatics, Technol. Sci., vol. 4, no. 1, pp. 277–284, 2022, doi: 10.47065/bits.v4i1.1670.
