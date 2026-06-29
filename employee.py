class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

    def display(self):
        print(f"Name: {self.name}")
        print(f"Salary: ₹{self.calculate_salary()}")

class RegularEmployee(Employee):
    def __init__(self, name, salary, bonus=0):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.salary + self.bonus

class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, salary=0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

class Manager(Employee):
    def __init__(self, name, salary, bonus=0, allowance=0):
        super().__init__(name, salary)
        self.bonus = bonus
        self.allowance = allowance

    def calculate_salary(self):
        return self.salary + self.bonus + self.allowance

# User Input
print("=== Regular Employee ===")
name = input("Enter Name: ")
salary = int(input("Enter Salary: ₹"))
bonus = int(input("Enter Bonus: ₹"))
re = RegularEmployee(name, salary, bonus)
re.display()

print("\n=== Contract Employee ===")
name2 = input("Enter Name: ")
rate = int(input("Enter Hourly Rate: ₹"))
hours = int(input("Enter Hours Worked: "))
ce = ContractEmployee(name2, rate, hours)
ce.display()

print("\n=== Manager ===")
name3 = input("Enter Name: ")
salary3 = int(input("Enter Salary: ₹"))
bonus3 = int(input("Enter Bonus: ₹"))
allowance = int(input("Enter Allowance: ₹"))
mg = Manager(name3, salary3, bonus3, allowance)
mg.display()