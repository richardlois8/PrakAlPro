#Membaca dan Menulis File

#Masalah
'''
Sebuah perusahaan yang bergerak di bidang jasa memiliki data nama, alamat, dan no telp pelanggannya yang disimpan dalam 
sebuah file data pelanggan.txt. Pelanggan yang dimiliki perusahaan ini semakin banyak sehingga proses yang biasa dilakukan untuk 
mengambil data yang dibutuhkan tidak lagi efisien. Bantulah perusahaan ini dengan membuat program yang dapat mengambil
data yang dibutuhkan oleh karyawan pada saat itu. Data yang ditampilkan tergantung apa yang diminta oleh pengguna.
Input 1 berupa identitas yang dimiliki dan input 2 apa yang dicari dari identitas tsb.
Contoh input 1 : Adi Mahendra dan input 2 : Tanggal lahir, maka outputnya adalah tgl lahir dari Adi Mahendra. 
'''

#Alur
'''
Input :
- Data yang diketahui
- Data yang dicari

Proses :
- Membuka File
- Memisahkan tiap data
- Mencari data yang diketahui berada di baris mana
- Mengakses data yang dibutuhkan
- Menutup file

Output :
- Data yang dibutuhkan
'''

#Program
handle = open("data pelanggan.txt")

ketahui = input("Data yang diketahui : ")
ketahui = ketahui.lower()
print("Data yang ingin dicari: \n1.Nama\n2.Tanggal Lahir \n3.Alamat \n4.No Telepon")
cari = int(input("Data yang ingin dicari (1-4): "))

for line in handle:
    pisah1 = line.split("|")

    for i in pisah1:
        pisah2 = i.splitlines()
        i = i.lower()

        if i.find(ketahui) != -1:
            if cari == 1:
                print(f"Nama : {pisah1[0]}")
                break
            elif cari == 2:
                print(f"Tanggal Lahir : {pisah1[1]}")
                break
            elif cari == 3:
                print(f"Alamat : {pisah1[2]}")
                break
            elif cari == 4:
                print(f"No Telepon : {pisah1[3]}")
                break
            else:
                print("Pilihan tidak ada.")
                break


handle.close()