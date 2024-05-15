from contextlib import contextmanager

@contextmanager
def suppress_exception(exception_type):
    try:
        yield
    except exception_type:
        pass

with suppress_exception(ZeroDivisionError):
    result = 10 / 0 
    print("This line will be executed even though an exception occurred.")
