size = int(input("input size of list: "))
ls = []
for i in range(0, size):
    num = int(input("input numbers of list: "))
    ls.append(num)
min = ls[0]
for j in ls:
    if j < min:
        min = j
print("This is the minimum: ",min)
max = ls[0]
for k in ls:
    if k > max:
        max = k
print("This is the maximum: ", max)
sum = max + min
print("This is the sum of maximum and minimum: ", sum)