def polindrome_step(number):
    steps= 0
    while str(number) != str(number)[::-1]:
        number += int(str(number)[::-1])
        steps += 1
    return steps

number = int(input("enter number: "))
print(polindrome_step(number))
