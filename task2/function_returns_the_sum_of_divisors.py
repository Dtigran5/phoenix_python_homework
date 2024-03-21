def sum_divisor(*args):
    sum = 0
    for num in args:
        sum += num
    return sum

print(sum_divisor(3,5,7,9))
print(sum_divisor(1,2,3,4,5))
print(sum_divisor(10,20,30))
