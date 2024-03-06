arr = [1, 5, 3, 6, 8, 4, 7, 2, 10, 9]
even = []
odd = []
for num in arr:
    if num % 2 == 0:
        even.append(num)
    else: 
        odd.append(num)
even.sort()
odd.sort(reverse = True)
result = even + odd
print(result)