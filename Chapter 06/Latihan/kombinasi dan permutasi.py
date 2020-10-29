from faktorial import *

def kombinasi (a, b):
    hasil = faktorial(a)/(faktorial(a-b) * faktorial(b))
    print ("Hasil dari kombinasi ", a, "C", b, "adalah ", hasil)

def permutasi (a, b):
    hasil = faktorial(a)/ faktorial(a-b)
    print ("Hasil dari permutasi ", a, "P", b, "adalah ", hasil)


kombinasi(5, 3)
permutasi(10, 7)
