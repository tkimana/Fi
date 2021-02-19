
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


class Designer(Employee):
    pass



Se= SoftwareEngineer('Joe', 24, 4000, 'Junior')
De= Designer('Greg', 34, 500)

print(Se.level)

Se.work()