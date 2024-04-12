def largest_square_less_than_n(n):
    i = 1
    while i ** 2 <= n:
        i += 1
    return (i - 1) ** 2


n = int(input("Enter n: "))
result = largest_square_less_than_n(n)
print(f"Largest square less than or equal to {n}: {result}")
