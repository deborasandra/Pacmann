from lingkaran import luas_lingkaran, keliling_lingkaran
from persegi_panjang import luas_persegi_panjang, keliling_persegi_panjang
from segitiga import luas_segitiga, keliling_segitiga


input_user = input("Apa yang ingin dihitung (lingkaran/persegi panjang/segitiga) : ")

if input_user == "lingkaran":
    jari_jari = float(input("Masukkan jari-jari lingkaran : "))
    print(f"Luas lingkaran adalah {luas_lingkaran(jari_jari)}")
    print(f"Keliling lingkaran adalah {keliling_lingkaran(jari_jari)}")

elif input_user == "persegi panjang":
    jenis_persegi_panjang = input("Luas/Keliling : ")
    panjang = float(input("Masukkan panjang : "))
    lebar = float(input("Masukkan lebar : "))
    if jenis_persegi_panjang == "luas":
        print(f"Luas persegi panjang adalah {luas_persegi_panjang(panjang, lebar)}")
    elif jenis_persegi_panjang == "keliling":        
        print(f"Keliling persegi panjang adalah {keliling_persegi_panjang(panjang, lebar)}")

elif input_user == "segitiga":
    jenis_segitiga = input("Luas/Keliling : ")
    if jenis_segitiga == "luas":
        alas = float(input("Masukkan alas : "))
        tinggi = float(input("Masukkan tinggi : "))
        print(f"Luas segitiga adalah {luas_segitiga(alas, tinggi)}")
    elif jenis_segitiga == "keliling":
        sisi1 = float(input("Masukkan sisi 1 : "))
        sisi2 = float(input("Masukkan sisi 2 : "))
        sisi3 = float(input("Masukkan sisi 3 : "))
        print(f"Keliling segitiga adalah {keliling_segitiga(sisi1, sisi2, sisi3)}")
    else:
        print("Input tidak valid")

else:
    print("Input tidak valid")

