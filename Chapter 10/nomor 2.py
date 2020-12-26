print ('=' * 50, "\nProgram Input Data Mahasiswa")
print ("Format : nim | nama | alamat(kota) ")
print('-' * 50)
print ("File akan disimpan dengan nama \"Data Mhs.txt\" \nPada folder yang sama dengan file python ini")
file = open ("Data Mhs.txt", 'a+')
status = True
while status == True :
    data = []
    nim = input ("\nMasukkan NIM mahasiswa/i : ")
    data.append(nim)
    nama = input ("Masukkan nama mahasiswa/i : ")
    data.append(nama)
    kota = input ("Masukkan asal kota : ")
    data.append(kota)
    gabung = ' | '.join(data)
    file.write(gabung + '\n')
    konfirmasi = input ("\nIngin menambahkan lagi? (y/n) : ")
    if konfirmasi != 'y' :
        print ("\nFile telah disimpan")
        print ('=' * 50)
        file.close()
        status = False
        
        
        
        

