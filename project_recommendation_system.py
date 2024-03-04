# -*- coding: utf-8 -*-
"""project_recommendation_system.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16KDw_yxo64ZNJzIfRQRTxZDK8l88VBul

# Laporan Proyek Machine Learning - Novan Nur Hidayat

# PENGEMBANGAN SISTEM REKOMENDASI MAKANAN DENGAN ALGORITMA _CONTENT BASED FILTERING_ DAN _COLLABORATIVE FILTERING_

## Project Overview

- Latar belakang

  Makanan sangat penting bagi manusia, baik sebagai kebutuhan primer maupun sebagai komponen kehidupan sehari-hari seseorang. Kemerosotan ekonomi yang telah mempengaruhi beberapa industri telah menyebabkan peluang baru yang membuat industri kuliner, khususnya divisi _online_-nya, semakin sukses. Wisata kuliner menjadi hal terpenting di dunia kuliner. Memanfaatkan informasi yang tersedia di internet membuat banyak masyarakat lebih sulit untuk memilih kebutuhan mereka [1].
"""

# Import semua library yang dibutuhkan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from pathlib import Path

"""## Business Understanding

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
"""

foods = pd.read_csv('foods.csv')
foods

"""### Variabel-variabel pada _Food Recommendation System_ adalah sebagai berikut:

Dataset _foods.csv_

- id_makanan : Nomor id dari masing-masing makanan.
- nama_makanan : Nama dari masing-masing makanan dari sebuah restoran.
- jenis_makanan : Jenis makanan apakah makanan tersebut termasuk 'Healthy_Food' 'Snack' 'Dessert' 'Japanese' 'Indian' 'French' 'Mexican'
 'Italian' 'Chinese' 'Beverage' 'Thai' 'Korean' 'Vietnames' 'Nepalese' 'Spanish'.
- veg_non : Mengidentifikasi apakah makanan tersebut termasuk dalam Vegan atau Non-Vegan.
- deskripsi : Deskripsi komposisi dari makanan.
"""

# Mengubah nama kolom "C_Type" menjadi "jenis_makanan" dan nama kolom "Describe" menjadi "deskripsi"
foods = foods.rename(columns={'Food_ID': 'id_makanan', 'Name': 'nama_makanan', 'C_Type': 'jenis_makanan', 'Veg_Non': 'veg_non', 'Describe': 'deskripsi'})
foods

# Melihat info lebih lanjur mengenai dataset
foods.info()

# Mengecek missing value
foods.isnull().sum()

foods_duplicates = foods.duplicated().sum()
print("Jumlah duplikat dalam DataFrame foods:", foods_duplicates)

# Mengecek variabel nama_makanan yang unik
print('Jumlah data: ', len(foods.nama_makanan.unique()))
print('Jenis model: ', foods.nama_makanan.unique())

print('Jumlah data: ', len(foods.jenis_makanan.unique()))
print('Jenis makanan: ', foods.jenis_makanan.unique())

# Mengganti nilai "Healthy Food" menjadi "Healthy_Food"
foods['jenis_makanan'] = foods['jenis_makanan'].str.replace('Healthy Food', 'Healthy_Food').str.replace(' Korean', 'Korean')
print('Jumlah data: ', len(foods.jenis_makanan.unique()))
print('Jenis makanan: ', foods.jenis_makanan.unique())

"""Jumlah data pada dataset _ratings.csv_ sebanyak 512 data, yang terbagi dalam 3 kolom. Kolom pertama yaitu 'User_ID' yang di _rename_ menjadi 'user_id' memiliki 512 data bertipe _integer_ dengan 101 data yang unik, kolom 'Food_ID' yang di _rename_ menjadi 'id_makanan' memiliki 512 data bertipe _integer_ dengan 310 data yang unik, kolom 'Rating' yang di _rename_ menjadi 'rating' memiliki 512 data bertipe _integer_. Terdapat 1 nilai NaN pada dataset ini. Dataset dapat lebih lanjut dilihat pada Tabel 3 dan 4.

"""

ratings = pd.read_csv('ratings.csv')
ratings

"""Dataset _ratings.csv_

- user_id : Nomor id pelanggan yang memberikan rating pada makanan.
- id_makanan : Nomor id dari masing-masing makanan.
- rating : Rating dari pelanggan tentang makanan tersebut.
"""

# Mengubah nama kolom "User_ID" menjadi "user_id"
ratings = ratings.rename(columns={'User_ID': 'user_id', 'Food_ID': 'id_makanan', 'Rating': 'rating'})
ratings

