def remove(num, index):
    if index < 0 or index >= len(num):
        return num
    new_num = num[:index] + num[index + 1:]
    return new_num

num = [1,2,3,4,5,6]
print(remove(num, 2))