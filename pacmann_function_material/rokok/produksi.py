def profit(info):
  """
  Menghitung keuntungan penjualan
  parameter:
    info (dict): dictionary yang berisi data produksi
  return:
    profit (int): keuntungan penjualan
  """
  total_sales = info['jumlah_produk']*info['harga_jual']
  total_cost = info['jumlah_produk']*info['biaya_produksi']
  profit = total_sales-total_cost
  return profit


def harga_pokok(info):
  """
  Menghitung harga pokok penjualan
  parameter:
    info (dict): dictionary yang berisi data produksi
  return:
    total (int): harga pokok penjualan
  """
  total = info['biaya_produksi'] +info['jumlah_produk'] - info['persediaan_sisa']
  return total