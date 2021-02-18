
se1=["Software Engineer", "Joe", 10, "junior", 3000]
se2=["Software Engineer", "Alex", 100, "Sunior", 5000]


# Creating a Function in Python
def code(se):
    print(f'{se[1]} is writing code ...')

code(se2)


class SoftwareEngineer:
    # Class attribute
    alies= 'Magic keyboard'
    def __init__(self, name, age, level, salary):

        # Instance Attributes
        self.name= name
        self.age= age
        self.level= level
        self.salary= salary
        self.active=True



# Instance Method
    def code(self):
        print(f'{self.name} is writing code ...')

    def code_in_language(self, language):

        print(f'{self.name} is coding in {language}' )

    def information(self):
        information= f'name: {self.name}, age: {self.age}, {self.level}, {self.active}'
        return information
    


    



# Instance 
Se1= SoftwareEngineer('greg', 23, 'Entry Level', '80k')
print(Se1.name, Se1.age, Se1.level, Se1.salary)
print(Se1.alies)
Se1.code()
Se1.code_in_language('Java')

print(Se1.information())

# Recap
# Create a class(blueprint)
# create a instance (object)
# class vs instance 
# instance attributes: defined in __init__(self)
# Class attributes