def ubah_huruf (kata, a, b):
    kata_list = list (kata)
    if a in kata_list :
        while a in kata_list :
            kata_list[kata_list.index(a)] = b
        kata = ''.join(kata_list)
        print (kata)
    elif a not in kata_list:
        print ("Huruf",a,"tidak ada dalam kata \"",kata,"\"")



