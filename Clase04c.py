import androidhelper
droid = androidhelper.Android ()

n1 ='ingrese un palabra 1: '
n2 ='ingrese una palabra 2: '
x = str (droid.dialogGetInput(n1).result)
y = str (droid.dialogGetInput(n2).result)

print x, 'y', y,
if (len (x) < 4 and len (y) < 4):
  print 'no tienen el mismo largo'
elif (x [-4:] == y [-4:]):
  print 'riman'
else:
  print 'no riman'