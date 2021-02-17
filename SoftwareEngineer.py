
se1=["Software Engineer", "Joe", 10, "junior", 3000]
se2=["Software Engineer", "Alex", 100, "Sunior", 5000]

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




# Instance 
Se1= SoftwareEngineer('greg', 23, 'Entry Level', '80k')
print(Se1.name, Se1.age, Se1.level, Se1.salary)
print(Se1.alies)

# Recap
# Create a class(blueprint)
# create a instance (object)
# class vs instance 
# instance attributes: defined in __init__(self)
# Class attributes