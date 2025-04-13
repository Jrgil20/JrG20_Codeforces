
def ReduceGrid(n, factor, grid):
    reduce_grid = []
    # Create the reduced grid
    for i in range(0, n, factor):
        for j in range(0, n, factor):
            cell_value = grid[i][j]
            reduce_grid.extend([cell_value])
    return reduce_grid

cases = int(input())

for _ in range(cases):
   # Leer las dimensiones de la matriz
    n, factor = map(int, input().split())  # Ignorar el segundo valor (factor)

    # Inicializar la matriz vacía
    grid = []

    # Leer cada fila y columna  de la matriz
    for _ in range(n):
        row = list(map(int, input().strip()))
        grid.append(row)

    # Imprimir la matriz
    reduce = ReduceGrid(n, factor, grid)
    for row in reduce:
        print(*row)