import androidhelper
droid = androidhelper.Android()

n = int(droid.dialogGetInput('n notas?').result)
x = 0
for i in range (n):
  x = x + float(droid.dialogGetInput('nota?').result)
promedio = x/n
print 'El promedio es', promedio