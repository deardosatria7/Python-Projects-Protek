# ini soal nomor 4
jarakAB = 125
jarakBC = 256
kecepatanAB = 62
kecepatanBC = 70
jamBerangkat = 6
menitBerangkat = 0
menitIstirahat = 45
waktuPerjalanan = int (((jarakAB / kecepatanAB) + (jarakBC/kecepatanBC))*60) + (menitIstirahat)
jamTiba = waktuPerjalanan//60 + (waktuPerjalanan%60)/100 + jamBerangkat
print ("Pak Budi sampai tujuan pada pukul", jamTiba, "WIB")


