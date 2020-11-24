try :
    namaFile = input ("Silahkan masukkan alamat file Anda : ")
    file = open (namaFile, "r")
    status = True
    file = open(namaFile, "a")
    while (status == True):
        isi_file = input ("Masukkan data yang ingin Anda tambah :")
        file.write(isi_file)
        file.write("\n")
        konfirmasi = input ("Apa Anda ingin menambahkan data lain? (y/n) :")
        if (konfirmasi != 'y'):
            status = False
            file = open (namaFile, "r")
            print ("Berikut adalah tampilan akhir dari file tersebut \n")
            print(file.read())
            file.close()
except (FileNotFoundError):
    print ("\nFile tidak ditemukan \nMohon cek kembali alamat file Anda")

except (PermissionError):
    print ("\nMohon periksa kembali alamat file yang Anda masukkan")

    
