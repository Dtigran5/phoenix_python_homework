N = int(input("Enter size: "))
matrix = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(i + j)
    matrix.append(row)
if N >= 4:
    max_sum = 0
    min_sum = float('inf')
    for i in range(N):
        row_sum = 0
        for j in range(N):
            row_sum +=matrix[i][j]
        if i == 0 and i == 3:
            max_sum += row_sum
            min_sum += row_sum
        else:
            if row_sum + sum(matrix[i-3]) > max_sum:
                max_sum = row_sum + sum(matrix[i-3])
            if row_sum + sum(matrix[i-3]) < min_sum:
                min_sum = row_sum + sum(matrix[i-3])
    print(max_sum, min_sum)
else :
    prin("N is too small")
