datos =[]
for i in range (10):
  datos.append ([i,i+1])
print datos
datos.reverse()
colores = ['azul', 'rojo', 'verde', 'amarillo']
print colores
colores.sort ()
print colores [1:][0][-1]
x = datos + colores
print x
x [0] = 1
print datos