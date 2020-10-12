# import library
import time
import datetime

# import nama user
nama = input("Hallo... nama saya Mr. Kompie, nama anda siapa? ")

# tampilkan nama user
print ("Oh... Nama Anda", nama , ", nama yang bagus sekali.")

# kasih jeda 3 detik
time.sleep(3)

# input tahun lahir
thnLahir = int(input("BTW... " + nama + " kamu lahir tahun berapa? "))

# kasih jeda 3 detik
time.sleep(3)

# hitung usia user
skrg = datetime.datetime.now()
usia = skrg.year - thnLahir

# tampilkan usia
print ("Hmm...", nama , "kamu sudah", usia,"tahun ya...")

# kasih jeda 3 detik
time.sleep(3)

# tampilkan pesan sesuai usia
if (usia>50) :
    print ("Anda sudah cukup tua ya?")
    print ("Selalu jaga kesehatan ya...")
elif (usia>20) :
    print ("Ternyata Anda masih cukup muda belia!")
    print ("Jangan sia-siakan masa mudamu ya!!")
elif (usia>=17) :
    print ("Hihihi... Anda ternyata masih ABG" )
    print ("Mulai berpikirlah secara dewasa ya!!")
else :
    print ("Oalah... Anda masih anak-anak toh...")
    print ("Jangan suka merengek-rengek minta uang jajan ya")

# kasih jeda 3 detik
time.sleep(3)

# say goodbye
print ("Oke... See you later", nama,".. Senang berkenalan denganmu!!")

    
