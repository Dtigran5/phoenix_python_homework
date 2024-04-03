text = input("please input string: ")
di = {}

for char in text:
    if char.isalpha():
        di[char] = di.get(char, 0) + 1

print(di)