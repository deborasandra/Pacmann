#FUNCTION#
"""
def pelanggan(*nama):
    print("Pelanggan toko hari ini :")
    return nama
pelanggan_ouput = pelanggan("Pacmann","Academy","Rafi")
print(pelanggan_ouput)
"""

#CASE 1 - PENGHASILAN PEGAWAI
print("1B - JUMLAH PENGHASILAN PEGAWAI")
def penghasilan_pegawai():
    kategori = input("Kategori Pegawai (Tetap/Kontrak) : ")
    jam_lembur = int(input("Jam Lembur : "))
    penghasilan_tetap = 4_500_000

    if kategori == "tetap":
        penghasilan_utama = penghasilan_tetap
        penghasilan_lembur_perjam = 50_000
    elif kategori == "kontrak" :
        penghasilan_utama = 0.7 * penghasilan_tetap
        penghasilan_lembur_perjam = 30_000
    else:
        #tidak termasuk tetap / kontrak, maka kasih tau user input error
        pesan_error = "Kategori yang diterima tidak dapat diproses, masukkan kategori 'tetap' atau 'kontrak'"
        return pesan_error

    if jam_lembur > 20:
        jam_lembur = 20
    elif jam_lembur < 0:
        pesan_error = "Jam lembur tidak boleh negatif"
        return pesan_error

    penghasilan_lembur = penghasilan_lembur_perjam * jam_lembur
    penghasilan_total = penghasilan_utama + (penghasilan_lembur)
    pajak = int(0.01 * penghasilan_total)
    penghasilan_nett = penghasilan_total- pajak
    
    print(f"Penghasilan lembur = Rp. {penghasilan_lembur:,}")
    print(f"Penghasilan total = Rp. {penghasilan_total:,}")
    print(f"Besar Pajak = Rp. {pajak:,}")
    print(f"Penghasilan Nett = Rp. {penghasilan_nett:,}")
    return penghasilan_lembur, penghasilan_total, pajak, penghasilan_nett
penghasilan_pegawai()