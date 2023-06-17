def menerimaMHS(menu):

    while menu != 5:
       

        if menu == 1:
            
            array = []
            jumlah = int(input("Masukkan Jumlah Mahasiswa : "))
            for i in range(jumlah):
                nama = input("Masukkan Nama Mahasiswa : ")
                array.append(nama)

        elif menu == 2:
            print("Data Mahasiswa : ",array)
            hapus = input("Masukkan Nama Mahasiswa Yang Mau Dihapus : ")
            array.remove(hapus)
            print("Data Mahasiswa : ",array)
        
        elif menu == 3:
            print("Urutkan Data Mahasiswa")
            array.sort()
            print("Data Mahasiswa : ",array)
            
        elif menu == 4:
            print("Lihat Data Mahasiswa",array)
                

        else:
            print("Menu tidak tersedia")
        menu = int(input("Pilih menu :  "))
   
    print("Terimakasih..")       
    
            
           
    


print(" <=== Menu Data Mahasiswa ===> ")
print("1. Tambah Data Mahasiswa")
print("2. Hapus Data Mahasiswa")
print("3. Urutkan Data Mahasiswa")
print("4. Lihat Data Mahasiswa")
print("5. Tutup")
print("------------------")


menu = int(input("Pilih menu :  "))
menerimaMHS(menu)
