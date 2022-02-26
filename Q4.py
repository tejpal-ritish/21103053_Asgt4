#Q4. wap to make a class and execute functions on it

class student:                                                                                          
    def __init__(self,name,rno):
        self.name=name
        self.rno=rno
        print('Object Created\n')
    def __del__(self):
        print('Object destroyed')
name=input('Enter name of student -> ').strip()                                                         
roll=int(input('Enter roll number of student -> '))
student1=student(name,roll)                                                                        
print('The name of the student is %s and the roll number is %d \n' % (student1.name,student1.rno)) 
del student1
