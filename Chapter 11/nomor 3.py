def diffDate(x):
    # x dalam bentuk ('yyyy-mm-dd')
    import datetime
    now = datetime.datetime.now()
    tgl_now = datetime.datetime(now.year, now.month, now.day)
    x_split = x.split('-')
    y = [int(i) for i in x_split]
    tgl_input = datetime.datetime(y[0], y[1], y[2])
    global selisih
    if tgl_now <= tgl_input:
        selisih = '-'
    elif tgl_now > tgl_input:
        global hari
        hari = tgl_now - tgl_input
        selisih = str(hari.days) + ' hari'

from datetime import *
now = datetime.date(datetime.now())

with open("dataPerpus.txt") as f:
    datax = []
    for text in f:
        splited = text.split('|')
        for data in splited:
            datax.append(data)
    print("Data peminjaman diambil dari dataPerpus.txt hasil nomor 1")
    kode = input("Masukkan kode member :")
    if kode in datax:
        print("\nKode Member \t\t\t:", kode)
        print("Nama Member \t\t\t:", datax[datax.index(kode)+1])
        print("Judul buku \t\t\t:", datax[datax.index(kode)+2])
        print("Tanggal mulai pinjam\t\t:", datax[datax.index(kode)+3])
        print("Tanggal max pengembalian\t:", datax[datax.index(kode)+4][:-1])
        print("Tanggal pengembalian \t\t:", now)
        diffDate(datax[datax.index(kode)+4][:-1])
        print("Terlambat\t\t\t:", selisih)
        if selisih == '-':
            print("Denda\t\t\t\t: -")
        else:
            print("Denda\t\t\t\t: Rp", hari.days * 2000)
    else :
        print("\nKode Member tidak ditemukan")
        
        
        
        
