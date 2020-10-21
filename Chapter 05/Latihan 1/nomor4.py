golA = 10000000
potA = 0.025
gajiA = golA * potA
percentageA = "{:.1%}".format(potA)
golB = 8500000
potB = 0.02
gajiB = golB * potB
percentageB = "{:.1%}".format(potB)
golC = 7000000
potC = 0.015
gajiC = golC * potC
percentageC = "{:.1%}".format(potC)
golD = 5500000
potD = 0.01
gajiD = golD * potD
percentageD = "{:.1%}".format(potD)

kode1 = input ("Silahkan masukkan kode karyawan   :")
nama1 = input ("Silahkan masukkan nama karyawan   :")
gol1 = input ("Masukkan golongan (huruf kapital) :")

if ( gol1 == 'A'):
    print ("==========================================")
    print ("STRUK RINCIAN GAJI KARYAWAN")
    print ("------------------------------------------")
    print ("Nama Karyawan        :", nama1, "(kode: ", kode1,")")
    print ("Golongan             :", gol1)
    print ("------------------------------------------")
    print ("Gaji Pokok           : Rp ", golA)
    print ("Potongan (", percentageA,")    : Rp ", gajiA)
    print ("------------------------------------------")
    print ("Gaji bersih          : Rp ", golA - gajiA)
    
elif ( gol1 == 'B'):
    print ("==========================================")
    print ("STRUK RINCIAN GAJI KARYAWAN")
    print ("------------------------------------------")
    print ("Nama Karyawan        :", nama1, "(kode: ", kode1,")")
    print ("Golongan             :", gol1)
    print ("------------------------------------------")
    print ("Gaji Pokok           : Rp ", golB)
    print ("Potongan (", percentageB,")    : Rp ", gajiB)
    print ("------------------------------------------")
    print ("Gaji bersih          : Rp ", golB - gajiB)
    
elif ( gol1 == 'C'):
    print ("==========================================")
    print ("STRUK RINCIAN GAJI KARYAWAN")
    print ("------------------------------------------")
    print ("Nama Karyawan        :", nama1, "(kode: ", kode1,")")
    print ("Golongan             :", gol1)
    print ("------------------------------------------")
    print ("Gaji Pokok           : Rp ", golC)
    print ("Potongan (", percentageC,")    : Rp ", gajiC)
    print ("------------------------------------------")
    print ("Gaji bersih          : Rp ", golC - gajiC)

elif ( gol1 == 'D'):
    print ("==========================================")
    print ("STRUK RINCIAN GAJI KARYAWAN")
    print ("------------------------------------------")
    print ("Nama Karyawan        :", nama1, "(kode: ", kode1,")")
    print ("Golongan             :", gol1)
    print ("------------------------------------------")
    print ("Gaji Pokok           : Rp ", golD)
    print ("Potongan (", percentageD,")    : Rp ", gajiD)
    print ("------------------------------------------")
    print ("Gaji bersih          : Rp ", golD - gajiD)

print ("\n") 
print ("-------------TERIMA KASIH-----------------")
