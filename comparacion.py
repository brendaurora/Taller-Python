#comparacion
x = int(input('Teclea tu calificacion: '))
y = int(input('Teclea tu calificacion anterior: '))

if x < y:
    print('Bajaste tu rendimiento')
elif x == y:
    print('Tu rendimiento es el mismo')
else:
    print('Felicidades, mejoraste tu rendimiento')
