#String

#Masalah
'''
Perusahan Otobus Bagong Jaya sudah berdiri sejak lama dan memiliki banyak armada untuk disewakan kepada pengguna.
Armada yang terlalu banyak membuat tim dari PO Bagong Jaya kesusahan untuk menentukan bis tersebut bermesin apa, hasil karoseri
mana dan juga tahun keluaran apa. Informasi tersebut dibutuhkan ketika ingin menservis bis dan juga bila pengguna menanyakan
armada apa yang akan dipakai nantinya.Bantulah PO Bis Bagong Jaya dalam membuat program yang berfungsi untuk mengetahui bis itu 
bermesin apa, keluaran tahun berapa, dan hasiil karoseri mana. Berikut ketentuannya :
Format penulisan kode : KODE MESIN-KODE KAROSEI-TAHUN
Kode Mesin : Hino (HN), Mercedes Benz (MB), Scania (SC)
Kode karoseri : Adiputro (AP), Laksana (LK), Tentrem(TR)
Tahun mengikuti kode, jika kode 17 maka tahun 2017. Semua bus diproduksi di atas tahun 2010.
'''

#Alur
'''
Input :
- Kode bis

Proses :
- Pemisahan tiap kode bis
- Percabangan tiap kode mesin dan karoseri
- Penentuan tahun

Output :
= Mesin yang digunakan
- Karoseri yang dipakai
- Tahun keluaran

'''

#Program
print(10*"=","Selamat Datang",10*"=")
print("Format penulisan kode Bis sebagai berikut.\nContoh : MB-AP-21")

def kodemesin(mesin):
    if mesin == "HN":
        print("Mesin\t\t: Hino")
    elif mesin == "MB":
        print("Mesin\t\t: Mercedes Benz")
    elif mesin == "SC":
        print("Mesin\t\t: Scania")
    else:
        print("Kode Mesin Tidak Tersedia")

def kodekaroseri(karoseri):
    if karoseri == "AP":
        print("Karoseri\t: Adi Putro")
    elif karoseri == "LK":
        print("Karoseri\t: Laksana")
    elif karoseri == "TR":
        print("Karoseri\t: Tentrem")
    else:
        print("Kode Karoseri Tidak Tersedia")

def kodetahun(tahun):
    tahunbuat = "20"+tahun
    print(f"Tahun pembuatan\t: {tahunbuat}")

while True:
    kode = input("\nKode Bis\t: ")
    kode = kode.upper()
    kode = kode.split("-")

    kodemesin(kode[0])
    kodekaroseri(kode[1])
    kodetahun(kode[2])

    pilih = input("Lanjut atau Tidak? (Y/T) : ")
    pilih = pilih.upper()
    if pilih == "Y":
        continue
    elif pilih == "T":
        print("Terima Kasih")
        break
    else:
        print("Invalid")