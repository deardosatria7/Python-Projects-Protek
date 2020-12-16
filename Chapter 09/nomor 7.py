mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO', 
       'K002:DWI AMALIA FITRIANI:1979-09-17:KUDUS',
       'K003:FAZA FAUZAN:2005-01-28:KARANGANYAR']
print ('=' * 65)
print ("NIM", "\tNAMA", "\t\t\t TGL.LAHIR", "\t TEMPAT LAHIR")
print ('-' * 65)

for data in mhs :
    mhs1 = data.split(':')
    print (mhs1[0],"\t", end='')
    print (mhs1[1],"\t",end='')
    tgl = mhs1[2].split('-')
    tgl.reverse()
    tgl_fix = '/'.join(tgl)
    if (len(mhs1[1])>11):
        print ("",tgl_fix,end='') 
    else :
        print ("\t",tgl_fix,end='')
    print ("\t",mhs1[3])
print ('=' * 65)


    


