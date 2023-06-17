
# Program Biodata 

nama = str(input('Masukkan Nama :'))
ttl = input('Masukkan TTL :')
alamat = input('Masukkan Alamat:')
umur = input('Masukkan Umur:')
phone = input('Masukkan No.Telp:')
study = input('Masukkan Program Studi :')
hobi = str(input('Masukkan Hobi :'))

biodata = "Halo {} Kelahiran Asal {} \nAlamat {}  Usia {} Nomor Telepon {} Mengambil Studi {} Memiliki hobi {}"

print(biodata.format(nama,ttl,alamat,umur,phone,study,hobi))



