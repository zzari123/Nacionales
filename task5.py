class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        if amount > 0:
            self.salary += amount
            print(f"Salary increased by: ${amount:.2f}")
        else:
            print("Raise amount must be positive.")

    def display_employee(self):
        print(f"Employee Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ${self.salary:.2f}")


employee = Employee("John Smith", "Civil Engineer", 40000)

print("Initial Employee Details:")
employee.display_employee()

employee.give_raise(50000)  

print("\nUpdated Employee Details:")
employee.display_employee()