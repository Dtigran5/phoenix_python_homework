import time

def retry(max_retries, delay, exceptions=(Exception,)):
    def decorator(func):
        def wrapper(*args, **kwargs):
            retries = 0
            while retries < max_retries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    retries += 1
                    print(f"Exception occurred: {e}. Retrying in {delay} seconds...")
                    time.sleep(delay)
            return None  
        return wrapper
    return decorator

@retry(max_retries=3, delay=1, exceptions=(RuntimeError,))
def example_function():
    import random
    if random.randint(0, 10) < 8:
        raise RuntimeError("Random error occurred")
    else:
        return "Success"

result = example_function()
print(result)