ratings.describe()

print('Jumlah user id: ', len(ratings.user_id.unique()))
print('Jumlah id makanan: ', len(ratings.id_makanan.unique()))
print('Jumlah data rating: ', len(ratings))

ratings.isnull().sum()

ratings = ratings.dropna()
ratings.isnull().sum()

ratings

ratings_duplicates = ratings.duplicated().sum()
print("Jumlah duplikat dalam DataFrame ratings:", ratings_duplicates)

ratings.shape

"""### Exploratory Data Analysis"""

# Menggabungkan dataset foods dan ratings menjadi dataframe baru
foods_all = pd.merge(foods, ratings, on='id_makanan', how='left')
foods_all

foods_all.isnull().sum()

# Menghapus missing value
foods_all = foods_all.dropna()
foods_all

foods_all.isnull().sum()

foods_all = foods_all.drop_duplicates()
foods_all

"""## Data Preparation

Mengkonversi data pada kolom 'id_makanan', 'nama_makanan', dan 'jenis_makanan' menjadi bentuk _list_ dan membuat _dictionary_ untuk menentukan pasangan _key-value_ antara ketiga kolom tersebut. Hasil dapat dilihat pada tabel 9.

"""

# Mengonversi data series 'id_makanan' menjadi dalam bentuk list
food_id = foods_all['id_makanan'].tolist()

# Mengonversi data series ‘nama_makanan’ menjadi dalam bentuk list
food_name = foods_all['nama_makanan'].tolist()

# Mengonversi data series ‘jenis_makanan’ menjadi dalam bentuk list
food_varian = foods_all['jenis_makanan'].tolist()

print(len(food_id))
print(len(food_name))
print(len(food_varian))

# Membuat dictionary untuk data ‘id_makanan’, ‘nama_makanan’, dan ‘jenis_makanan’
foods_new = pd.DataFrame({
    'id_makanan': food_id,
    'nama_makanan': food_name,
    'jenis_makanan': food_varian
})
foods_new

foods_new = foods_new.drop_duplicates()
foods_new

"""- _TF-IDF Vectorizer_

  Teknik untuk pembobotan kata-kata disebut _Term Frequency-Inverse Document Frequency (TF-IDF)_, yang menentukan seberapa sering sebuah kata muncul di setiap dokumen serta di semua dokumen. _Term Frequency (TF)_ dan _Inverse Document Frequency (IDF)_ membentuk TF-IDF. Nilai yang disebut "_Term Frequency_" menunjukkan seberapa sering istilah tertentu muncul dalam dokumen. Berat istilah meningkat seiring dengan berapa kali istilah tersebut muncul dalam dokumen. Tujuan dari _Inverse Document Frequency (IDF)_ adalah untuk mengurangi bobot istilah jika muncul di setiap dokumen. Berbeda dengan _TF_, nilainya meningkat dengan menurunnya frekuensi kata dalam dokumen [3]. Setelah _TF-IDF_ diterapkan pada 'nama_makanan' dan 'jenis_makanan', hasilnya terdapat pada tabel 10.

"""

# Inisialisasi TfidfVectorizer
tf = TfidfVectorizer()

# Melakukan perhitungan idf pada data jenis_makanan
tf.fit(foods_new['jenis_makanan'])

# Mapping array dari fitur index integer ke fitur jenis
tf.get_feature_names_out()

# Melakukan fit lalu ditransformasikan ke bentuk matrix
tfidf_matrix = tf.fit_transform(foods_new['jenis_makanan'])

# Melihat ukuran matrix tfidf
tfidf_matrix.shape

# Mengubah vektor tf-idf dalam bentuk matriks dengan fungsi todense()
tfidf_matrix.todense()

# Membuat dataframe untuk melihat tf-idf matrix
# Kolom diisi dengan jenis masakan
# Baris diisi dengan nama makanan

pd.DataFrame(
    tfidf_matrix.todense(),
    columns=tf.get_feature_names_out(),
    index=foods_new.nama_makanan
).sample(10, axis=1).sample(32, axis=0)

