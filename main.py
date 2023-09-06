
def ordenar_fila(matriz, fila):
    fila_a_ordenar = matriz[fila]
    n = len(fila_a_ordenar)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if fila_a_ordenar[j] > fila_a_ordenar[j + 1]:
                fila_a_ordenar[j], fila_a_ordenar[j + 1] = fila_a_ordenar[j + 1], fila_a_ordenar[j]


matriz = [
    [3, 2, 1],
    [6, 5, 4],
    [9, 8, 7]
]


print("Matriz Original:")
for fila in matriz:
    print(fila)


fila_a_ordenar = 0


ordenar_fila(matriz, fila_a_ordenar)


print("\nMatriz con la Fila Ordenada:")
for fila in matriz:
    print(fila)
