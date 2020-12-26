alamat = input ("Masukkan alamat dari file yang ingin dibuka (contoh = D:\Folder\File) : ")
try:
    file = open(alamat, 'r' )
    genap = []
    ganjil = []
    data_int = []
    try:
        for data in file:
            data_int.append(int(data))
        print()
        for data in data_int:
            print (data)
            if (data % 2 == 0):
                genap.append(data)
            else :
                ganjil.append(data)
        print ("\nTotal bilangan genap ada",len(genap))
        print ("Total bilangan ganjil ada",len(ganjil))
        file.close()
    except (ValueError):
        print ("\nIsi text harus berupa bilangan!")
        file.close()
except (OSError):
    print("\nFile tidak ditemukan")

