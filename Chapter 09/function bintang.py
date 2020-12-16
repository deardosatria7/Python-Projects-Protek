def bintang(n):
    i = 0
    j = 1
    while i < n :
        star = '*' * j
        i += 1
        j += 2
        print (star.center(n+n))

bintang (10)
