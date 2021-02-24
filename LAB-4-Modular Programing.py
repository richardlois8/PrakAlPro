#Modular Programing

#Masalah
'''
Cindy baru saja lulus kuliah dan mendapat pekerjaan. Sekarang ia sudah bisa membiayai hidupnya sendiri. Gaji yang ia dapatkan cukup
besar per bulannya. Tiap bulan ia mendapat gaji pokok dan terkadang mendapat penghasilan tambahan. Namun, Cindy
termasuk orang yang boros dan tidak rapi dalam keuangan. Seringkali Cindy bingung uangnya habis untuk apa saja. Bantulah Cindy
dengan membuat fungsi yang dapat digunakan berulang kali.Fungsi ini dapat menentukan berapa budget yang dapat Cindy gunakan untuk
makan(40%), pakaian(25%), jajan(15%), dan dana darurat(20%).
'''

#Alur
'''
Input :
- Gaji
- Persen alokasi dana

Proses :
- Membuat fungsi
- Percabangan pilihan dana

Output :
- Alokasi dana sesuai kriteria
'''

#Program
def makan(gaji,persen=(40/100)):
    makan = gaji*persen
    return makan
def pakaian(gaji,persen=(25/100)):
    pakaian = gaji*persen
    return pakaian
def jajan(gaji,persen=(15/100)):
    jajan = gaji*persen
    return jajan
def darurat(gaji,persen=(20/100)):
    darurat = gaji*persen
    return darurat

print(10*"=","Selamat Datang di Program Alokasi Dana",10*"=")
gaji = int(input("Masukkan total gaji Anda = Rp. "))
print()
print("Pilihan Alokasi Dana : \n1. Makan \n2. Pakaian \n3. Jajan \n4. Dana Darurat")
pilihan = int(input("Masukkan pilihan Anda : "))

if pilihan == 1:
    print("Dana makan bulan ini sebesar Rp. ",makan(gaji))
elif pilihan == 2:
    print("Dana untuk membeli pakaian bulan ini sebesar Rp. ",pakaian(gaji))
elif pilihan == 3:
    print("Dana untuk jajan bulan ini sebesar Rp. ",jajan(gaji))
elif pilihan == 4:
    print("Dana darurat yang harus disisihkan bulan ini sebesar Rp. ",darurat(gaji))
else:
    print("Pilihan Anda tidak ada.")
