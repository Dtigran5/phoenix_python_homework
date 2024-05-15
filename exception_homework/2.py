try:
    with open('example.txt', 'r') as file:
        for line in file:
            print(line)
except IOError:
    print("Error: File not found.")
