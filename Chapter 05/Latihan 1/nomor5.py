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

kode1 = input ("Silahkan masukkan kode karyawan          :")
nama1 = input ("Silahkan masukkan nama karyawan          :")
gol1 = input ("Masukkan golongan (huruf kapital)        :")
menikah = input ("Masukkan status (1=menikah, 2=belum)     :")
if ( menikah == '1'):
    jmlAnak = int ( input ("Masukkan jumlah anak                     :"))
else :
    print("")
    
if ( gol1 == 'A'):
    print ("==============================================================")
    print ("STRUK RINCIAN GAJI KARYAWAN")
    print ("--------------------------------------------------------------")
    print ("Nama Karyawan               :", nama1, "(kode: ",kode1,")")
    print ("Golongan                    :", gol1)
    if (menikah == '1'):
        print ("Status Menikah              : Menikah")
        print ("Jumlah anak                 : ",jmlAnak)
    else :
        print ("")
        
    print ("--------------------------------------------------------------")
    print ("Gaji Pokok                  : Rp ", golA)
    if (menikah == '1'):
        print ("Tunjangan Istri/Suami       : Rp ", golA * 0.1)
        print ("Tunjangan anak              : Rp ", jmlAnak * 5/100 * golA)
        print ("Gaji Kotor                  : Rp ", golA + (golA * 0.1) + (jmlAnak * 5/100 * golA))
        print ("--------------------------------------------------------------+")
        print ("Potongan (", percentageA,")           : Rp ", gajiA)
        print ("--------------------------------------------------------------")
        print ("Gaji Bersih                 : Rp ", (golA + (golA * 0.1) + (jmlAnak * 5/100 * golA))- gajiA)

    else :
        print ("Potongan (", percentageA,")           : Rp ", gajiA)
        print ("--------------------------------------------------------------")
        print ("Gaji bersih                 : Rp ", golA - gajiA)

elif ( gol1 == 'B'):
    print ("===============================================================")
    print ("STRUK RINCIAN GAJI KARYAWAN")
    print ("---------------------------------------------------------------")
    print ("Nama Karyawan               :", nama1, "(kode: ",kode1,")")
    print ("Golongan                    :", gol1)
    if (menikah == '1'):
        print ("Status Menikah              : Menikah")
        print ("Jumlah anak                 : ",jmlAnak)
    else :
        print ("")
        
    print ("---------------------------------------------------------------")
    print ("Gaji Pokok                  : Rp ", golB)
    if (menikah == '1'):
        print ("Tunjangan Istri/Suami       : Rp ", golB * 0.1)
        print ("Tunjangan anak              : Rp ", jmlAnak * 5/100 * golB)
        print ("Gaji Kotor                  : Rp ", golB + (golB * 0.1) + (jmlAnak * 5/100 * golB))
        print ("---------------------------------------------------------------+")
        print ("Potongan (", percentageB,")           : Rp ", gajiB)
        print ("---------------------------------------------------------------")
        print ("Gaji Bersih                 : Rp ", (golB + (golB * 0.1) + (jmlAnak * 5/100 * golB))- gajiB)

    else :
        print ("Potongan (", percentageB,")           : Rp ", gajiB)
        print ("---------------------------------------------------------------")
        print ("Gaji bersih                 : Rp ", golB - gajiB)

elif ( gol1 == 'C'):
    print ("===============================================================")
    print ("STRUK RINCIAN GAJI KARYAWAN")
    print ("---------------------------------------------------------------")
    print ("Nama Karyawan               :", nama1, "(kode: ",kode1,")")
    print ("Golongan                    :", gol1)
    if (menikah == '1'):
        print ("Status Menikah              : Menikah")
        print ("Jumlah anak                 : ",jmlAnak)
    else :
        print ("")
        
    print ("---------------------------------------------------------------")
    print ("Gaji Pokok                  : Rp ", golC)
    if (menikah == '1'):
        print ("Tunjangan Istri/Suami       : Rp ", golC * 0.1)
        print ("Tunjangan anak              : Rp ", jmlAnak * 5/100 * golC)
        print ("Gaji Kotor                  : Rp ", golC + (golC * 0.1) + (jmlAnak * 5/100 * golC))
        print ("---------------------------------------------------------------+")
        print ("Potongan (", percentageC,")           : Rp ", gajiC)
        print ("---------------------------------------------------------------")
        print ("Gaji Bersih                 : Rp ", (golC + (golC * 0.1) + (jmlAnak * 5/100 * golC))- gajiC)

    else :
        print ("Potongan (", percentageC,")           : Rp ", gajiC)
        print ("---------------------------------------------------------------")
        print ("Gaji bersih                 : Rp ", golC - gajiC)

elif ( gol1 == 'D'):
    print ("==================================================================")
    print ("STRUK RINCIAN GAJI KARYAWAN")
    print ("------------------------------------------------------------------")
    print ("Nama Karyawan               :", nama1, "(kode: ",kode1,")")
    print ("Golongan                    :", gol1)
    if (menikah == '1'):
        print ("Status Menikah              : Menikah")
        print ("Jumlah anak                 : ",jmlAnak)
    else :
        print ("")
        
    print ("------------------------------------------------------------------")
    print ("Gaji Pokok                  : Rp ", golD)
    if (menikah == '1'):
        print ("Tunjangan Istri/Suami       : Rp ", golD * 0.1)
        print ("Tunjangan anak              : Rp ", jmlAnak * 5/100 * golD)
        print ("Gaji Kotor                  : Rp ", golD + (golD * 0.1) + (jmlAnak * 5/100 * golD))
        print ("------------------------------------------------------------------+")
        print ("Potongan (", percentageD,")           : Rp ", gajiD)
        print ("------------------------------------------------------------------")
        print ("Gaji Bersih                 : Rp ", (golD + (golD * 0.1) + (jmlAnak * 5/100 * golD))- gajiD)

    else :
        print ("Potongan (", percentageD,")           : Rp ", gajiD)
        print ("------------------------------------------------------------------")
        print ("Gaji bersih                 : Rp ", golD - gajiD)


print ("\n") 
print ("---------------------TERIMA KASIH--------------------------")
