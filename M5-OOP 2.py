#1A & 1B
# buat kelas Jets
class Jets:
    def __init__(self, asal, nama):
        self.asal = asal
        self.nama = nama
    # buat atribut asal dan nama
    ...

#BISA LANGSUNG TANPA CHILD CLASS
# buat child class A7S37 dan inherit dari parent class Jets
class A7S37(Jets):
    pass

# buat child class IDN17 dan inherit dari parent class Jets
class IDN17(Jets):
    pass

# buatlah instance untuk menampung kelas
jets_1 = A7S37("Swedia","AJS37")
jets_2 = IDN17("Indonesia","IDN17")

# tampilkan hasil program
print(jets_1.asal)
print(jets_1.nama)
print(jets_2.asal)
print(jets_2.nama)

#2A & 2B
#buat class Kendaraan
class Kendaraan:
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas

#buat class child Mikrolet
class Mikrolet(Kendaraan):
    tarif = 2000

    # buatlah method untuk mencari keuntungan
    def hitung_untung(self):
        return self.tarif * self.kapasitas

#buat class child Bus
class Bus(Kendaraan):
    tarif = 5000
    def hitung_untung(self):
        kotor = self.tarif * self.kapasitas
        bersih = kotor + (0.1*kotor)
        return bersih
        
#buatlah instance
kendaraan_1 = Mikrolet(10)
kendaraan_2 = Bus(30)
print(kendaraan_1.hitung_untung())
print(kendaraan_2.hitung_untung())

#3A & 3B
# buat kelas Person
class Person:
    # buatlah attribute yang terdapat parameter nama dan umur
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    # buat method display untuk class Person
    def display(self):
        print(f"Person Nama : {self.nama}")
        print(f"Person Umur : {self.umur}")

# buat child class Student dari class Person
class Student(Person):
    # definisikan attribute dari parent class dan buat attribute baru peminatan
    def __init__(self,nama,umur,peminatan):
        super().__init__(nama,umur)
        self.peminatan = peminatan

    # buat method display untuk class Student
    def display_student(self):
        print(f"Nama Student : {self.nama}")
        print(f"Umur Student : {self.umur}")
        print(f"Peminatan Student : {self.peminatan}")

     # buat method filter_umur sesuai dengan ketentuan soal
    def filter_umur(self):
        if self.umur >= 18 and self.umur <= 24:
            kategori = "Muda"
        elif self.umur >=25 and self.umur <= 45:
            kategori = "Produktif"
        else:
            kategori = "Lanjut Usia"
        print(f"{self.nama} masuk ke dalam kategori grup {kategori}")
        return kategori
        
# uji Person class
person_1 = Person("Tomas Wild",37)
person_1.display()
print("----------------------------------------")
student_1 = Student("Albert",23,"Mathematics")
student_1.display_student()
student_1.filter_umur()
student_2 = Student("Jonathan", 46 , "Science")
student_2.display_student()
student_2.filter_umur()
student_3 = Student("Ronald", 25 , "Law")
student_3.display_student()
student_3.filter_umur()