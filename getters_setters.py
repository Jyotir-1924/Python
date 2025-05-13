class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @property
    def first_name(self):
        return self.name.split(" ")[0]
    #This defines the getter for the Class' object. When we use this, we need not call this as a function or rather as a Attribute/Entity.
    @first_name.setter
    def first_name(self, name):
        new_name = f"{name} {self.name.split(" ")[1]}"
        self.name = new_name
    #This acts as the setter for the Class' object. When we use this, we need not call this as a function or rather as a Attribute/Entity and simply pass the change that we need to set as an assignment.
e = Employee("Jyotiraditya Gautam", 45000)
print(e.first_name)
e.first_name = "Aditya"
print(e.name)