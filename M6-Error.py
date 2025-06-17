'''#2A
def menghitung_pajak():
  while True:
        penghasilan = int(input( "Masukan Penghasilan Anda : " ))
        print(f"{penghasilan} / potongan pajak 5% = {penghasilan/0.5}")
        break
  
menghitung_pajak()


#2B
def menghitung_pajak():
  pajak = 0.05
  
  while True:
    try:
        penghasilan = int(input( "Masukan Penghasilan Anda : " ))
        biaya_pajak = penghasilan * pajak
        total_akhir = penghasilan - biaya_pajak
        print(f"Pajak yang harus dibayar adalah {biaya_pajak}, sehingga total akhir penghasilan adalah {total_akhir}")
        break
    except:
        print("Terjadi Exception")
  
menghitung_pajak()
'''

#2C
def menghitung_pajak():
  pajak = 0.05
  
  while True:
    try:
        penghasilan = int(input( "Masukan Penghasilan Anda : " ))
        
        if penghasilan < 0:
           raise Exception("Penghasilan harus bilangan positif")

        biaya_pajak = penghasilan * pajak
        total_akhir = penghasilan - biaya_pajak
        print(f"Pajak yang harus dibayar adalah {biaya_pajak}, sehingga total akhir penghasilan adalah {total_akhir}")
        break

    except ValueError:
        print("Nilai bukan data integer, masukkan kembali input Anda!")
    
    except Exception as e:
       print(e)

menghitung_pajak()

'''
#3
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
'''