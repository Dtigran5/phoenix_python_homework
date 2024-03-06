size = int(input("input size of list: "))
ls = []
for i in range(0, size):
    num = int(input("input numbers of list: "))
    ls.append(num)
min = ls[0]
for j in ls:
    if j < min:
        min = j
print(min)