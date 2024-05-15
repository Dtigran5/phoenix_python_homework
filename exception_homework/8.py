import sys

def recursive_function():
    try:
        recursive_function()
    except RecursionError:
        print("Maximum recursion depth exceeded.")
        sys.exit()

recursive_function()
