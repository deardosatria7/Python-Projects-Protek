print('=' * 70)
print("Program penghitung dua bilangan")
print('-' * 70)
print("bilangan-bilangan tersebut berada dalam file \"number.txt\" \npada folder yang sama dengan kode python ini")
print('-' * 70)
print("Hasil penjumlahan akan disimpan dalam file bernama \"hasil jumlah.txt\" \npada folder yang sama")
print('-' * 70)
hasil = []
baru = []
with open("number.txt", 'r') as file:
    text = file.read()
    mentah = text.split('\n')
    ab = mentah[:-1]
    for data in ab:
        angka = data.split('|')
        for data in angka:
            hasil.append(int(data))
    i = 0
    j = 1
    while j < len(hasil):
        hasil1 = hasil[i] + hasil[j]
        baru.append(hasil1)
        i += 2
        j += 2
with open ("hasil jumlah.txt", 'w+') as f:
    for data in baru:
        tulis = str(data)
        f.write(tulis + '\n')
print("File telah dibuat")
print('=' * 70)
    
      
