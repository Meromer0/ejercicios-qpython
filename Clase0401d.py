import androidhelper
droid = androidhelper.Android()

n = int (droid.dialogGetInput ('Ingrese un numero: ').result)
for i in range (n+1):
  print 2 ** i,
