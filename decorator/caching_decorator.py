def cache_decorator(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    return wrapper

@cache_decorator
def example_task(n):
    print(f"Executing task for {n}")
    return n * 2

print(example_task(5))  
print(example_task(5))  
print(example_task(3))  
print(example_task(3))  
