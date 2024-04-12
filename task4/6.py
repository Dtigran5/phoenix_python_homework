def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]


arr = [64, 25, 12, 22, 11]

bubble_sort_arr = arr.copy()
bubble_sort(bubble_sort_arr)
print("Bubble Sort:", bubble_sort_arr)

selection_sort_arr = arr.copy()
selection_sort(selection_sort_arr)
print("Selection Sort:", selection_sort_arr)
