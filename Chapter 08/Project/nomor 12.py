buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
status = True
print ("-----Program penjual buah-----\n")
print ("Daftar harga buah per kilogram")
print (buah)
while (status == True):
    print ("\nMenu : ")
    print ("A. Beli buah \nB. Tambah daftar harga buah \nC. Hapus buah dari daftar harga \nD. Keluar dari aplikasi")
    menu = input ("\nPilihan Anda (huruf BESAR) : ")
    print() 
    harga = []
    if (menu == 'A'):
        while True :
            beli = input ("Nama buah yang ingin dibeli : ")
            if (beli in buah):
                try:
                    kilo = int ( input ("jumlah kilogram             : "))
                    harga1 = kilo * buah[beli]
                    harga.append(harga1)
                    konfirmasi = input ("\nIngin beli buah lagi? (y/n) : ")
                    if (konfirmasi != 'y'):
                        print("-------------------------------")
                        print("Total harga                 : Rp", sum(harga), "\n")
                        break    
                except (ValueError):
                    print ("Masukkan jumlah kilogram yang valid")
            
            elif (beli == '') or (beli not in buah):
                print ("Buah yang ingin Anda beli tidak ada di daftar")
            
    elif (menu == 'B'):
        i = True
        while (i == True) :
            buah_baru = input ("Masukkan nama buah baru yang ingin dijual :")
            if (buah_baru in buah):
                print (buah_baru, "sudah ada dalam daftar")
            elif (buah_baru not in buah):    
                try:
                    harga_baru = int ( input ("Harga per kilogram : Rp"))
                    buah[buah_baru] = harga_baru
                    print (buah_baru, "berhasil ditambahkan\n")
                    print ("Daftar harga saat ini \n")
                    for data in buah:
                        print (data, "( Harga Rp",buah.get(data),")")
                        i = False
                    print()
                except (ValueError):
                    print ("Masukkan harga yang valid")
    elif (menu == 'C'):
        j = True
        while (j == True):
            hapus = input ("Ketikkan nama buah yang akan dihapus : ")
            if (hapus not in buah):
                print ("Buah", hapus, "tidak ada dalam daftar")
            elif (hapus in buah):
                del buah[hapus]
                print (hapus, "telah dihapus dari daftar\n")
                print ("Daftar harga saat ini\n")
                for data in buah:
                        print (data, "( Harga Rp",buah.get(data),")")
                j = False
    elif (menu == 'D'):
        print("Terimakasih telah menggunakan layanan kami")
        break
