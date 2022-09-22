"""
Write a python program to create a School class 
and 3 instance variables and 1 class variable. 
"""

class School:

    School = "JVSK"

    def __init__(self, name, roll_number, age):
        self.name = name
        self.roll_number = roll_number
        self.age = age



s1 = School("Jayesh", 12, 33)
s2 = School("Hitesh", 14, 35)

print()
print(s1.name, s1.roll_number, s1.age, s1.School)
print(s2.name, s2.roll_number, s2.age, s2.School)
print()
