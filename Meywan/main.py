# percabangan
# percabangan 1 kondisi

# struktur percabangan
"""
   1. if -nya
   2. kondisinya,statement yang harus
   terpenuhi agar aksi di jalankan
   3.aksinya
"""

nama = input("Masukan nama anda!")

# percabangan
# if <kondisi> : <aksi>
if nama == "adam": print("selamat datang")
print("terima kasih") #bukan aksi

# percabangan dengan idensitas
if nama == "adam":# kondisi
    print("selamat datang")
    print("selamat belajar")
print("terim kasih")

#percabangan dengan else statement
if nama == "adam":
    print("selamat datang")
else:
    print("anda bukan adam")

print("program berakhir")
