import numpy as np

print("Bienvenido al generador de matrices")

###             -- Dimensión ingresada --
filas = int(input("Escribe un numero: "))
columnas = filas 

###              -- Generar la matriz n*n --

# Rellear la matriz con numero aleatorios de 0 a 9 con la dimension ingresada
m = [np.random.randint(0, 9, filas) for i in range(filas)]

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




for i in range(filas):
    m.append([])
    for j in range(columnas):
        valor = filas
 
sumaFila=[sum(i) for i in m]
print (sumaFila)
 
s
