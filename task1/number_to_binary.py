number = int(input("Enter number: "))
binary =""
while number > 0:
    binary += str(number % 2)
    number = number // 2
print("Binary representation:", binary)