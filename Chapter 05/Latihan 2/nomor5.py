from random import randint
bilTebak = randint (0,100)

print ("Halo... Nama saya Mr. Komputer :D")
print ("Saya telah memilih bilangan secara acak dari 0 - 100")
print ("Coba tebak, bilangan berapakah itu?? :)))")

while True :
    bilAnda = int ( input ("Silahkan masukkan tebakkan Anda :"))

    if (bilAnda > 0) and (bilAnda < bilTebak):
        print ("Ups... Kurang tepat, bilangan Anda terlalu kecil")
    elif (bilAnda < 100) and (bilAnda > bilTebak):
        print ("Yahhh... Masih salah, bilangan Anda terlalu besar")
        continue
    elif (bilAnda == bilTebak):
        print ("Selamatttt tebakan Anda tepat :>")
        break
    else :
        print ("Ingat yaa, bilangan 0 - 100 :D ")
        continue
