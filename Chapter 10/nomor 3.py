print ("Program ini akan membuka \"Data Mhs.txt\" dari hasil program nomor 2 \n")
dicti = {'nim' : '' , 'nama' : '' , 'asal' : ''}
baru = []
with open("Data Mhs.txt") as file:
    for data in file :
        my_list = data.split(' | ')
        for key in dicti:
            dicti['nim']=my_list[0]
            dicti['nama']=my_list[1]
            dicti['asal']=(my_list[2][:-1])
        print(dicti)
