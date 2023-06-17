#Bubble Sort

def bubblesort():
    nilai = [3.8,2.9,3.3,4.0,2.7]
    print("Nilai awal: ", nilai)
    for i in range(len(nilai)-1, 0, -1):
        for j in range(i):
            if nilai[j] < nilai[j+1]:
                nilai[j], nilai[j+1]=nilai[j+1], nilai[j]
    print("Nilai akhir: ", nilai)

bubblesort()

