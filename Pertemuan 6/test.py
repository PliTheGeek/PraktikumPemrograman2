
# #methods dengan function

# def kelilingpersegi(sisi):
    
#     return 4*sisi

# def luaspersegi(sisi):
#     return sisi*sisi

# panjang = int(input("Masukkan Panjang Sisi "))

# print("Keliling Persegi Adalah",kelilingpersegi(panjang))
# print("Keliling Persegi Adalah",luaspersegi(panjang))

# #methods dengan prosedur

# def kelilingluaspersegi(sisi):
#     keliling = 4*sisi
#     luas = sisi*sisi

#     print("keliling persegi adalah : %d" %keliling)
#     print("Luas Persegi : %d" %luas)

# panjang = int(input("Masukkan Panjang sisi *Program Ini menggunakan Prosedur : "))
# kelilingluaspersegi(panjang)


def bandingnilai(nilai1,nilai2):

    if (nilai1 > nilai2):
        print(nilai1)

    elif(nilai1 == nilai2):
        print("Tidak Ada")

    else:
        print(nilai2)

