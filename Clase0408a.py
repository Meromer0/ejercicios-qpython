import androidhelper
droid = androidhelper.Android()

m = droid.dialogGetInput ('Ingrese oracion: ').result
n = 1
t = True
for i in range (len (m)):
  while m[-(i+n)] == ' ':
    n +=1
  if m [i] == ' ':
    n -= 1
  elif m[i]!= m[-(i+n)]:
    print 'No es palindromo'
    t = False
    break
if t:
  print 'Es palindromo'

