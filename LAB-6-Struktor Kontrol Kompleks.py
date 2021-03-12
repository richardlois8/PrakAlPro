#Struktur Kontrol Kompleks

#Masalah
'''
Bu Rini sedang kesulitan untuk menentukan IPK dari mahasiswa-mahasiswanya. Di mana ia harus menghitung secara manual sehingga membutuhkan
waktu yang lama. Bantulah Bu Rini dengan membuat program yang dapat menentukan IPK tiap mahasiswanya. Ketentuan untuk input nilai ada 4 
dengan bobot sebagai berikut. Tugas 1 (20%), tugas 2(20%), UTS(30%),dan UAS(30%). 
Nilai akhir >= 85 IPK = A
Nilai akhir >= 70 IPK = B
Nilai akhir >= 55 IPK = C
Nilai akhir >= 40 IPK = D
Nilai akhir < 40 IPK = E
referensi : https://kelasprogrammer.com/5-contoh-program-sederhana-python/
'''

#Alur
'''
Input :
- Nama mahasiswa
- Nilai

Proses :
- Perulangan program hingga pengguna memilih berhenti
- Percabangan untuk menentukan IPK
- Perulangan untuk mengakses data

Output :
- IPK
- Data yang telah diinputkan

'''

#Program
data_nilai = []

print(10*"=","Selamat Datang",10*"=")

while True:
    print("\nAnda ingin melakukan apa? \n1. Menghitung IPK \n2. Tampilkan data IPK")
    pilihan = int(input("Masukkan pilihan Anda : "))

    if pilihan == 1:
        nama = str(input("\nNama mahasiswa : "))
        tugas1 = float(input("Nilai Tugas 1 : "))
        tugas2 = float(input("Nilai Tugas 2 : "))
        uts = float(input("Nilai UTS : "))
        uas = float(input("Nilai UAS 1 : "))

        nilai = (tugas1*0.2)+(tugas2*0.2)+(uts*0.3)+(uas*0.3)

        if nilai >= 85:
            ipk = "IPK = A"
            nama_ipk = nama+" mendapat "+ipk
            data_nilai.append(nama_ipk)
            print(ipk)
        elif nilai >= 70:
            ipk = "IPK = B"
            nama_ipk = nama+" mendapat "+ipk
            data_nilai.append(nama_ipk)
            print(ipk)
        elif nilai >= 55:
            ipk = "IPK = C"
            nama_ipk = nama+" mendapat "+ipk
            data_nilai.append(nama_ipk)
            print(ipk)
        elif nilai >= 40:
            ipk = "IPK = D"
            nama_ipk = nama+" mendapat "+ipk
            data_nilai.append(nama_ipk)
            print(ipk)
        else:
            ipk = "IPK = E"
            nama_ipk = nama+" mendapat "+ipk+"\nMaaf Anda harus mengulang semester depan."
            data_nilai.append(nama_ipk)
            print(ipk,"\n Maaf Anda harus mengulang semester depan.")
    elif pilihan == 2:
        print("Data Mahasiswa : ")
        for i in data_nilai:
            print(i)
    else:
        print("Input tidak valid.")

    lanjut_tidak = str(input("Lanjut menggunakan program? (Y/T) "))
    lanjut_tidak = lanjut_tidak.upper()
    if lanjut_tidak == "Y":
        continue
    elif lanjut_tidak == "T":
        break
    else:
        print("Input tidak valid")