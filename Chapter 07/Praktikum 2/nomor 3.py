try :
    # membuka dan membaca file d:/data.txt
    file = open("d:/data.txt", "r")

    # baca baris pertama dari file
    # simpan kedalam variabel bil1 sebagai integer
    bil1 = int (file.readline())

    # baca baris kedua dari file
    # simpan dalam vsriabel bil2 sebagai integer
    bil2 = int (file.readline())

    #hitung dan tampilkan hasil bagi
    hasil = bil1/bil2
    print (bil1, "dibagi dengan", bil2, "sama dengan", hasil)
except (FileNotFoundError):
    print ("Mohon periksa kembali alamat file Anda")
except (ZeroDivisionError):
    print ("Tidak dapat membagi dengan nol")

