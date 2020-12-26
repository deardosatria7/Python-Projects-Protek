enkripsi = []
hasil = []
print('=' * 50)
print("Program Sandi Caesar")
print('-'*50)
try :
    alamat = input ("Masukkan alamat teks yang akan di-enkripsi\n(contoh D:\Folder\Text.txt) : ")
    angka = int ( input("Berapa alpabhet yang ingin Anda geser?\n(contoh A --> E = 4) : "))
    with open (alamat, 'r', encoding="utf-8") as sumber:
        for kata in sumber:
            for huruf in kata:
                x = ord(huruf)
                y = x + angka
                enkripsi.append(y)
    print('-' * 50)
    print ("Hasil telah disimpan di folder yang sama dengan kode python ini \nDengan nama \"Enkripsi.txt\" ")
    print('=' * 50)
    with open ("Enkripsi.txt", 'w+', encoding="utf-8") as f:
        for data in enkripsi :
            z = chr(data)
            a = ''.join(z)
            f.write(a)
except(FileNotFoundError):
    print("\nFile tidak ditemukan...")
except(ValueError):
    print("\nMasukkan angka yang valid")


    
    

    
