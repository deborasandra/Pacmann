def beban_usaha(operasional, non_operasional) :
  result = operasional - non_operasional
  return result

def laba_bersih(laba_kotor, operasional, non_operasional) :
  result = laba_kotor - (operasional + non_operasional)
  return result