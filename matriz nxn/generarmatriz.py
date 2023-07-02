import numpy as np

print("Bienvenido al generador de matrices")

###             -- Dimensión ingresada --
n = int(input("Escribe un numero: "))
 

###              -- Generar la matriz n*n --

# Rellear la matriz con numero aleatorios de 0 a 9 con la dimension ingresada
m = [np.random.randint(0, 9, n) for i in range(n)]

#matriz = [list(range(1 + n * i, 1 + n * (i + 1)))
    #for i in range(n)]


###               -- Imprimir el resultado --

# Imprimir solo resultado
#print("La matriz creada es: " + str(matriz))

# Imprimir el resultado separado por lineas
#for line in matriz:
    #print('\n'.join(map(str, line)))

# Imprimir matriz separadas por lineas y con espacios por celda
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in m]))


###             --- Sumas de las filas ---

suma_filas = [ ]

for i in range(len(m)):
    contador_filas = 0

    for j in range(len(m[0])):
        contador_filas += m[i][j]

    suma_filas.append(contador_filas)

suma_total_filas = sum(suma_filas)

print("La suma de cada fila es: ", suma_filas)
print("La suma total de las filas es: ", suma_total_filas)


###             --- Sumas de las columnas ---

suma_columnas = [ ]

for j in range(len(m[0])):
    contador_columnas = 0

    for i in range(len(m)):
        contador_columnas += m[i][j]

    suma_columnas.append(contador_columnas)

suma_total_columnas = sum(suma_columnas)

print("La suma de cada columnas es: ", suma_columnas)
print("La suma total de las columnas es: ", suma_total_columnas)
