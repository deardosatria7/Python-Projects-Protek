try :
    listAngka = []
    banyakBil = int ( input ("Ketikkan banyaknya bilangan yang akan dimasukkan : "))
    while(len(listAngka) < banyakBil):
        angka = int ( input ("Masukkan sebuah angka : "))
        listAngka.append(angka)

    listAngka.sort(reverse = True)
    print ("Urutan besar ke kecil dari angka yang sudah dimasukkan adalah\n",listAngka)
except (ValueError):
    print ("Mohon masukkan angka yang valid...")
