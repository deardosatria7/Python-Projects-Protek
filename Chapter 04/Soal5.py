# ini soal nomor 5
print ("Grafik horiontal jumlah mahasiswa laki-laki dan perempuan")
jmlLakiLaki = a = int (input ("Silahkan masukkan data jumlah mahasiswa laki-laki : "))
jmlPerempuan = b = int (input ("Silahkan masukkan data jumlah mahasiswa perempuan : "))
c = int (jmlLakiLaki/10)
d = int (jmlPerempuan/10)
print (" Grafik : ")
print ("Mahasiswa laki-laki :", end = '')
print ('*' * c, "(",jmlLakiLaki,")")
print ("Mahasiswa perempuan :", end = '')
print ('*' * d, "(",jmlPerempuan,")")
