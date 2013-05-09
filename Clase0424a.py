def fact_recip (n):
  prod = 1
  for i in range(2,n+1):
    prod *= i
  return 1/prod

def signo (n):
  return (-1)**n+1

def sen_aprox (x,m):
  if m > 1:
    e = 2*m-1
    return x**(e)*signo(m)*fact_recip(e)+sen_aprox(x,m-1)
  return 1