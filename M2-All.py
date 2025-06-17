""" LATIHAN SOAL
PRIMITIVE DATA STRUCTURE
"""

#1A Menghitung Upah Kotor
print("MENGHITUNG UPAH KOTOR")
upah_perjam = 30_000 # definisikan upah per jam sebagai variabel konstant

#Joko
kary_1 = "Joko" # definisikan nama variabel untuk menampung nama karyawan 1 atau Joko
jam_kerja_kary1 = 44 # definisikan variabel untuk menampung jam kerja karyawan 1
upah_kotor_kary1 = upah_perjam * jam_kerja_kary1 # hitung upah kotor karyawan 1
print(f'Upah Kerja (kotor) {kary_1} = Rp {upah_kotor_kary1:,}') # tampilkan upah kerja (kotor) karyawan 1

# untuk karyawan yang lain, lakukan seperti code di atas
# Alex
kary_2 = "Alex"
jam_kerja_kary2 = 48
upah_kotor_kary2 = upah_perjam * jam_kerja_kary2
print(f'Upah Kerja (kotor) {kary_2} = Rp {upah_kotor_kary2:,}')

# Chandra
kary_3 = "Chandra"
jam_kerja_kary3 = 50
upah_kotor_kary3 = upah_perjam * jam_kerja_kary3
print(f'Upah Kerja (kotor) {kary_3} = Rp {upah_kotor_kary3:,}')

# Hartono
kary_4 = "Hartono"
jam_kerja_kary4 = 42
upah_kotor_kary4 = upah_perjam * jam_kerja_kary4
print(f'Upah Kerja (kotor) {kary_4} = Rp {upah_kotor_kary4:,}')

# Samsul
kary_5 = "Samsul"
jam_kerja_kary5 = 45
upah_kotor_kary5 = upah_perjam * jam_kerja_kary5
print(f'Upah Kerja (kotor) {kary_5} = Rp {upah_kotor_kary5:,}')

print()

#1B Menghitung Upah Lembur
upah_lembur_perjam = 35_000 #Upah lembur per jam
#Jam Lembur Karyawan
jam_lembur_kary1 = 12
jam_lembur_kary2 = 11
jam_lembur_kary3 = 10
jam_lembur_kary4 = 15
jam_lembur_kary5 = 12
#Upah Lembur Karyawan
upah_lembur_kary1 = upah_lembur_perjam * jam_lembur_kary1
upah_lembur_kary2 = upah_lembur_perjam * jam_lembur_kary2
upah_lembur_kary3 = upah_lembur_perjam * jam_lembur_kary3
upah_lembur_kary4 = upah_lembur_perjam * jam_lembur_kary4
upah_lembur_kary5 = upah_lembur_perjam * jam_lembur_kary5
#Print hasil
print("MENGHITUNG UPAH LEMBUR")
print(f'Upah Lembur {kary_1} = Rp {upah_lembur_kary1:,}')
print(f'Upah Lembur {kary_2} = Rp {upah_lembur_kary2:,}')
print(f'Upah Lembur {kary_3} = Rp {upah_lembur_kary3:,}')
print(f'Upah Lembur {kary_4} = Rp {upah_lembur_kary4:,}')
print(f'Upah Lembur {kary_5} = Rp {upah_lembur_kary5:,}')

print()

#1C MENGHITUNG TOTAL UPAH
#Total Upah
upah_total_kary1 = upah_kotor_kary1 + upah_lembur_kary1
upah_total_kary2 = upah_kotor_kary2 + upah_lembur_kary2
upah_total_kary3 = upah_kotor_kary3 + upah_lembur_kary3
upah_total_kary4 = upah_kotor_kary4 + upah_lembur_kary4
upah_total_kary5 = upah_kotor_kary5 + upah_lembur_kary5
#Print hasil
print("MENGHITUNG TOTAL UPAH")
print(f'Total Upah {kary_1} = Rp {upah_total_kary1:,}')
print(f'Total Upah {kary_2} = Rp {upah_total_kary2:,}')
print(f'Total Upah {kary_3} = Rp {upah_total_kary3:,}')
print(f'Total Upah {kary_4} = Rp {upah_total_kary4:,}')
print(f'Total Upah {kary_5} = Rp {upah_total_kary5:,}')

print()

#1D MENGHITUNG PAJAK
#Persentase pajak
persen_pajak = 5/100
#Pajak Karyawan
pajak_kary1 = upah_total_kary1 * persen_pajak
pajak_kary2 = upah_total_kary2 * persen_pajak
pajak_kary3 = upah_total_kary3 * persen_pajak
pajak_kary4 = upah_total_kary4 * persen_pajak
pajak_kary5 = upah_total_kary5 * persen_pajak
#Print hasil
print("MENGHITUNG BESAR PAJAK KARYAWAN")
print(f'Total Pajak {kary_1} = Rp {pajak_kary1:,}')
print(f'Total Pajak {kary_2} = Rp {pajak_kary2:,}')
print(f'Total Pajak {kary_3} = Rp {pajak_kary3:,}')
print(f'Total Pajak {kary_4} = Rp {pajak_kary4:,}')
print(f'Total Pajak {kary_5} = Rp {pajak_kary5:,}')

print()

#1E MENGHITUNG TOTAL UPAH (NETTO) SETELAH PAJAK
upah_nett_kary1 = upah_total_kary1 - pajak_kary1
upah_nett_kary2 = upah_total_kary2 - pajak_kary2
upah_nett_kary3 = upah_total_kary3 - pajak_kary3
upah_nett_kary4 = upah_total_kary4 - pajak_kary4
upah_nett_kary5 = upah_total_kary5 - pajak_kary5
#Print hasil
print("MENGHITUNG TOTAL UPAH (NETTO) / SETELAH PAJAK KARYAWAN")
print(f'Total Upah (Netto) {kary_1} = Rp {upah_nett_kary1:,}')
print(f'Total Upah (Netto) {kary_2} = Rp {upah_nett_kary2:,}')
print(f'Total Upah (Netto) {kary_3} = Rp {upah_nett_kary3:,}')
print(f'Total Upah (Netto) {kary_4} = Rp {upah_nett_kary4:,}')
print(f'Total Upah (Netto) {kary_5} = Rp {upah_nett_kary5:,}')

print()

#1F MENGHITUNG TOTAL UPAH SELURUH KARYAWAN PERUSAHAAN B
total_upah_kary_all = upah_nett_kary1 + upah_nett_kary2 + upah_nett_kary3 + upah_nett_kary4 + upah_nett_kary5
print(f'Jumlah total upah karyawan perusahaan B adalah = Rp {total_upah_kary_all:,}')

#1G MENGHITUNG RATA RATA UPAH KARYAWAN
jml_kary = 5
rata_rata_upah = total_upah_kary_all / jml_kary
print(f'Rata - rata upah karyawan Perusahaan B adalah = Rp {rata_rata_upah:,}')

print()

#2A MENGHITUNG PAJAK MOBIL TAHUN PERTAMA
harga_jual = 200_000_000
bbnkb = (10/100) * harga_jual
pkb = (2/100) * harga_jual
swdkllj = 143_000
tnkb = 100_000
penerbitan_stnk = 200_000
biaya_admin = 50_000
pajak_tahun_pertama = bbnkb + pkb + swdkllj + tnkb + penerbitan_stnk + biaya_admin
#Print Hasil
print(f'Pajak Tahun Pertama mobil Pak Samsul = Rp {pajak_tahun_pertama:,}')