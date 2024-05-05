def is_power_of_4(num):
    if num > 0 and (num & (num - 1)) == 0 and (num - 1) % 3 == 0:
        return True
    else:
        return False

num = int(input("Enter number: "))
print(is_power_of_4(num))