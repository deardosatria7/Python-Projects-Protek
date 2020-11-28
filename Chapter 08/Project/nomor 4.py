sayur = ['bayam', 'kangkung', 'wortel', 'selada']
print ("----PROGRAM BELANJAAN SAYUR----")
print ("Keranjang saat ini : ", sayur)
print ("\nSilahkan memilih menu dibawah untuk melanjutkan")
while True :
    print ("Menu: \nA. Tambah sayur lain \nB. Hapus data sayur \nC. Tampilkan keranjang \nD. Keluar \n")
    pilih = input ("Pilihan Anda (huruf BESAR) : ")
    if (pilih == 'A'):
        tambah = str ( input ("Ketikkan satu sayur yang ingin ditambahkan : "))
        print (tambah, "sudah dimasukkan dalam keranjang\n")
        sayur.append (tambah)
    elif (pilih == 'B'):
        i = True
        while (i == True):
            try:
                hapus = str ( input ("Ketikkan satu sayur yang ingin dihapus : "))
                sayur.remove(hapus)
                print(hapus, "telah dihapus dari keranjang\n")
                i = False
            except (ValueError):
                print ("Tidak ditemukan dalam keranjang")
    
    elif (pilih == 'C') :
        print("isi keranjang sekarang : ", sayur, "\n")
    elif (pilih == 'D'):
        keluar = input ("Anda yakin ingin keluar dari program? (y/n) : ")
        if keluar == 'y':
            break
    
            
        
        
        
    
