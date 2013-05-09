import androidhelper

droid = androidhelper.Android()
f = float(droid.dialogGetInput('temp en f: ').result)
c = (f-32.0) * (5.0/9.0)
print('El equivalente en C es: ', c)