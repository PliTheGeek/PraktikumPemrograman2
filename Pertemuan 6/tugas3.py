def kalkulasi(pilih):

    bil1 = int(input("Masukkan Bil 1: "))
    bil2 = int(input("Masukkan Bil 2: "))
    
    if (pilih == 1):
       hasil = bil1 + bil2
       print("Hasil Penjumlahan : ",hasil)

    elif(pilih == 2):
        hasil = bil1 * bil2
        print("Hasil Perkalian : ",hasil)

    elif(pilih == 3):
        hasil = bil1 - bil2
        print("Hasil Pengurangan : ",hasil)

    elif(pilih == 4):
        hasil = bil1 / bil2
        print("Hasil Pembagian : ",hasil)

    else:
        print("Pilihan Tidak Sesuai")

print("1.Penjumlahan")
print("2.Perkalian")
print("3.Pengurangan")
print("4.Pembagian")

pilih = int(input("Masukkan Pilihan : "))

kalkulasi(pilih)