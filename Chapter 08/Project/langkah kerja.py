#langkah kerja
#buatlah list a dan b
a = [1,5,6,3,6,9,11,20,12]
b = [7,4,5,6,7,1,12,5,9]

#Sisipkan nilai 10 ke dalam indeks ke 3 dari a
#dan nilai 15 ke dalam indeks ke 2 dari b
a.insert(3, 10)
b.insert(2, 15)

#sisipkan nilai 4 ke indeks terakhir a
#dan nilai 8 ke indeks terakhir b
a.append(4)
b.append(8)

#buat list c yang merupakan sublist a 0-7
#dan list d yang merupakan sublist b 2-9
c = a[0:8]
d = b[2:10]

#buat list e yang merupakan hasil penjumlahan masing-masing sublist c dan d
e = []
for i in range (len(c)):
    z = c[i] + d[i]
    e.append(z)

#ubah list e menjadi tuple
e_tuple = tuple(e)

#cari nilai min, maks, dan jumlah seluruh elemmen pada e
e_minimum = min(e_tuple)
e_maksimum = max(e_tuple)
e_jumlah = sum(e_tuple)

#buatlah string "myString"
myString = 'python adalah bahasa pemrograman yang menyenangkan'

#Dengan menggunakan set() tentukan karakter huruf apa saja yang menyusun string tersebut
set_myString = set(myString)

#Urutkan secara alfabet himpunan karakter huruf yang diperoleh dari langkah 10, dengan terlebih dahulu mengubahnya ke list
list_myString = list(set_myString)
list_myString.sort()
print(list_myString)
