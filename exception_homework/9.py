def convert_strings_to_integers(str_list):
    failed_conversions = 0
    int_list = []
    
    for s in str_list:
        try:
            num = int(s)
            int_list.append(num)
        except ValueError:
            failed_conversions += 1
    
    return int_list, failed_conversions

str_list = ["10", "20", "30", "40", "50", "abc", "60"]
result, failed_conversions = convert_strings_to_integers(str_list)

print("Converted integers:", result)
print("Number of failed conversions:", failed_conversions)