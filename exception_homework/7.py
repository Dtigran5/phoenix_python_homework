def validate_date_format():
    while True:
        try:
            date_input = input("Please enter a date in the format 'YYYY-MM-DD': ")
            if len(date_input) != 10 or date_input[4] != '-' or date_input[7] != '-':
                raise ValueError("Incorrect date format. Please use 'YYYY-MM-DD'.")
            break
        except ValueError as ve:
            print(ve)

validate_date_format()
