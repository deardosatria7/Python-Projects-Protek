# ini soal nomor 1
sewa1 = 200000
sewa2 = 10000
jamMulai = 6
menitMulai = 0
jamSelesai = 23
menitSelesai = 50


waktuSewa = (jamSelesai - jamMulai) + int ((menitSelesai - menitMulai)/60)
harga = (waktuSewa//12 * sewa1) + waktuSewa%12 * sewa2
print (harga)
