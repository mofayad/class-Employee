class Employee:
    def __init__(self, baseSalary, bonusHrs, sales, name):
        self.baseSalary = baseSalary
        self.bonusHrs = bonusHrs
        self.sales = sales
        self.name = name

    def calculateNetSalary(self):
        bonus = self.bonusHrs * 10  # Assuming each bonus hour adds $10
        commission = 0.01 * self.sales  # Assuming a 1% commission on sales
        net_salary = self.baseSalary + bonus + commission
        return net_salary

    def info(self):
        print(f"Employee: {self.name}, Base Salary: ${self.baseSalary}, Bonus Hours: {self.bonusHrs} hrs, Sales: ${self.sales}")

# Example Test
employee1 = Employee(baseSalary=50000, bonusHrs=5, sales=100000, name="John Doe")

employee1.info()
net_salary = employee1.calculateNetSalary()
print(f"Net Salary: ${net_salary}")
