from datetime import *
now = datetime.date(datetime.now())

def tgl_pinjam():
    import datetime
    n = True
    while n == True :
        try :
            tgl = input("Tanggal mulai pinjam (yyyy-mm-dd) \t:")
            tgl_split = tgl.split('-')
            x = [int(i) for i in tgl_split]
            global tglPinjam
            tglPinjam = datetime.date(x[0], x[1], x[2])
            n = False
        except(ValueError):
            print("\nMasukkan format tanggal yang benar! (yyyy-mm-dd)")
        except (IndexError):
            print("\nMasukkan format tanggal yang benar! (yyyy-mm-dd)")
            
        
with open("dataPerpus.txt", 'a+')as f:
    status = True
    while status == True:
        data = []
        kode = input("Masukkan kode member \t\t\t:" )
        data.append(kode)
        nama = input("Nama member \t\t\t\t:")
        data.append(nama)
        buku = input("Judul buku yang dipinjam \t\t:")
        tgl_pinjam()
        week = tglPinjam + timedelta(days=7)
        data.append(buku)
        data.append(str(tglPinjam))
        data.append(str(week))
        gabung = '|'.join(data)
        f.write(gabung + '\n')
        konfirmasi = input("\nIngin menambah data lainnya? (y/n) \t:")
        if konfirmasi != 'y':
            status = False
            print("\nFile telah dibuat dengan nama dataPerpus.txt")
        
        
