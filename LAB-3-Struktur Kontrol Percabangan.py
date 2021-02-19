#Struktur Kontrol Percabangan

#Masalah
'''Sekolah Minggu Gereja Imperfect akan membagikan hadiah bagi anak-anak yang tergabung dalam gereja ini. Bu Mei kebingungan untuk 
menghitung dana hadiah yang diperoleh setiap anak. Berikut ini kriteria yang harus diperhatikan Bu Mei dalam menentukan dana hadiah 
tiap murid.
1. Kelas Kecil
- Jumlah kehadiran 1 s/d 5 = Rp. 100.000
- Jumlah kehadiran 6 s/d 10 = Rp. 150.000
- Jumlah kehadiran 11 s/d 15 = Rp. 200.000
1. Kelas Besar
- Jumlah kehadiran 1 s/d 5 = Rp. 150.000
- Jumlah kehadiran 6 s/d 10 = Rp. 200.000
- Jumlah kehadiran 11 s/d 15 = Rp. 250.000
Bantulah Bu Mei dengan membuat program untuk mentukan dana hadiah tiap anak berdasarkan ketentuan di atas. Program tersebut juga harus
dilengkapi penanganan kesalahan jika Bu Mei memasukkan input yang tidak sesuai
'''

#Alur
'''
Input :
- Input kelas murid.
- Input jumlah kehadirannya.

Proses :
- Percabangan antar kelas.
- Percabangan jumlah kehadiran.

Output :
- Dana hadiah tiap murid.

'''

#Program
print(10*'=',"Program Penghitung Dana Hadiah Sekolah Minggu",10*'=')
print("Untuk mendapatkan nilai dana hadiah tiap murid, masukkan kelas murid dan jumlah kehadirannya.")

kls = str(input("Masukkan kelas murid = "))
kelas = kls.lower()

try:
    absen = int(input("Masukkan jumlah kehadiran murid = "))
    if kelas == "kecil":
        if absen >= 1 and absen <= 5:
            print("Dana hadiah murid = Rp. 100.000")
        elif absen >= 6 and absen <= 10:
            print("Dana hadiah murid = Rp. 150.000")
        elif absen >= 11 and absen <= 15:
            print("Dana hadiah murid = Rp. 200.000")
        else:
            print("Jumlah kehadiran hanya antara 1 s/d 15")
    elif kelas == "besar":
        if absen >= 1 and absen <= 5:
            print("Dana hadiah murid = Rp. 150.000")
        elif absen >= 6 and absen <= 10:
            print("Dana hadiah murid = Rp. 200.000")
        elif absen >= 11 and absen <= 15:
            print("Dana hadiah murid = Rp. 250.000")
        else:
            print("Jumlah kehadiran hanya antara 1 s/d 15")
    else:
        print("Hanya ada 2 pilihan kelas, yaitu kecil atau besar")
except:
    print("Input kehadiran harus berupa angka")