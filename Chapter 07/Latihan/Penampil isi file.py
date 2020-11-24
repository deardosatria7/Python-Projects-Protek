try :
    file = input ("Masukkan alamat file yang ingin Anda tampilkan : ")
    bukaFile = open(file, "r")
    print ("Berikut adalah isi file tersebut", "\n")
    print(bukaFile.read())       
except (FileNotFoundError):
    print("File tidak ditemukan", "\nMohon masukkan alamat yang tepat")
            
