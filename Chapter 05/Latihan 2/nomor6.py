from random import randint
bilTebak = randint (0,100)
sum = 0
print ("Halo... Nama saya Mr. Komputer :D")
print ("Saya telah memilih bilangan secara acak dari 0 - 100")
print ("Coba tebak, bilangan berapakah itu?? :)))")
while True :
    bilAnda = int ( input ("Silahkan masukkan tebakkan Anda :"))

    if (bilAnda > 0) and (bilAnda < bilTebak):
        print ("Ups... Kurang tepat, bilangan Anda terlalu kecil")
        sum += 1
    elif (bilAnda < 100) and (bilAnda > bilTebak):
        print ("Yahhh... Masih salah, bilangan Anda terlalu besar")
        sum += 1
        continue
    elif (bilAnda == bilTebak):
        print ("\nSelamatttt tebakan Anda tepat :>")
        score = 100 - sum * 2
        if ( score > 0):
            print ("Score Anda = ", score)
        else :
            print ("Yahhh... Maaf score Anda nol, Anda gagal :(((")
        break
    else :
        print ("\nIngat yaa, bilangan 0 - 100 :D ")
        continue
