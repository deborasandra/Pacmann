#CASE 4 - LAPORAN PENJUALAN
#docstring = digunakan untuk memberi pemahaman, seperti comment
def harga_pokok(beli_bersih, stok_awal, stok_akhir):
  """
  Fungsi untuk menghitung harga pokok penjualan suatu produk.
  Parameter:
      beli_bersih (int) = Pembelian barang baru selama satu tahun.
      stok_awal (int): Persediaan awal barang selama satu tahun
      stok_akhir (int): Persediaan awal barang selama satu tahun.
  Return : hpp (int) : Harga pokok penjualan.
  """
  hpp = beli_bersih + stok_awal - stok_akhir 
  return hpp

harga_pokok = lambda beli_bersih, stok_awal, stok_akhir : beli_bersih + stok_awal - stok_akhir
print(harga_pokok(500_000, 300_000, 200_000))
