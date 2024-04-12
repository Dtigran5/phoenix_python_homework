l = [1,1,2,2,3,3,4,5,5]

def search_el(l):
    start = 0
    end = len(l) - 1
    while start < end:
        mid = (start + end) // 2
        if l[mid] != l[mid - 1] and l[mid] != l[mid + 1]:
            return l[mid]
        elif l[mid] != l[mid - 1]:
            if mid % 2 == 0:
                start = mid + 2
            else:
                end = mid - 1
        else:
            if mid % 2 == 0:
                end = mid -2 
            else:
                start = mid - 1
    return l[start]

print(search_el(l))