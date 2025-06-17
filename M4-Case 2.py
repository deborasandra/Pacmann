#CASE 2 - PERHITUNGAN RATIO
print("2 - PERHITUNGAN RATIO")
list1 = [10, 8, 6, 4, 2, 0, -2, -4] #membuat list
print(f"List Angka : {list1}")
def perhitungan_ratio(list_input) :
    banyaknya_positif = 0
    banyaknya_negatif = 0
    banyaknya_nol = 0

    for angka in list_input:
        if angka > 0:
            banyaknya_positif += 1
        elif angka == 0 :
            banyaknya_nol += 1
        elif angka < 0 :
            banyaknya_negatif += 1
    
    banyaknya_angka = len(list_input)
    rasio_positif = banyaknya_positif / banyaknya_angka
    rasio_negatif = banyaknya_negatif / banyaknya_angka
    rasio_nol = banyaknya_nol / banyaknya_angka

    print(f"Rasio bilangan positif adalah {rasio_positif:.3f}")
    print(f"Rasio bilangan negatif adalah {rasio_negatif:.3f}")
    print(f"Rasio bilangan nol adalah {rasio_nol:.3f}")

    return rasio_positif, rasio_negatif, rasio_nol

perhitungan_ratio(list1)