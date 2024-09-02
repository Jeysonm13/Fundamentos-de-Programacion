def crear_matriz():
    # Crear una matriz 3x3 con valores numéricos
    matriz = [
        [9, 7, 5],
        [8, 3, 2],
        [6, 1, 4]
    ]
    return matriz

def bubble_sort_fila(fila):
    # Implementar Bubble Sort para ordenar una fila en orden ascendente
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]
    return fila

# Crear la matriz
matriz = crear_matriz()

# Fila que deseas ordenar (por ejemplo, la fila 1)
fila_a_ordenar = 1

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenar la fila específica
matriz[fila_a_ordenar] = bubble_sort_fila(matriz[fila_a_ordenar])

# Mostrar la matriz con la fila ordenada
print("\nMatriz con la fila 1 ordenada:")
for fila in matriz:
    print(fila)
