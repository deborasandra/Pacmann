#CASE 5 - DAFTAR PEGAWAI
print("5 - DAFTAR PEGAWAI")
def daftar_pegawai(**informasi_karyawan) :
    #informasi karyawan adalah sebuah dictionary
    for nama_karyawan, kota_karyawan in informasi_karyawan.items():
        print(f"{nama_karyawan} berasal dari {kota_karyawan}")

daftar_pegawai(Irsyaad = "Bekasi", 
               Chaidar = "Ternate", 
               Dwita = "Bali", 
               Fikria = "Malang", 
               Nurhaliza = "Yogyakarta")