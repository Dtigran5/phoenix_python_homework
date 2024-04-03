di = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

target = int(input("please enter value that you want to find in dictionary: "))

if target in di.values():
    print(f"the value {target} is in dictionary")
else:
    print(f"the value {target} is not in dictionary")