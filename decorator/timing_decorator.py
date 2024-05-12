from time import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        duration = end_time - start_time
        print(f"Execution time: {duration} seconds")
        return result
    return wrapper

@timing_decorator
def example_function():
    return "hello"

print(example_function())