"""- _Cosine Similarity_

  Kosinus sudut yang dibentuk oleh dua benda atau vektor dalam ruang dimensi-n ditentukan oleh skor _cosine similarity_. Sudut antara vektor riwayat berita pembaca pada data uji dan pembaca pada data pelatihan ditentukan dengan menggunakan skor _cosine similarity_. Kedua vektor identik jika sudutnya nol atau skor kosinus adalah 1. Sebaliknya, kedua vektor berbeda secara signifikan satu sama lain jika skor kosinus menampilkan -1, atau sudut 180 derajat. Pada tahap ini, dihitung _cosine similarity dataframe tfidf_matrix_ yang telah diperoleh pada tahapan sebelumnya. Dengan satu baris kode untuk memanggil fungsi _cosine similarity_ dari _library sklearn_, telah berhasil menghitung kesamaan _(similarity)_ antar makanan. Kode akan menghasilkan _output_ berupa matriks kesamaan dalam bentuk _array_ [3].

"""

# Menghitung cosine similarity pada matrix tf-idf
cosine_sim = cosine_similarity(tfidf_matrix)
cosine_sim

# Membuat dataframe dari variabel cosine_sim dengan baris dan kolom berupa nama makanan
cosine_sim_df = pd.DataFrame(cosine_sim, index=foods_new['nama_makanan'], columns=foods_new['nama_makanan'])
print('Shape:', cosine_sim_df.shape)

# Melihat similarity matrix pada setiap makanan
cosine_sim_df.sample(15, axis=1).sample(15, axis=0)

"""## Modeling

Model akan dikembangkan dengan 2 metode yang berbeda. Kedua metode tersebut adalah sebagai berikut:

1. _Content Based Filtering_

     Sistem rekomendasi _Content Based Filtering_ menyarankan produk yang mirip dengan produk yang disukai pengguna sebelumnya. Nilai item ditentukan dengan mempertimbangkan fitur yang ada di setiap konten. Sistem rekomendasi _knowledge-based_ menyarankan item berdasarkan pengetahuan domain pengguna tentang fitur apa yang tersedia dalam item dan bagaimana pengguna dapat memenuhi kebutuhan dan berguna bagi pengguna. Nilai kesamaan dihitung berdasarkan besarnya nilai kesamaan antara kebutuhan pengguna dan rekomendasi yang ada. Ada dua pendekatan yang tersedia dalam metode rekomendasi _knowledge-based_ yaitu _case based_ dan _constraint-based_. Kesamaan antara kedua pendekatan ini adalah bahwa pengguna harus mengirimkan permintaan sesegera mungkin.  Selanjutnya, sistem akan mengidentifikasi solusi yang paling sesuai dengan kebutuhan pengguna [1]. Seperti yang terlihat pada gambar 3.
"""

def food_recommendations(makanan, similarity_data=cosine_sim_df, items=foods_new[['nama_makanan', 'jenis_makanan']], k=5):
    """
    Rekomendasi makanan berdasarkan kemiripan dataframe

    Parameter:
    ---
    makanan : tipe data string (str)
                Makanan (index kemiripan dataframe)
    similarity_data : tipe data pd.DataFrame (object)
                      Kesamaan dataframe, simetrik, dengan makanan sebagai
                      indeks dan kolom
    items : tipe data pd.DataFrame (object)
            Mengandung kedua nama dan fitur lainnya yang digunakan untuk mendefinisikan kemiripan
    k : tipe data integer (int)
        Banyaknya jumlah rekomendasi yang diberikan
    ---


    Pada index ini, kita mengambil k dengan nilai similarity terbesar
    pada index matrix yang diberikan (i).
    """


    # Mengambil data dengan menggunakan argpartition untuk melakukan partisi secara tidak langsung sepanjang sumbu yang diberikan
    # Dataframe diubah menjadi numpy
    # Range(start, stop, step)
    index = similarity_data.loc[:,makanan].to_numpy().argpartition(
        range(-1, -k, -1))

    # Mengambil data dengan similarity terbesar dari index yang ada
    closest = similarity_data.columns[index[-1:-(k+2):-1]]

    # Drop makanan agar nama makanan yang dicari tidak muncul dalam daftar rekomendasi
    closest = closest.drop(makanan, errors='ignore')

    return pd.DataFrame(closest).merge(items).head(k)

foods_new[foods_new.nama_makanan.eq('sweet potato pie')]

"""_sweet potato pie_ masuk dalam kategori jenis makanan dessert. Tentunya diharapkan rekomendasi yang diberikan adalah makanan dengan kategori yang mirip. Lalu panggil fungsi food_recommendations. Hasilnya dapat dilihat pada tabel 13.

"""

# Mendapatkan rekomendasi makanan yang mirip dengan sweet potato pie
food_recommendations('sweet potato pie')

