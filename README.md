🐍 Python Basic Data Types & Type Casting

Repository ini berisi contoh kode Python dasar untuk memahami:

Cara menampilkan output

Tipe data dasar Python

Konversi tipe data (type casting)

Ditujukan untuk pemula yang baru mulai belajar Python.

📂 Isi Program

Program ini mencakup pembelajaran berikut:

✅ Output Dasar

Menggunakan fungsi print() untuk menampilkan teks ke layar.

✅ Tipe Data Dasar

Integer (int) → bilangan bulat

Float (float) → bilangan desimal

String (str) → teks / karakter

Boolean (bool) → True atau False

✅ Pengecekan Tipe Data

Menggunakan fungsi:

type()

✅ Konversi Tipe Data (Casting)

Mengubah satu tipe data ke tipe lain menggunakan:

int()

float()

bool()

🧪 Contoh Kode
print("yonmus")

data_integer = 20
print("data : ", data_integer)
print("- bertipe :", type(data_integer))

data_float = 20.5
print("Data : ", data_float)
print("- bertipe : ", type(data_float))

data_string = "Hello, Python!"
print("Data : ", data_string)
print("- bertipe : ", type(data_string))

⚠ Catatan Penting

❌ Kode berikut akan error:

int("Hello, Python!")
float("Hello, Python!")


✔ Konversi hanya berhasil jika string berisi angka, contoh:

int("123")
float("20.5")

🔍 Boolean dari String
bool("Hello")
# True

bool("")
# False


String kosong → False

String tidak kosong → True

▶ Cara Menjalankan Program

Pastikan Python sudah terinstall

Simpan file sebagai:

main.py


Jalankan:

python main.py

🎯 Tujuan Pembelajaran

Memahami konsep tipe data Python

Mengetahui cara mengecek tipe data

Mengenal dasar konversi tipe data

Menyiapkan dasar sebelum masuk ke:

Control flow

Function

OOP Python

📌 License

This project is open-source and free to use for learning purposes.
