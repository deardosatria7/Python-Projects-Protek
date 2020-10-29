def starFormation3 (n):
    i = 0
    while ( i < n/2 ):
        i += 1
        print ('* ' * i)
    while ( i >= n/2 or i > 0):
        i -= 1
        print ('* ' * i)
        
    
starFormation3 (9)
