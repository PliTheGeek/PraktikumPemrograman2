
#Tugas Kode Ke 1

array = []

jumlah = int(input("Masukkan Jumlah Kata  : "))



for i in range (jumlah):
    
    kata = input("Masukan Kata : ")

    array.append(kata)

    
print("Didalam Array Terdata Kata :",array)

cari = input("Masukkan Kata Yang Mau Dicari : " )

if cari in array:
    print(f"Kata yang Kamu Cari Ada Kok Nih! '{cari}' Indeks Ke : ", array.index(cari))

else:
    print(f"Kata {cari} Yang kamu Cari Gaada")