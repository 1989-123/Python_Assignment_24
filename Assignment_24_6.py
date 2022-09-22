"""
Write a python program to create 3 user objects 
and find the youngest of all. 
"""

class Person:


    def greter(p1, p2, p3):
         ((print("P1 is greter") if p1 > p3 else print("P3 is greter"))) if p1 > p2 else ((print("P2 is greter") if p2 > p3 else print("P3 is greter")))


p1 = Person()
p2 = Person()
p3 = Person()

print()
Person.greter(234, 65, 4388)
print()
