def even_list(arr):
    new_arr = []
    for i in arr:
        if i % 2 != 0:
            new_arr.append(i)
    return new_arr
arr = [1,2,3,4,5,6]
print(even_list(arr))