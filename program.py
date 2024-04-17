def read_employees(file_name):
    employees = []
    with open(file_name, 'r') as file:
        for line in file:
            name, age, department = line.strip().split(',')
            age = int(age)
            employees.append((name, age, department))
    return employees

def calculate_average_age(employees):
    total_age = sum(emp[1] for emp in employees)
    return total_age / len(employees)

def count_employees_by_department(employees):
    department_count = {}
    for emp in employees:
        department_count[emp[2]] = department_count.get(emp[2], 0) + 1
    return department_count

def find_oldest_and_youngest(employees):
    oldest = max(employees, key=lambda x: x[1])
    youngest = min(employees, key=lambda x: x[1])
    return oldest, youngest

def write_results(file_name, average_age, department_count, oldest, youngest):
    with open(file_name, 'w') as file:
        file.write(f"Average Age of Employees: {average_age}\n")
        file.write("Employee Count by Department:\n")
        for department, count in department_count.items():
            file.write(f"{department}: {count}\n")
        file.write(f"Oldest Employee: {oldest[0]}, Age: {oldest[1]}, Department: {oldest[2]}\n")
        file.write(f"Youngest Employee: {youngest[0]}, Age: {youngest[1]}, Department: {youngest[2]}\n")

input_file = 'person.txt'
output_file = 'employee_results.txt'

employees = read_employees(input_file)
average_age = calculate_average_age(employees)
department_count = count_employees_by_department(employees)
oldest, youngest = find_oldest_and_youngest(employees)
write_results(output_file, average_age, department_count, oldest, youngest)

print("Results have been written to", output_file)
