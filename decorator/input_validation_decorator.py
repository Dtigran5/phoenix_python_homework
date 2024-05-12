def input_validation_decorator(validation_rules):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if not validation_rules(*args, **kwargs):
                raise ValueError("Input validation failed. Please check your inputs.")
            return func(*args, **kwargs)
        return wrapper
    return decorator

def check_positive_number(a, b):
    return a > 0 and b > 0

@input_validation_decorator(check_positive_number)
def divide(a, b):
    return a / b

try:
    result = divide(10, 0)
except ValueError as e:
    print(e)
