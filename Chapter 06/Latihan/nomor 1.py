print ("Aplikasi triple pythagoras checker", "\nsisi a, b, dan c (sisi miring)")
a= int (input ("    Nilai a="))
b= int (input ("    Nilai b="))
c= int (input ("    Nilai c="))

def isPythagoras (a, b, c):
    if (a % 3 == 0 and b % 4 == 0 and c % 5 == 0):
        print ("Benar, nilai yang anda masukkan termasuk dalam triple pythagoras")
    elif (a % 5 == 0 and b % 12 == 0 and c % 13 == 0):
        print ("Benar, nilai yang anda masukkan termasuk dalam triple pythagoras")
    elif (a % 7 == 0 and b % 24 == 0 and c % 25 == 0):
        print ("Benar, nilai yang anda masukkan termasuk dalam triple pythagoras")
    elif (a % 8 == 0 and b % 15 == 0 and c % 17 == 0):
        print ("Benar, nilai yang anda masukkan termasuk dalam triple pythagoras")
    elif (a % 9 == 0 and b % 40 == 0 and c % 41 == 0):
        print ("Benar, nilai yang anda masukkan termasuk dalam triple pythagoras")
    else :
        print ("Salah, nilai yang anda masukkan tidak termasuk dalam triple pythagoras")

isPythagoras (a, b, c)
