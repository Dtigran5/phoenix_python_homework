def find_unique_element(arr):
    unique_element = 0
    for num in arr:
        unique_element ^= num
    return unique_element

arr = [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
print("The unique number is:", find_unique_element(arr))
