def custom_zip(*iterables):
    result = []
    for i in range(len(iterables[0])):
        temp = []
        for iterable in iterables:
            temp.append(iterable[i])
        result.append(tuple(temp))
    return result

a = [1, 2, 3]
b = ['a', 'b', 'c']
c = (True, False, True)

for item in custom_zip(a, b, c):
    print(item)
