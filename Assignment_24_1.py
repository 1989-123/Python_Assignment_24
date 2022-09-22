"""
Write a python program to create a user class 
with 3 properties : name, age, email 
"""

# class Computer:

#     def __init__(self, cpu, ram):
#         self.cpu = cpu
#         self.ram = ram

#     def show(self):
#         print(self.cpu, self.ram)

# c1 = Computer("i3", 8)
# c2 = Computer("i5", 16)

# print()
# c1.show()
# c2.show()
# print()


class Person:

    def display(self):
        print(self.name)
        print(self.age)
        print(self.email)


p1 = Person()
p1.name = "Jayesh"
p1.age = 33
p1.email = 'pj92147@gmail.com'
print()
p1.display()
print()
