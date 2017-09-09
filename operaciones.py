#Menu
n1 = int(input('Ingresa el primer numero:'))
n2 = int(input('Ingresa el segundo numero:'))

Suma = n1 + n2
Resta = n1 - n2
Producto = n1 * n2

operacion = int(input('¿Que operación quieres realizar? Suma teclea 1, Resta teclea 2, Producto teclea 3'))

if operacion == 1: 
	print('La suma de los numeros es', Suma)
elif operacion == 2:
	print('La resta de los numeros es', Resta)
elif operacion == 3:
	print('El producto de los numeros es', Producto)
else :
	print('No elegiste una opcion valida')
