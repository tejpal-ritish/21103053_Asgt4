#Q5. wap to store details of 3 employees


class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

emp1=Employee("Mehak",40000)
emp2=Employee("Ashok",50000)
emp3=Employee("Viren",60000)

print('Part A) -> \n')
emp1.salary=70000
print('The updated salary of employee Mehak is -> ',emp1.salary,'\n')

print('Part B) -> \n ')
del emp1
print('Record of employee Viren has been deleted')