"""2. _Collaborative Filtering_

      Metode _Collaborative Filtering_ adalah teknik yang memberikan rekomendasi berdasarkan preferensi pengguna atau item serupa lainnya.  Dua jenis metode _Collaborative Filtering_ dibedakan menjadi: _User Based CF_ dan _Item Based CF_. _User-Based Collaborative Filtering_ menyatakan bahwa cara terbaik untuk menemukan item menarik bagi pengguna adalah dengan mencari pengguna lain yang memiliki minat atau kebutuhan yang sama. Algoritma _User Based CF_ dapat mengidentifikasi pengguna yang mirip satu sama lain _(user neighbor)_ dengan mengidentifikasi pengguna yang berbeda satu sama lain _(user similarity)_. Setiap rating yang didapatkan dari pengguna yang bertetangga kemudian akan dijadikan mesin rekomendasi bagi pengguna aktif [1]. Seperti yang terlihat pada gambar 4.

"""

# Mengubah user_id menjadi list tanpa nilai yang sama
users_id = ratings['user_id'].unique().tolist()
print('list user_id: ', users_id)

# Melakukan encoding user_id
user_to_user_encoded = {x: i for i, x in enumerate(users_id)}
print('encoded user_id : ', user_to_user_encoded)

# Melakukan proses encoding angka ke ke user_id
user_encoded_to_user = {i: x for i, x in enumerate(users_id)}
print('encoded angka ke user_id: ', user_encoded_to_user)

# Mengubah id_makanan menjadi list tanpa nilai yang sama
foods_id = ratings['id_makanan'].unique().tolist()

# Melakukan proses encoding id_makanan
food_to_food_encoded = {x: i for i, x in enumerate(foods_id)}

# Melakukan proses encoding angka ke id_makanan
food_encoded_to_food = {i: x for i, x in enumerate(foods_id)}

# Mapping userID ke dataframe user
ratings['user'] = ratings['user_id'].map(user_to_user_encoded)

# Mapping placeID ke dataframe makanan
ratings['food'] = ratings['id_makanan'].map(food_to_food_encoded)

# Mendapatkan jumlah user
num_users = len(user_to_user_encoded)
print(num_users)

# Mendapatkan jumlah makanan
num_food = len(food_encoded_to_food)
print(num_food)

# Mengubah rating menjadi nilai float
ratings['rating'] = ratings['rating'].values.astype(np.float32)

# Nilai minimum rating
min_rating = min(ratings['rating'])

# Nilai maksimal rating
max_rating = max(ratings['rating'])

print('Number of User: {}, Number of Food: {}, Min Rating: {}, Max Rating: {}'.format(
    num_users, num_food, min_rating, max_rating
))

# Mengacak dataset
ratings = ratings.sample(frac=1, random_state=12)
ratings

# Membuat variabel x untuk mencocokkan data user dan makanan menjadi satu value
x = ratings[['user', 'food']].values

# Membuat variabel y untuk membuat rating dari hasil
y = ratings['rating'].apply(lambda x: (x - min_rating) / (max_rating - min_rating)).values

# Membagi menjadi 80% data train dan 20% data validasi
train_indices = int(0.8 * ratings.shape[0])
x_train, x_val, y_train, y_val = (
    x[:train_indices],
    x[train_indices:],
    y[:train_indices],
    y[train_indices:]
)

print(x, y)

