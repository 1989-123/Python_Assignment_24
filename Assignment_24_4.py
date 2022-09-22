"""
Write a python program to init default values for user 
object using __init__ method.
"""

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(name, age)

print()
p1 = Person("Jayesh", 33)
print()
