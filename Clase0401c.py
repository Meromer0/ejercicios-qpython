import androidhelper
droid = androidhelper.Android()

n = int (droid.dialogGetInput ('Ingrese un numero: ').result)
for i in range (1,11):
  print n, 'x', i, '=', n*i
