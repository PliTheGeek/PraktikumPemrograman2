def luaskelilingjarijari(r):
    phi = 3.14
    
    luas = (phi*r*r)
    keliling = (phi*2*r)

    print("Luas Lingkaran Adalah",luas)
    print("Keliling Lingkaran Adalah",keliling)
    return luas,keliling

jari = int(input("Masukkan Jari Jari Lingkaran : "))
luaskelilingjarijari(jari)