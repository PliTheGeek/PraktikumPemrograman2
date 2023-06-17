#Menggunakan Function

def funcganjilgenap(n):
    
    if (n %2 == 0):
        print("n adalah bilangan genap")
    else:
        print("n adalah bil ganjil")
    
    return n

bil = int(input("Masukkan Bilangan : "))

funcganjilgenap(bil)

#Menggunakan Procedure

def ganjilgenap(n):
    
    if (n %2 == 0):
        print("n adalah bilangan genap")
    else:
        print("n adalah bil ganjil")
    
    

bil = int(input("Masukkan Bilangan : "))

ganjilgenap(bil)