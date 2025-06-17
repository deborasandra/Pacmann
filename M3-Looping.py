#CASE 1 
#MENENTUKAN JADWAL BEKAL
list_bekal = ["Nasi + Telur","Nasi + Ikan","Nasi + Tahu dan Tempe"]

index = 0
for tanggal in range(1,31):
    
    if tanggal % 7 == 0:
        print(f"Tanggal {tanggal} libur")
        continue

    print(f"Tanggal {tanggal} Bekal {list_bekal[index]}")

    index += 1
    if index > 2:
        index = 0