def probabilidad_tsunami(mareas,umbral):
  total = 0
  for a in mareas:
    if a >= umbral:
      total +=1
  return total/len(mareas) * 100

def hay_que_evacuar(mareas):
  if probabilidad_tsunami(mareas,270.0) > 32.0:
    return True
  return False