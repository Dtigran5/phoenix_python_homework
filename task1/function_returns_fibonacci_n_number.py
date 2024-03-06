def fibonacci(n):
    if n <= 1:
        return n
    else:
        num = [0,1]
        for i in range(2, n +1):
            num.append(num[-1] + num[-2])
        return num[n]

n = int(input("Enter number: "))
print( "The", n, "th Fibonacci number:",fibonacci(n))