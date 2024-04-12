def anti_diagonal_sum(matrix):
    n = len(matrix)
    diagonal_sum = 0
    for i in range(n):
        diagonal_sum += matrix[i][n - 1 - i]
    return diagonal_sum

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Sum of anti-diagonal elements:", anti_diagonal_sum(matrix))
