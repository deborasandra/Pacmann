import perhitungan_angsuran_per_bulan_klien as perhitungan_bunga

pinjaman = int(input("Masukkan besaran biaya yang dipinjam : "))
bunga = float(input("Masukkan suku bunga : "))

print(perhitungan_bunga.bunga_flat(pinjaman, bunga))