class Employee:
    def __init__(self, name, department="General", bonus=0):
        self.name = name
        self.department = department
        self.bonus = bonus
        self.base_salary = 30000

    def annual_summary(self):
        total_pay = self.base_salary + self.bonus
        print(f"Employee Name: {self.name}")
        print(f"Department:    {self.department}")
        print(f"Total Pay:     ₹{total_pay} (Base: ₹{self.base_salary} + Bonus: ₹{self.bonus})")
        print("-" * 50)


print("--- EMPLOYEE ANNUAL SUMMARIES ---\n")

emp1 = Employee("Harmeet Bhati", "Engineering", 15000)
emp1.annual_summary()

emp2 = Employee("Nikhil Bhiduri", "Logistics")
emp2.annual_summary()

emp3 = Employee("Anusha")
emp3.annual_summary()