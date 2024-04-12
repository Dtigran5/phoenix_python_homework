def diagonal_sum(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0
    diagonal_sum = 0
    for i in range(min(rows, cols)):
        diagonal_sum += matrix[i][i]
    return diagonal_sum

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Diagonal sum of the matrix:", diagonal_sum(matrix))
