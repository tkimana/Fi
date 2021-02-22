class SoftwareEngineer:
     def __init__(self):
         self._salary=None
         self._number_of_bugs_solved=0


    # Getter
     @property
     def Salary(self):
        return self._salary
    # Setter
     @Salary.setter
     def Salary(self, value):
        self._salary= value
     @Salary.deleter
     def Salary(self):
        del self._salary
     



     

Se= SoftwareEngineer()
Se.Salary=400

del Se.Salary  
print(Se.Salary)

