#Dictionary

#Masalah
'''
Siti baru saja membuat bisnis kecil. Namun, ia masih melakukan perhitungan secara manual. Ia tidak punya program kasir.
Sebagai teman yang baik Anda ingin membantunya dengan membuat program kasir di mana program ini juga bisa melakukan
penyimpanan harga dari item yang diinputkan.
'''

#Alur
'''
Input :
- Nama barang
- Harga barang
- Kuantitas barang

Proses :
- Melakukan penyimpanan nama barang dan harganya di dictionary
- Mengakses isi dari dictionary
- Melakukan perhitungan

Output :
- Total harga yang harus dibayarkan

'''

#Program
data_barang = dict() #{kopi:2000}

while True:
    print("\nPilihan menu :\n1. Input data barang dan harga\n2. Program Kasir \n3. Exit")

    pilihan = int(input("Apa yang ingin Anda lakukan? "))

    if pilihan == 1:
        nama = input("Nama barang : ").lower()
        harga = int(input("Harga satuan : "))

        data_barang[nama] = harga
    elif pilihan == 2:
        print(10*"=","Selamat Datang di Program Kasir",10*"=")
        print("Masukkan 0 untuk berhenti")
        total = 0

        while True:
            barang = input("Nama barang : ").lower()
            if barang == '0':
                break
            jumlah = int(input("Jumlah barang : "))

            try:
                harga = data_barang.get(barang,"Barang tidak tersedia")
                total += (harga*jumlah)
            except:
                print("Barang tidak tersedia.\nTolong masukkan barang lain")
        print(f"Total harga : Rp.{total}")
        
    elif pilihan == 3:
        print("Terimakasih")
        break

    else:
        print("Input tidak sesuai")  
    
