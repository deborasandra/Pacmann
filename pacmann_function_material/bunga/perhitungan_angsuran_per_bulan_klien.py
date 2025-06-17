def bunga_flat(pinjaman, bunga) :
    bulan = 12
    pokok_pinjaman = pinjaman / bulan
    bunga_pertahun = pinjaman * bunga
    bunga_perbulan = bunga_pertahun / bulan
    total_angsuran = int(pokok_pinjaman + bunga_perbulan)
    return total_angsuran