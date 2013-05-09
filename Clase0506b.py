def calcular_puntaje(anotaciones):
  total = 0
  for punto in puntos:
    if punto == 'L':
      total +=1
    elif punto == 'D':
      total +=2
    elif punto == 'T':
      total +=3
  return total

def ganador_partido (anotaciones_a,anotaciones_b):
  if calcular_puntaje(anotaciones_a) > calcular_puntaje(anotaciones_b):
    return 'A'
  elif calcular_puntaje(anotaciones_b) > calcular_puntaje(anotaciones_a):
    return 'B'
  return 'Empate'