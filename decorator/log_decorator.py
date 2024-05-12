import time

def log_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"Task '{func.__name__}' started at {start_time}")
        result = None
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print(f"Exception in task '{func.__name__}': {e}")
            return None 
        end_time = time.time()
        print(f"Task '{func.__name__}' ended at {end_time}. Elapsed time: {end_time - start_time} seconds")
        return result
    return wrapper

@log_decorator
def example_task():
    print("Executing example task...")
    time.sleep(2)
    return "Task completed successfully"

print(example_task())
