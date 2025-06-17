"""
#1A
#buat kelas Mobil
class Mobil:
    #Atribut Class
    bunyi = "ngengg"

    #berikan atribut instance kecepatan dan jarak
    def __init__ (self, kecepatan, jarak):
        self.kecepatan = kecepatan
        self.jarak = jarak

avanza = Mobil(240,18)
print(avanza.kecepatan, avanza.jarak)
print(avanza.bunyi)

#1B
#buat kelas Motor
class Motor:
    def __init__(self, kecepatan, jarak, warna):
        self.kecepatan = kecepatan
        self.jarak = jarak
        self.warna = warna

#berikan atribut instance kecepatan, jarak, dan warna
vario = Motor(100, 100, "Merah")
beat = Motor(90,90,"putih")

#1C
#buat kelas Skuter tanpa variabel dan method
class Skuter:
    roda = 2 #misal jika ditambahkan variabel/object kelas

skuter_A = Skuter()
print(skuter_A.roda)

#2A
#buat class Belanja
class Belanja:
    roti = 3
    soda = 5
    selai = 2
    
    #gaperlu __init__
    #def __init__(self):
        #pass

    #buat method jumlah_belanja dengan output nama barang dan jumlah barang berdasarkan
    #attribute kelas
    def jumlah_belanja():
        return f"Jumlah Belanja : Roti = {Belanja.roti}, Soda = {Belanja.soda}, Selai = {Belanja.selai}"

##Proses pemanggilan fungsi
keranjang_a.jumlah_belanja()

#2B
#buat class AlatTulis
class AlatTulis:
    pensil = 2000
    pulpen = 3000
    penghapus = 1000
    
    def __init__(self):
        pass

    #buat method TotalHarga dengan output nama dan harga
    def total_harga(self):
        return f"Daftar Harga: Pensil = {AlatTulis.pensil}, Pulpen = {AlatTulis.pulpen}, Penghapus = {AlatTulis.penghapus}"
        

##Proses pemanggilan fungsi
user2 = AlatTulis()
user2.total_harga()

#3A
#BUAT KELAS PEKERJA
class Pekerja:
    def __init__(self,nama_depan,nama_belakang):
        self.nama_depan = nama_depan
        self.nama_belakang = nama_belakang
        self.nama_lengkap = nama_depan + nama_belakang
        self.email = nama_depan + "." + nama_belakang + "@company.com"
        
# buatlah instance dan panggil attribute nya
pekerja_1 = Pekerja("Debora","Sandra")
print(pekerja_1.nama_depan)
print(pekerja_1.nama_belakang)
print(pekerja_1.nama_lengkap)
print(pekerja_1.email)

#3B ???

#4A
#buat class BankAccount
class BankAccount:
    # buat attribute dengan parameter: nomor_rekening, nama, dan saldo
    def __init__(self, nomor_rekening, nama, saldo):
        self.nomor_rekening = nomor_rekening
        self.nama = nama
        self.saldo = saldo

     # buat method display()
    def display(self):
        print(f"Nomor Akun : {self.nomor_rekening}")
        print(f"Nama Akun : {self.nama}")
        print(f"Saldo : Rp. {self.saldo}")
        
# buatlah instance dan panggil attribute nya
akun_1 = BankAccount(2178514584,"Bambang",5000000)
akun_1.display()

#4B
#buat class BankAccount
class BankAccount:
    # buat attribute dengan parameter: nomor_rekening, nama, dan saldo
    def __init__(self, nomor_rekening, nama, saldo):
        self.nomor_rekening = nomor_rekening
        self.nama = nama
        self.saldo = saldo

    # buat method setor tunai
    def setor_tunai(self,saldo_masuk):
        self.saldo += saldo_masuk
    
    # buat method display()
    def display(self):
        print(f"Nomor Akun : {self.nomor_rekening}")
        print(f"Nama Akun : {self.nama}")
        print(f"Saldo : Rp. {self.saldo}")

# buatlah instance dan panggil attribute nya
akun_1 = BankAccount(2178514584,"Bambang",5000000)
akun_1.setor_tunai(20000)
akun_1.display()

#4C
#buat class BankAccount
class BankAccount:
    # buat attribute dengan parameter: nomor_rekening, nama, dan saldo
    def __init__(self, nomor_rekening, nama, saldo):
        self.nomor_rekening = nomor_rekening
        self.nama = nama
        self.saldo = saldo

    # buat method setor tunai
    def setor_tunai(self,saldo_masuk):
        self.saldo += saldo_masuk

    # buat method tarik tunai
    def tarik_tunai(self,saldo_keluar):
        self.saldo -= saldo_keluar
    
    # buat method display()
    def display(self):
        print(f"Nomor Akun : {self.nomor_rekening}")
        print(f"Nama Akun : {self.nama}")
        print(f"Saldo : Rp. {self.saldo}")

# buatlah instance dan panggil attribute nya
akun_1 = BankAccount(2178514584,"Bambang",5000000)
akun_1.setor_tunai(20000)
akun_1.tarik_tunai(500000)
akun_1.setor_tunai(1000000)
akun_1.display()

"""

#buat class BankAccount
class BankAccount:
    # buat attribute dengan parameter: nomor_rekening, nama, dan saldo
    def __init__(self, nomor_rekening, nama, saldo):
        self.nomor_rekening = nomor_rekening
        self.nama = nama
        self.saldo = saldo

    # buat method setor tunai
    def setor_tunai(self, saldo_masuk):
        self.saldo += saldo_masuk

     # buat method display()
    def display(self):
        print(f"Nomor Akun : {self.nomor_rekening}")
        print(f"Nama Akun : {self.nama}")
        print(f"Saldo : Rp. {self.saldo}")

# buatlah instance dan panggil attribute nya
akun_1 = BankAccount(2178514584,"Bambang",5000000)
akun_1.setor_tunai(20000)
akun_1.display()