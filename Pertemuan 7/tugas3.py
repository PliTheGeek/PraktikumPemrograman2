def insertion_asc(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] > key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
    print("after : ",array)

def insertion_desc(array):
    for i in range(1, len(array)):
        key_item = array[i]
        j = i - 1
        while j >= 0 and array[j] < key_item:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key_item
    print("after : ",array)

array = []
jumlah = int(input("Masukkan Jumlah Buku : "))
    
for i in range(jumlah):
    
    buku = input("Masukkan Nama Buku : ") 
    array.append(buku)

print("Urutkan Buku Seperti Apa ? ")
print("1.Asc")  
print("2.Desc")

pilih =  int(input("Pilih : "))

if pilih == 1:
    insertion_asc(array)
elif pilih == 2:
    insertion_desc(array)