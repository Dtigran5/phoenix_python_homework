def custom_deep_copy(obj, copies=None):
    if copies is None:
        copies = {}
    if id(obj) in copies:
        return copies[id(obj)]
    if isinstance(obj, dict):
        copied_obj = {}
        copies[id(obj)] = copied_obj
        for key, value in obj.items():
            copied_obj[custom_deep_copy(key, copies)] = custom_deep_copy(value, copies)
        return copied_obj
    elif isinstance(obj, list):
        copied_obj = []
        copies[id(obj)] = copied_obj
        for item in obj:
            copied_obj.append(custom_deep_copy(item, copies))
        return copied_obj
    elif isinstance(obj, tuple):
        copied_obj = tuple(custom_deep_copy(item, copies) for item in obj)
        copies[id(obj)] = copied_obj
        return copied_obj
    else:
        return obj


original_dict = {'a': 1, 'b': [2, 3], 'c': {'d': 4}}
copied_dict = custom_deep_copy(original_dict)

print("Original Dictionary:", original_dict)
print("Copied Dictionary:", copied_dict)

original_dict['b'][0] = 10  
original_dict['c']['d'] = 40 

print("\nOriginal Dictionary after modification:", original_dict)
print("Copied Dictionary:", copied_dict)  
