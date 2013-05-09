import androidhelper
droid = androidhelper.Android ()

x = float (droid.dialogGetInput('say wut?').result)
y = 3.0/2.0 * x - 3* int (x/2)
print 'y =', y