nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},       
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50}, 
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30}, 
	    {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]

def nilaiAkhir (x):
    nama = {}
    nim = {}
    for i in range (len(x)):
        nilai_akhir = ((x[i]['mid'])+ (2*(x[i]['uas'])))/3
        nama[x[i]['nama']] = nilai_akhir
        nim[x[i]['nim']] = nilai_akhir
    namaMax = max(nama, key=nama.get)
    nimMax = max(nim, key=nim.get)
    print ("Mahasiswa dengan nilai akhir tertinggi adalah", namaMax, "( nim : ",nimMax,")")

nilaiAkhir(nilaiMhs)
        
