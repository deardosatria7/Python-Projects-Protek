def bintang2(n):
    i = 0
    j = 1
    while i < n/2 :
        star = '*' * j
        i += 1
        j += 2
        print (star.center(n+n))
    j -= 2
    while (i >= n/2) :
        j -= 2
        i += 1
        star = '*' * j
        print (star.center(n+n))
        if i == n :
            break

bintang2 (9)
