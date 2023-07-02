import numpy as np

print("Bienvenido al generador de matrices")

###             -- Dimensión ingresada --
n = int(input("Escribe un numero: "))
 

###              -- Generar la matriz n*n --

# Rellear la matriz con numero aleatorios de 0 a 9 con la dimension ingresada
m = [np.random.randint(0, 9, n) for j in range(n)]

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
