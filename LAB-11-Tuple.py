#Tuple

#Masalah
'''
Dito tergabung dalam kepanitiaan di kampusnya. Ia masuk di bagian pendaftaran. Dito merupakan seorang mahasiswa Informatika.
Ia tertarik untuk membuat program yang bisa digunakan untuk mendata nama, domisili, dan no telp peserta. Namun, ia 
kesusahan membuatnya. Bantulah Dito untuk membuat program ini, di mana nantinya data yang telah diinputkan bisa
ditampilkan hanya nama dan domisili atau nama dan no telp saja.
'''

#Alur
'''
Input :
- Nama
- Domisili
- No telepon

Proses :
- Menyimpan nama dan domisili
- Menyimpan nama dan no telp
- Mengakses data yang telah diinputkan

Output :
- Nama dan domisili
- Nama dan no telp

'''

#Program
data_domisili = dict()
data_telp = dict()

while True:
    print("Halo! Selamat Datang.\n1. Input Data\n2. Tampilkan Data\n0. Berhenti")
    pilihan = int(input("\nPilihan : "))

    if pilihan == 1: 
        print("Silahkan masukkan data Anda")
        nama = input("Nama\t\t: ")
        domisili = input("Domisli\t\t: ")
        notelp = input("No Telepon\t: ")

        if list(data_domisili.items()) == [] or list(data_telp.items()) == []:
            data_domisili["Nama","Domisili"] = nama,domisili
            data_telp["Nama","No Telp"] = nama,notelp
        else:
            data_domisili["Nama","Domisili"] += nama,domisili
            data_telp["Nama","No Telp"] += nama,notelp 
    elif pilihan == 2:
        pilih_tampil = input("Tampilkan data apa (Domisili/Telepon)? ").lower()
        
        if pilih_tampil == 'domisili':
            cek_enter = 1
            for header,data in list(data_domisili.items()):
                for i in header:
                    print(i,end='\t\t')
                print(20*"-")
                for j in data:
                    print(j,end='\t\t')
                    if cek_enter % 2 == 0:
                        print()
                    cek_enter += 1
        elif pilih_tampil == 'telepon':
            cek_enter = 1
            for header,data in list(data_telp.items()):
                for i in header:
                    print(i,end='\t\t')
                print(20*"-")
                for j in data:
                    print(j,end='\t\t')
                    if cek_enter % 2 == 0:
                        print()
                    cek_enter += 1
        else:
            print("Input tidak sesuai")
    elif pilihan == 0:
        break
    else:
        print("Input tidak sesuai")
