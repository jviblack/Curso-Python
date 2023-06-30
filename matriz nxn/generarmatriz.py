n = int(input("Escribe un numero: "))
 
# Formar lista
# Crear la matriz n*n
matriz = [list(range(1 + n * i, 1 + n * (i + 1)))
    for i in range(n)]

# Imprimir el resultado
#print("La matriz creada es: " + str(matriz))

# Imprimir el resultado separado por lineas
#for line in matriz:
    #print('\n'.join(map(str, line)))

# Imprimir matriz separadas por lineas y con espacios por celda
print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in matriz]))
