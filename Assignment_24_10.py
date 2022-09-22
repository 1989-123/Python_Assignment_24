"""
Define a class Employee with instance object variables empid, name, salary. Write
__init__() method in the class to initialize instance object variables.
Also define instance methods to input fields and display field values 
"""

class Employee:

    def __init__(self):
        self.empid = input("Enter your Employee id: ")
        self.name = input("Enter your name: ")
        self.salary = int(input("Enter your salary: "))

    def show(self):
        print(self. empid, self.name, self.salary)


e1 = Employee()
print()
e2 = Employee()
print()
e1.show()
e2.show()
print()
