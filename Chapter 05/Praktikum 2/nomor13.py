sum = 0
from random import randint
while True :
    bil = randint(0,10)
    print (bil)
    sum += 1
    if (bil == 5):
        print ("Jumlah perulangan : ", sum)
        break
