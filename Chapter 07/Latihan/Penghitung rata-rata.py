print ("------------------------------------")
print ("  ***Program Penghitung Rata-rata***")
print ("------------------------------------\n")
status = True
sum = 0
i = 0
while (status == True):
    try:
        bil = int ( input ("Masukkan sebuah bilangan : "))
        sum = sum + bil
        i += 1
        konfirmasi = input ("Ingin menambahkan bilangan lain? (y/n) : ")
        if konfirmasi != 'y' :
            status = False
            print ("\nRata-rata dari semua bilangan diatas adalah ", sum/i)
    except (ValueError):
        print ("Maaf, bukan bilangan bulat")
