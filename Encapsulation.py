class SoftwareEngineer:
     def __init__(self, name, age):
         self.name= name
         self.age=age
         self._salary=None
         self._number_of_bugs_solved=0

     def code(self):
        self._number_of_bugs_solved+=1
    # Getter
     def Get_Salary(self):
        return self._salary
    # Setter
     def Set_Salary(self, base_value):
         # Check value, and enforce constraints
        self._salary= self._calculate_salary(base_value)
        #self._salary=value

     def _calculate_salary(self, base_value):
        if self._number_of_bugs_solved < 10:
            return base_value + 2
        if self._number_of_bugs_solved < 100:
            return base_value * 2
        return base_value * 3

     

Se= SoftwareEngineer('Math', 34)

for i in range(40):
    Se.code()

print(Se._number_of_bugs_solved)

Se.Set_Salary(400)
print(Se.Get_Salary())

