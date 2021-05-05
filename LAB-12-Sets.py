#Sets

#Masalah
'''
Susan sedang bekerja di suatu toko elektronik. Pada bulan ini tokonya sedang mengadakan promo bagi pelanggan
yang membeli AC dan TV di bulan ini bisa mendapatkan sebuah Air Fryer, sedangkan yang hanya membeli salah satunya
hanya mendapatkan kipas angin. Susan sudah memiliki data pembeli TV dan AC, namun data tersebut berada di dalam 
sebuah file yang terpisah dan isinya sangat banyak. Sehingga rawan terjadi kesalahan. Susan meminta Anda sebagai
programmer untuk membuatkan sebuah program yang dapat digunakan untuk mengecek siapa saja yang mendapat 
hadiah tersbut.
'''

#Alur
'''
Input :
- Membuka file yang berisi data

Proses :
- Mengakses data yang ada di dalam file
- Menyimpan data tersebut
- Mencari data yang termasuk ke dalam 2 kategori atau hanya salah satunya saja

Output :
- Pelanggan yang membeli AC dan TV
- Pelanggan yang memvbeli AC atau TV saja
'''

#Program

pembeli_ac = input("Masukkan nama file data AC : ")
pembeli_tv = input("Masukkan nama file data TV : ")
try:
    file1 = open(pembeli_ac)
    file2 = open(pembeli_tv)
except:
    print("File tidak ditemukan")

dataAC = dict()
dataTV = dict()

for baris in file1:
    pisah = baris.split('-')
    dataAC[pisah[0]] = pisah[1]

for baris in file2:
    pisah = baris.split('-')
    dataTV[pisah[0]] = pisah[1]

simpanAC = set(dataAC.keys())
simpanTV = set(dataTV.keys())

beliKeduanya = simpanAC & simpanTV
beliAC = simpanAC - simpanTV
beliTV = simpanTV - simpanAC

print("\nPelanggan yang membeli AC dan TV serta mendapatkan Air Fryer")
for i in beliKeduanya:
    noTelp = dataAC.get(i)
    noTelp = noTelp.rstrip('\n')
    print(f"- {i}\t{noTelp}")

print("\nPelanggan yang membeli AC saja dan mendapatkan Kipas Angin")
for i in beliAC:
    noTelp = dataAC.get(i)
    noTelp = noTelp.rstrip('\n')
    print(f"- {i}\t{noTelp}")

print("\nPelanggan yang membeli TV saja dan mendapatkan Kipas Angin")
for i in beliTV:
    noTelp = dataTV.get(i)
    noTelp = noTelp.rstrip('\n')
    print(f"- {i}\t{noTelp}")