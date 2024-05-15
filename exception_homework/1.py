def read_integer():
    try:
        num = int(input("Enter an integer: "))
        return num
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return None

read_integer()