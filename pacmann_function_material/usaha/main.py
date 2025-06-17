import usaha

operasional = int(input("Masukkan biaya operasional : "))
non_operasional = int(input("Masukkan biaya non operasional : "))

print(f"Beban usaha yang dikeluarkan adalah : {usaha.beban_usaha(operasional, non_operasional)}")

operasional = int(input("Masukkan biaya operasional : "))
non_operasional = int(input("Masukkan biaya non operasional : "))
laba_kotor = int(input("Masukkan laba kotor : "))

print(f"Laba bersih yang dihasilkan adalah : {usaha.laba_bersih(laba_kotor, operasional, non_operasional)}")









