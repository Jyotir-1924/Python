class Company:
    companyName = "Meta"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    @classmethod
    def changeCompanyName(cls, newCompanyName):
        cls.companyName = newCompanyName
    @staticmethod
    def monthlyPayout(salary):
        return (salary-10000)*1.3
    
emp1 = Company("Pinku", 145000)
print(emp1.companyName)
emp1.changeCompanyName("Amazon")
print(emp1.monthlyPayout(emp1.salary))
print(emp1.companyName)
print(emp1.name)
print(emp1.salary)

#This is a program demonstrated to get the understanding of Static, Instance and Class methods. There are various needs which is demonstrated in the class.