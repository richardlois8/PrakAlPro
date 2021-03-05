#Struktur Kontrol Perulangan

#Masalah
'''
Guru SMAK Santo Paulus tiap masa kelulusan wajib menentukan predikat yang akan diberikan kepada tiap murid. Predikat tersebut 
diperoleh berdasarkan nilai akhir yang didapat oleh tiap murid. Berikut ini akan diberikan kriteria tiap predikat. Buatlah 
sebuah program yang dapat membantu guru-guru tersebut. Terdapat beberapa ketentuan yang perlu diperhatikan dalam program tsb.
Kriteria nilai akhir:
1. Nilai akhir A = Dengan Pujian
2. Nilai akhir B = Sangat Memuaskan
3. Nilai akhir C = Memuaskan
4. Nilai akhir D = Cukup
Program yang dibuat hanya bisa diakses oleh bagian kurikulum atau walikelas dengan username berikut "kurikulum" dan "walikelas"
Program akan berjalan terus hingga pengguna memilih exit.
'''

#Alur
'''
Input :
- Username
- Nilai akhir murid
- Nama

Proses :
- Masuk ke program dengan username
- Looping menu program hingga pengguna memilih exit
- Percabangan pemmilihan menu
- Percabangan nilai akhir
- Looping untuk mengeluarkan data yang telah diinput

Output :
- Predikat nilai akhir
- Kumpulan data dan predikat yang telah diinputkan
'''

#Program
print(10*"=","SELAMAT DATANG DI SIPENIR",10*"=")

datauser = ["kurikulum","walikelas"]
username = str(input("Masukkan username Anda : "))
dataPredikat = []

while username in datauser:
    print("\nPilihan menu : \n1. Predikat Nilai Akhir \n2. Data murid dan predikat \n3. Exit")
    pilihan = int(input("Masukkan pilihan Anda : "))
    if pilihan == 1:
        nama = str(input("Masukkan nama murid : "))
        nilai = str(input("Masukkan nilai akhir : "))
        nilai = nilai.upper() 
        if nilai == "A":
            predikatA = "Predikat : Dengan Pujian"
            print(predikatA)
            NamaPredikat = nama+" dengan "+predikatA
            dataPredikat.append(NamaPredikat)
        elif nilai == "B":
            predikatB = "Predikat : Sangat Memuaskan"
            print(predikatB)
            NamaPredikat = nama+" dengan "+predikatB
            dataPredikat.append(NamaPredikat)
        elif nilai == "C":
            predikatC = "Predikat : Memuaskan"
            print(predikatC)
            NamaPredikat = nama+" dengan "+predikatC
            dataPredikat.append(NamaPredikat)
        elif nilai == "D":
            predikatD = "Predikat : Cukup"
            print(predikatD)
            NamaPredikat = nama+" dengan "+predikatD
            dataPredikat.append(NamaPredikat)
        else:
            print("Tidak ada nilai tersebut. Masukkan kembali nilai lain.")
    elif pilihan == 2:
        for i in dataPredikat:
            print(i)
    elif pilihan == 3:
        print("\nTerimakasih sudah menggunakan program ini.")
        break
else:
    print("Maaf Anda tidak dapat masuk ke program ini. Username Anda tidak memenuhi syarat.")