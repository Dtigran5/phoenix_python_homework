def error_handling_decorator(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"An error occurred: {e}")
            # Additional error handling logic can be added here
    return wrapper

def example_function():
    return "hello"
print(example_function())

def example_function1():
    return 5/0
print(example_function1())