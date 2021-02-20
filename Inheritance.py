
# This is a base class
class Employee:
    def __init__(self, name, age, salary):
        self.name=name
        self.age=age
        self.salary=salary


    def work(self):
        print(f'{self.name} is working')

    


class SoftwareEngineer(Employee):
    

    def __init__(self, name, age, salary, level):
        super().__init__(name,age,salary)
        self.level=level

    def raised(self):
        print(f"{self.name} got the raised..")


class Designer(Employee):
    def __init__(self, name, age, salary, level, location):
        super().__init__(name, age, salary)
        self.location=location
        self.level=level




Se= SoftwareEngineer('Joe', 24, 4000, 'Junior')
De= Designer('Greg', 34, 500, 'Sunior', 'Houston')


print(De.level)
De.work()

Se.raised()

# Polymorphism


employees= [SoftwareEngineer('Joe', 24, 4000, 'Junior'), Designer('Greg', 34, 500, 'Sunior', 'Houston'),
 SoftwareEngineer('Math', 43, 500, 'Junior' )]



def motivate_employees(employees):
    for employee in employees:
            employee.work()

motivate_employees(employees)
