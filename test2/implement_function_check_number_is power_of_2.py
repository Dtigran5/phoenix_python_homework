def is_power_of_two(num):
    if num != 0 and (num & (num - 1)) == 0:
        return True 
    else:
        return False


num = int(input("enter number: "))
print(is_power_of_two(num))