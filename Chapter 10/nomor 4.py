print('=' * 80)
print("Program untuk mencari data mahasiswa/i berdasarkan NIM")
print("Daftar mahasiswa/i adalah file yang telah dibuat berdasarkan nomor 2")
print('-'*80)
nim = input ("Masukkan NIM dari Mahasiswa/i yang ingin dicari : ")
daftar = []
with open("Data Mhs.txt") as file:
    for data in file :
        my_list = data.split(' | ')
        daftar.append(my_list[0])
        daftar.append(my_list[1])
        daftar.append(my_list[2][:-1])
    if nim in daftar :
        print("\nData Mahasiswa")
        print("NIM\t\t:", nim)
        print("Nama\t\t:", daftar[(daftar.index(nim)+1)])
        print("Alamat\t\t:", daftar[(daftar.index(nim)+2)])
        print('='*80)
    else :
        print("\nNIM yang Anda masukkan tidak ditemukan dalam data")
        print('='*80)

    
