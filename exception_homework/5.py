import warnings

def deprecated_function():
    warnings.warn("This function is deprecated and will be removed in the future.", DeprecationWarning)
    print("This function is deprecated. Please avoid from using it.")
deprecated_function()
