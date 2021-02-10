# Variable, Expression, Statements

#Masalah
'''Tono pergi ke Matahalu untuk membeli beberapa pakaian. Saat melihat-lihat, Tono menemukan celana yang 
sedang di diskon. Melihat hal itu jiwa anak kost Tono bergejolak. Pada papan informasi dituliskan diskon 50% + 20%.
Melihat hal ini Tono kebingungan. Bantulah Tono dgn membuat program untuk menentukan berapa uang yang harus dibayarkan
dan berapa banyak Tono dapat menghemat uangnya?'''

'''
Input : 
- Harga pakaian
- Diskon 1
- Diskon 2

Proses:
- Hitung harga setelah di diskon 1
- Hitung harga setelah di diskon 2
- Hitung penghematan

Output:
- Jumlah uang yang harus dibayarkan Too
- Banyaknya uang yang dapat dihemat oleh Tono
'''

#Program
harga_awal = int(input('Masukkan harga awal pakaian: Rp. '))
diskon1 = int(input('Masukkan nilai diskon pertama (tanpa%): '))
diskon2 = int(input('Masukkan nilai diskon kedua (tanpa%): '))

harga2 = harga_awal-(harga_awal*(diskon1/100))
harga3 = harga2-(harga2*(diskon2/100))
hemat = harga_awal-harga3

print('Jumlah uang yang harus dibayarkan Tono sebesar: Rp. ',harga3)
print('Tono dapat menghemar uangnya sebesar : Rp.',hemat)

