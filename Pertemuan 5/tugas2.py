array = []

jumlah  = int(input("Masukkan Jumlah Mata Kuliah : ")) 


for i in range(jumlah):
    nilai = float(input("Masukkan nilai mata kuliah ke-{} : ".format(i)))
    array.append(nilai)

ratarata = sum(array)/jumlah

print()
if ratarata < 100  and ratarata  >= 90 :
    print('Hasil Predikat A dengan nilai : ')
elif ratarata < 90 and ratarata >= 70 :
    print('Hasil Predikat B dengan nilai : ')
elif ratarata < 70 and ratarata >= 50 :
    print('Hasil Predikat C dengan nilai : ')
elif ratarata < 50 and ratarata >= 30 :
    print('Hasil Predikat D dengan nilai : ')
elif ratarata < 30 and ratarata >= 0 :
    ('Hasil Predikat E dengan nilai : ')
else:
    print('Nilai tidak valid !')


for x in range(jumlah):
        
       print(f"Mata kuliah ke-{x} : " ,(array[x]))

