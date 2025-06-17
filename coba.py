def penghasilan_pegawai():
  kategori = input("Kategori Pegawai (Tetap/Kontrak) : ")
  lembur = input("Berapa jam lembur : ")
  jam_lembur = float(lembur)

  GAJI_TETAP = 4500000
  GAJI_KONTRAK = 0.7 * 4500000

  if (kategori == "Tetap" or kategori == "tetap") :
      if (jam_lembur >= 0 and jam_lembur <=20 ):
          gaji_lembur = jam_lembur * 50000
          print("\nTotal gaji lembur : Rp.", int(gaji_lembur))
          pendapatan = GAJI_TETAP + gaji_lembur
          print("Pendapatan : Rp.", int(pendapatan))

      elif (jam_lembur > 20 ) :
          gaji_lembur = 20 * 50000
          print("\nTotal gaji lembur : Rp.", int(gaji_lembur))

          pendapatan = GAJI_TETAP + gaji_lembur
          print("Pendapatan : Rp.", pendapatan)

      else :
          print("Jam Lembur tidak boleh bernilai negatif")

  elif (kategori == "Kontrak" or kategori == "kontrak")  :
      if (jam_lembur >= 0 and jam_lembur <=20):
          gaji_lembur = jam_lembur * 30000
          print("Total gaji lembur : Rp.", int(gaji_lembur))
          pendapatan = GAJI_KONTRAK + gaji_lembur
          print("Pendapatan : Rp.", pendapatan )

      elif (jam_lembur > 20 ) :
          gaji_lembur = 20 * 30000
          print("\nTotal gaji lembur : Rp.", int(gaji_lembur))
          pendapatan = GAJI_KONTRAK + gaji_lembur
          print("Pendapatan : Rp.", pendapatan)

      else :
          print("Jam Lembur tidak boleh bernilai negatif")
penghasilan_pegawai()

