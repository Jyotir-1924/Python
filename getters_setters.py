class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @property
    def first_name(self):
        return self.name.split(" ")[0]
    @first_name.setter
    def first_name(self, name):
        new_name = f"{name} {self.name.split(" ")[1]}"
        self.name = new_name
e = Employee("Jyotiraditya Gautam", 45000)
print(e.first_name)
e.first_name = "Aditya"
print(e.name)