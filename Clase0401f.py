for i in range (1,11):
  for j in range (1,11):
    result = str(i*j)
    if len (result)==1:
      print ' ', result,
    elif len (result)==2:
      print '', result,
    else:
      print result,
  print '\n',
print 'Los numeros estan alineados a la derecha'