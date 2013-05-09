import androidhelper
droid = androidhelper.Android ()

n1 ='nota 1: '
n2 = 'nota 2: '
n3 = 'nota 3: '
x = int (droid.dialogGetInput(n1).result)
y = int (droid.dialogGetInput(n2).result)
z = int (droid.dialogGetInput(n3).result)

mn = int (round ((x+y+z)/3.0))

print 'Su promedio', mn, 'es'
if mn < 30:
  print 'triste'
elif mn < 45:
  print 'insuficiente'
elif mn < 55:
  print 'mediocre'
else:
 print 'pasable'
