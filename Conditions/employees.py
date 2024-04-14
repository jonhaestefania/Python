# Using multiples list to compare actions

current_employees = ['matt', 'peter', 'bruce', 'barry', 'jon']

absent_employees = ['reed', 'clark', 'meii']

for absent_employee in absent_employees:
    if absent_employee in current_employees:
        print(f"The employee {absent_employee.title()} is working on ")

    else:
        print(f"Employee {absent_employee.title()} is absent.")
