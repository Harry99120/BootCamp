def calculate_salary(basic_salary):
    hra = 0.20 * basic_salary
    da = 0.15 * basic_salary
    
    gross_salary = basic_salary + hra + da
    tax = 0.10 * gross_salary
    net_salary = gross_salary - tax
    
    return gross_salary, net_salary

def main():
    print("=== Employee Salary Calculator ===")
    
    employee_records = []
    
    while True:
        print("\nEnter Employee Details:")
        emp_id = input("Enter Employee ID: ").strip()
        name = input("Enter Employee Name: ").strip()
        
        try:
            basic_salary = float(input("Enter Basic Salary: "))
        except ValueError:
            print("Invalid salary input! Skipping this employee.")
            continue
        
        gross, net = calculate_salary(basic_salary)

        employee_records.append({
            "id": emp_id,
            "name": name,
            "gross": gross,
            "net": net
        })
        
        choice = input("\nDo you want to add another employee? (yes/no): ").strip().lower()
        if choice not in ('yes', 'y'):
            break

    print("\n" + "="*45)
    print("             SALARY SUMMARY             ")
    print("="*45)
    
    for emp in employee_records:
        print(f"Employee ID : {emp['id']}")
        print(f"Name        : {emp['name']}")
        print(f"Gross Salary: {emp['gross']:.2f}")
        print(f"Net Salary  : {emp['net']:.2f}")
        print("-" * 45)

if __name__ == "__main__":
    main()