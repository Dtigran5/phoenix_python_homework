def pythogoras(n):
    ls = []
    for a in range(1, n + 1):
        for b in range(a, n + 1):
            c = (a**2 + b**2) ** 0.5
            if c.is_integer() and c <= n:
                ls.append((a,b, int(c)))
    return ls

print(pythogoras(10))
print(pythogoras(20))
