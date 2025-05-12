#  This is a class and object code sample
class Employee:

    def __init__(self, salary, name, company):
        self.salary = salary
        self.name = name
        self.company = company
    
    def get_info(self):
        print(f"The name of Employee is {self.name}")
        print(f"The salary of the Employee is {self.salary}")
        print(f"Company name is {self.company}")
        
e1 = Employee("1,45,000", "Jyotir", "Delhi")
e1.get_info()