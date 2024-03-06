N = int(input("Enter size: "))
matrix = []
for i in range(N):
    row = []
    for j in range(N):
        row.append(i + j)
    matrix.append(row)

if N >= 4:
    for row in matrix:
        print(row[0], row[2])
else:
    print("N is too small")