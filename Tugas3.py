print ("sebuah program unutk mengihitung bangun datar")
print ("pilih menu angka 1-3 : /n1. persegi/n2. lingkaran/n3.segitiga")
pilihmenu = int(input("silakan pilih menu dengan ketik angka 1-3 : "))

match pilihmenu: 
    case 1:
        print("untuk kamu menghitung luas persegi")
        sisi= int(input("masukan nilai"))
        hitung= sisi*sisi
        print(f"luas persegi : {hitung}")
    case 2:
        print("untuk hitung kamu luas lingkaran")
        Jarijari= int(input("masukkan nilai"))
        hitung= 22/7*Jarijari**2
        print(f"luas lingkaran : {hitung}")
    case 3: 
        print("Untuk kamu hitung luas segitiga")
        luas= int(input("masukkan nilai luas"))
        tinggi= int(input("masukkan nilai tinggi"))
        hitung= 1/2* luas*tinggi
        print(f"luas segitiga : {hitung}")
    case _:
        print("nomer tidak valid, pilih 1-3")