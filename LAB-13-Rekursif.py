#Rekursif

#Masalah
'''
Pak Ragil sudah cukup berumur dan ia akhir-akhir ini sedang tertarik untuk menghitung uangnya yang akan ditabung.
Pada tiap bank bunga nya tentu berbeda-beda, namun memiliki konsep penghitungan yang sama yaitu modal+bunga bulan 
pertama akan menjadi modal di bulan kedua. Pak Ragil yang sudah cukup berumur kebingungan untuk menghitungnya.
Anda sebagai keponakan yang baik akan membantunya dengan membuatkan program untuk Pak Ragil agar ia dapat mengetahui
berapa tabungannya ketika sudah mencapai bulan tertentu.
'''

#Alur
'''
Input :
- Modal awal
- Bunga per bulan
- Bulan ke berapa yang ingin diketahui

Proses :
- Membuat fungsi
- Mencari formula yang akan digunakan dalam rekursif
- Mengubah parameter sesuai dengan formula yang ditemukan

Output :
- Jumlah tabungan pada bulan yang dituju
'''

#Program

modal = int(input("Masukkan modal awal Anda : Rp. "))
bunga = int(input("Berapa bunga yang diberikan? (Tanpa persen) : "))
bunga = bunga/100
bulanTujuan = int(input("Bulan ke berapa yang ingin Anda ketahui? : "))

#bulan 1 bulan 2 bulan 3
#1000 1050 1102,5
#modal awal -> modal+bunga -> (modal+bunga) + bunga

def tabungan(modal,bulan=1):
    if bulan == bulanTujuan:
        return modal
    else:
        return tabungan(modal+(modal*bunga),bulan+1)

print(f"Tabungan Anda pada bulan ke-{bulanTujuan} adalah sebanyak Rp. {tabungan(modal)}")