import sys
nIndo = int( input ("Silahkan masukkan nilai Bahasa Indonesia    :"))
nMat = int( input ("Silahkan masukkan nilai Matematika          :"))
nIpa = int( input ("Silahkan masukkan nilai IPA                 :"))
if (nIndo < 0 or nIndo > 100)or (nMat < 0 or nMat > 100)or (nIpa < 0 or nIpa > 100): 
    print ("Maaf, nilai yang anda masukkan ada yang tidak valid (0-100)")
    sys.exit()
    
elif (nMat > 70 and nMat <= 100) & (nIpa >= 60 and nIpa <= 100 and nIpa >= 0) & (nIndo >= 60 and nIndo <= 100 and nIndo >= 0):
    print ("Status kelulusan                            :LULUS")
elif (nMat < 70 and nMat >= 0) or (nIpa < 60 and nIpa >= 0) or (nIndo < 60 and nIndo >= 0):
    print ("Status kelulusan                            :TIDAK LULUS")
    print ("\n")
    print ("Penyebab ketidaklulusan :")
    
if (nMat < 70 and nMat > 0) :
    print ("- Nilai Matematika harus lebih dari 70")
if (nIndo < 60 and nIndo > 0) :
    print ("- Nilai Bahasa Indonesia kurang dari 60")
if (nIpa < 60 and nIpa > 0) :
    print ("- Nilai IPA kurang dari 60")
    
