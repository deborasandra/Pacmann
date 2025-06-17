#CASE 3 - PERHITUNGAN PRODUK DIBELI SETELAH DISKON
def harga_promo(*harga): #*Arbitrary Arguments (*args)
    pembayaran = sum(harga)
    total_diskon = pembayaran * 0.40
    total_bayar = int(pembayaran - total_diskon)
    return total_bayar
total = harga_promo(200_000, 300_000, 400_000, 500_000, 600_000, 700_000)
print(f"Harga akhir yang dibayarkan : Rp {total:,}")