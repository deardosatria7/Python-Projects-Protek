buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print ("-----Program penjual buah-----\n")
print ("Daftar harga buah per kilogram")
print (buah, "\n")
while True:
    beli = input ("Nama buah yang ingin dibeli : ")
    if beli in buah:
        try:
            kilo = int ( input ("jumlah kilogram             : "))
            harga = kilo * buah[beli]
            print("-------------------------------")
            print("Total harga                 : Rp", harga)
            break
        except (ValueError):
            print ("Masukkan jumlah kilogram yang valid")
            break
    elif (beli == '') or (beli not in buah):
        print ("Buah yang ingin Anda beli tidak ada di daftar")
    
    
