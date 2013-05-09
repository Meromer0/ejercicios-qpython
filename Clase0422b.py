def contar (v, oracion):
  contado = 0
  for i in oracion:
    if i == v:
      contado += 1
  return contado

import androidhelper
droid = androidhelper.Android()
oracion = str (droid.dialogGetInput ('Ingrese oracion:').result)
vocales = 'aeiou'
for i in range(5):
  v = vocales[i]
  c = contar (v, oracion)
  print v, 'aparece', c, 'veces'