import androidhelper
droid = androidhelper.Android ()

n1 ='ingrese un anno'
n2 ='bisiesto'
x = int (droid.dialogGetInput(n1).result)

print x, 'es un anno',
if (x%4 == 0):
  if (x%100 ==0 and x%400 !=0):
    print 'no', n2
  else:
    print n2
else:
  print 'no', n2