def rotate_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    rotated_matrix = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            rotated_matrix[j][n-1-i] = matrix[i][j]
    return rotated_matrix


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

rotated_matrix = rotate_matrix(matrix)

for row in rotated_matrix:
    print(' '.join(map(str, row)))
