def crear_matriz():
    # Crear una matriz 3x3 con valores numéricos
    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    return matriz

def buscar_valor(matriz, valor_buscado):
    # Recorrer la matriz para encontrar el valor específico
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor_buscado:
                return (i, j)  # Devuelve la posición (fila, columna) si encuentra el valor
    return None  # Devuelve None si el valor no se encuentra en la matriz

# Crear la matriz
matriz = crear_matriz()

# Definir el valor que deseas buscar
valor_buscado = 5

# Buscar el valor en la matriz
posicion = buscar_valor(matriz, valor_buscado)

if posicion:
    print(f"El valor {valor_buscado} se encuentra en la posición {posicion}.")
else:
    print(f"El valor {valor_buscado} no se encuentra en la matriz.")
