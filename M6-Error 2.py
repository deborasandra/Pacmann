def menghitung_volume_kubus(r):
    #function ini untuk menghitung volume kubus
    count_volume = r**3
    return count_volume

def menghitung_volume_balok(panjang,lebar,tinggi):
    #function ini untuk menghitung volume balok
    count_volume = panjang*lebar*tinggi
    return count_volume

while True:
    nama_bangun_ruang = input("Masukan Nama Bangun Ruang :")
    valid_nama_bangun_ruang = ["kubus","balok"]
    try:
        if nama_bangun_ruang not in valid_nama_bangun_ruang:
            raise Exception("Nama bangun ruang tidak valid")

        if nama_bangun_ruang == "kubus":
            r = int(input("Masukan nilai rusuk : "))
            print(menghitung_volume_kubus(r))

        elif nama_bangun_ruang == "balok":
            panjang = int(input("Masukan nilai panjang : "))
            lebar = int(input("Masukan nilai lebar : ")) 
            tinggi = int(input("Masukan nilai tinggi : "))
            print(menghitung_volume_balok(panjang, lebar, tinggi))
        break
        
    except Exception as e:
        print(e)