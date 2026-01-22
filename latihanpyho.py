print ("yonmus")#print dalah menjalankan fungsi untuk menampilkan output ke layar

#tipe data integer / bilangan bulat 
data_integer = 20
print ("data : ", data_integer)
print ("- bertipe :", type (data_integer))

#tipe data float / bilangan desimal
data_float = 20.5                               
print("Data : ", data_float)
print("- bertipe : ", type(data_float))

#tipe data string / kumpulan karakter
data_string = "Hello, Python!"
print("Data : ", data_string)
print("- bertipe : ", type(data_string))

data_integer = int(data_string)  # Mengubah string ke integer
data_float = float(data_string)  # Mengubah string ke float
data_boolean = bool(data_string)  # Data boolean akan bernilai True jika data_string tidak kosong
print("Data integer : ", data_integer, ",type=", type(data_integer))
print("Data float : ", data_float, ",type=", type(data_float))
print("Data boolean : ", data_boolean, ",type=", type(data_boolean))
print("Data : ", data_integer)