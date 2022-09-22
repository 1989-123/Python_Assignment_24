"""
Write a python program to create 2 objects of 
the user class and assign different values. 
"""

class Person:
    
    def display(self, name, age):
        self.name = name
        self.age = age
        print(name, age)


p1 = Person()
p2 = Person()

print()
p1.display("Jayesh", 32)
p2.display("Hitesh", 35)
print()
