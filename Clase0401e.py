import androidhelper
droid = androidhelper.Android()

n = int (droid.dialogGetInput ('Ingrese un numero: ').result)
a = int (droid.dialogGetInput ('Ingrese un numero: ').result)
x = 0
for i in range (n+1,a):
  x += i
print 'La suma es', x