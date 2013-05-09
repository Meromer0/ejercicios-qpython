def es_divisible (n,d):
  return n%d == 0
def es_primo (n):
  for i in range(2,n):
    if es_divisible(n,i):
      return False
  return True
def iesimo_primo (n):
  for i in range (1,n+1):
    if es_primo(i):
      print i,'es primo'

import androidhelper
droid = androidhelper.Android()
n = int (droid.dialogGetInput ('Ingrese n:').result)
iesimo_primo(n)