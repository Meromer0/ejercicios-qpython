import androidhelper
droid = androidhelper.Android()

n = droid.dialogGetInput ('Ingrese un numero: ').result
t = True
for i in range (len (n)):
  
  if n[i]!=n [-(i+1)]:
    print 'No es palindromo'
    t = False
    break
if t:
  print 'Es palindromo'

