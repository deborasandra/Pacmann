import produksi

#Dictionary
data = {
  "biaya_produksi": 35000,
  "harga_jual": 50000,
  "jumlah_produk": 1200,
  "persediaan_sisa" : 100
}

print(f'Keuntungan penjualan adalah : {produksi.profit(data)}')
print(f'Harga pokok penjualan adalah : {produksi.harga_pokok(data)}')