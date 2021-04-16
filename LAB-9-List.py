#List

#Masalah
'''
Ridho baru saja membuat toko kecil-kecilan. Namun, ia seringkali kebingungan utk melihat stok barang dagangannya.
Sebagai teman yang baik Anda ingin membantu Ridho dengan membuat program yang bisa menghitung stok barang.
Di mana pada program ini bisa digunakan utk menambah, mengurangi stok barang, dan menampilkan stok barang.
'''

#Alur
'''
Input :
- nama barang
- kuantitas

Proses :
- memasukkan barang ke data list
- meremove isi dari list
- mengakses isi dari list utk menampilkan stok

Output :
- stok barang

'''

#Program
stokBarang = []

while True:
    print("\nApa yang ingin Anda lakukan?\n1. Menambah stok barang\n2.Mengurangi stok barang\n3. Tampilkan stok barang")

    pilihan = int(input("Pilihan Anda : "))

    if pilihan == 1:
        barang = input("Nama barang : ").lower()
        kuantitas = int(input("Jumlah barang : "))

        for i in range(1,kuantitas+1):
            stokBarang.append(barang)
    
    elif pilihan == 2:
        barang = input("Nama barang : ").lower()
        kuantitas = int(input("Jumlah barang : "))

        if barang not in stokBarang:
            print("Barang tersebut tidak tersedia")
        else:
            for i in range(1,kuantitas+1):
                stokBarang.remove(barang)
    
    elif pilihan == 3:
        stokBarang2 = set(stokBarang)

        for i in stokBarang2:
            hitung = stokBarang.count(i)
            print(f"{i}\t : {hitung}")
        break

    else:
        print("Pilihan tidak tersedia.")