def f(n):
  prod = 1
  for i in range (1, n+1):
    prod *= i
  return prod
def cb (n,k):
  n1 = f (n)
  k2 = f (n-k) * f (k)
  return n1/k2
import androidhelper
droid = androidhelper.Android()
n = int (droid.dialogGetInput ('n:').result)
k = int (droid.dialogGetInput ('k:').result)
print cb (n,k)