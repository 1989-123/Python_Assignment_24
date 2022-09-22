"""
Write a python program to delete the 
age property of the user 
"""

class Person:

    def diaplay(self, name, age):
        self.name = name
        self.age = age
        print(name, age)


print()
p1 = Person()
p1.name = "Jayesh"
p1.age = 33
p1.diaplay(p1.name, p1.age)
del p1.age
p1.diaplay(p1.name, p1.age)
print()
