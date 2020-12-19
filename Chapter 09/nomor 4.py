import random

def shuffleString (kata, n):
    memori = []
    while (len(memori) < n):
        i = random.sample(kata, len(kata))
        hasil = ''.join(i)
        if hasil not in memori :
            memori.append(hasil)

    print (memori)


shuffleString('aku', 4)