class RecommenderNet(tf.keras.Model):

  # Insialisasi fungsi
  def __init__(self, num_users, num_food, embedding_size, **kwargs):
    super(RecommenderNet, self).__init__(**kwargs)
    self.num_users = num_users
    self.num_food = num_food
    self.embedding_size = embedding_size
    self.user_embedding = layers.Embedding( # layer embedding user
        num_users,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.user_bias = layers.Embedding(num_users, 1) # layer embedding user bias
    self.food_embedding = layers.Embedding( # layer embeddings resto
        num_food,
        embedding_size,
        embeddings_initializer = 'he_normal',
        embeddings_regularizer = keras.regularizers.l2(1e-6)
    )
    self.food_bias = layers.Embedding(num_food, 1) # layer embedding resto bias

  def call(self, inputs):
    user_vector = self.user_embedding(inputs[:,0]) # memanggil layer embedding 1
    user_bias = self.user_bias(inputs[:, 0]) # memanggil layer embedding 2
    food_vector = self.food_embedding(inputs[:, 1]) # memanggil layer embedding 3
    food_bias = self.food_bias(inputs[:, 1]) # memanggil layer embedding 4

    dot_user_food = tf.tensordot(user_vector, food_vector, 2)

    x = dot_user_food + user_bias + food_bias

    return tf.nn.sigmoid(x) # activation sigmoid

model = RecommenderNet(num_users, num_food, 50) # inisialisasi model

# model compile
model.compile(
    loss = tf.keras.losses.BinaryCrossentropy(),
    optimizer = keras.optimizers.Adam(learning_rate=0.001),
    metrics=[tf.keras.metrics.RootMeanSquaredError()]
)

"""## Evaluation

- Metrik yang digunakan adalah _RMSE_

  _Root Mean Squared Error (RMSE)_ adalah salah satu metrik evaluasi yang umum digunakan dalam regresi untuk mengukur seberapa baik model regresi memprediksi nilai target aktual dalam suatu dataset. Metrik ini memberikan gambaran tentang seberapa dekat prediksi model dengan nilai aktual yang diamati.

"""

# Memulai training

history = model.fit(
    x = x_train,
    y = y_train,
    batch_size = 8,
    epochs = 100,
    validation_data = (x_val, y_val)
)

plt.plot(history.history['root_mean_squared_error'])
plt.plot(history.history['val_root_mean_squared_error'])
plt.title('model_metrics')
plt.ylabel('root_mean_squared_error')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

"""Pada gambar 3, proses _training_ model cukup smooth dan model konvergen pada _epochs_ sekitar 100. Dari proses ini, diperoleh nilai _error_ akhir sebesar sekitar 0.19 dan _error_ pada data validasi sebesar 0.33. Nilai tersebut cukup bagus untuk sistem rekomendasi.

Mendapatkan rekomendasi makanan dengan metode _Collaborative Filtering_

   Tahap pertama yaitu ambil sampel user secara acak dan definisikan variabel food_not_displayed yang merupakan daftar makanan yang belum pernah dilihat oleh pelanggan. Hal ini dilakukan karena daftar food_not_displayed inilah yang akan menjadi makanan yang direkomendasikan.
"""

food_df = foods_new
rating_food = pd.read_csv('ratings.csv')

# Mengambil sample user
user_id = rating_food.User_ID.sample(1).iloc[0]
food_displayed_by_user = rating_food[rating_food.User_ID == user_id]

# Operator bitwise (~)
food_not_displayed = food_df[~food_df['id_makanan'].isin(food_displayed_by_user.Food_ID.values)]['id_makanan']
food_not_displayed = list(
    set(food_not_displayed)
    .intersection(set(food_to_food_encoded.keys()))
)

food_not_displayed = [[food_to_food_encoded.get(x)] for x in food_not_displayed]
user_encoder = user_to_user_encoded.get(user_id)
user_food_array = np.hstack(
    ([[user_encoder]] * len(food_not_displayed), food_not_displayed)
)

ratings = model.predict(user_food_array).flatten()

top_ratings_indices = ratings.argsort()[-10:][::-1]
recommended_food_ids = [
    food_encoded_to_food.get(food_not_displayed[x][0]) for x in top_ratings_indices
]

print('Showing recommendations for users: {}'.format(user_id))
print('===' * 9)
print('Food with high ratings from user')
print('----' * 8)

top_food_user = (
    food_displayed_by_user.sort_values(
        by = 'Rating',
        ascending=False
    )
    .head(5)
    .Food_ID.values
)

food_df_rows = food_df[food_df['id_makanan'].isin(top_food_user)]
for row in food_df_rows.itertuples():
    print(row.nama_makanan, ':', row.jenis_makanan)

print('----' * 8)
print('Top 10 food recommendation')
print('----' * 8)

recommended_food = food_df[food_df['id_makanan'].isin(recommended_food_ids)]
for row in recommended_food.itertuples():
    print(row.nama_makanan, ':', row.jenis_makanan)

"""Hasil di atas adalah rekomendasi untuk user dengan id 59. Dari _output_ tersebut, didapat perbandingan antara _food with high ratings from user_ dan _Top 10 food recommendation_ untuk user.

   Beberapa makanan rekomendasi menyediakan kategori jenis makanan yang sesuai dengan rating user. Diperoleh 2 rekomendasi makanan dengan kategori jenis makanan 'Indian', 3 rekomendasi makanan dengan kategori 'Healthy_Food', 1 rekomendasi makanan kategori 'Dessert', 2 rekomendasi makanan kategori 'Japanese', dan 2 makanan dengan kategori 'Italian'.

"""