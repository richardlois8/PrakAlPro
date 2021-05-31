#Regex

#Masalah
'''
Perusahaan "Gemilang Jaya" sedang kesulitan melakukan pendataan barangnya. Namun, perusahaan ini memiliki sebuah file
yang berisi data pembelian barang dari konsumen. Apabila dilakukan pendataan secara manual maka akan memakan waktu yang
sangat lama. Oleh karena itu, perusahaan ini meminta bantuanmu untuk melakukan pendataan kode barang dari perusahaan tersebut.
Output yang diinginkan adalah kode barang beserta nama barangnya. 
'''

#Alur
'''
Input :
- Nama file

Proses :
- Membuka file
- Mengakses tiap baris dalam file
- Mencari string yang cocok dengan pola dalam regex

Output :
- Kode barang
- Nama barang
- Harga barang
'''

#Program
import re

try:
    namaFile = input("Nama file : ")
    file = open(namaFile)
except:
    print("File tidak tersedia")

print("Kode Barang\t\tNaama Barang\t\t\tHarga")
for baris in file:
    try:
        kodeBarang = re.search("\w{3}\-\d{3}\-\w+",baris).group()
        namaBarang = re.search("\[\w.+\]",baris).group()
        namaBarang = namaBarang[1:len(namaBarang)-1]
        hargaBarang = re.search("\d+\.\d+\.?\d+",baris).group()
        print(f"{kodeBarang}\t\t{namaBarang}\t\t{hargaBarang}")
    except:
        continue