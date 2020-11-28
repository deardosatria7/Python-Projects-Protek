print ("Program input nama mahasiswa")
status = True
a = []
while (status == True):
    namaMhs = str ( input ("Masukkan nama mahasiswa/i : "))
    a.append(namaMhs)
    konfirmasi = input ("Apakah Anda ingin menambahkan lagi? (y/n) : ")
    a.sort()
    if (konfirmasi != 'y'):
        print()
        for data in a:
            print (data, "(", len(data), "karakter", ")")
            status = False 
        
