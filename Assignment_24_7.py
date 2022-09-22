"""
Write a python program to create a Laptop class 
with 4 attributes (brand, ram, cpu,hdd) and 2 methods 
(showConfig() to print the values, __init__() to 
initialize thevalues). 
"""

class Laptop:
    

    def __init__(self, brand, ram, cpu, hdd):
        self.brand = brand
        self.ram = ram
        self.cpu = cpu
        self.hdd = hdd

    def showConfig(self):
        print("BRAND is:",self.brand)
        print("RAM is:", self.ram)
        print("CPU is:", self.cpu)
        print("HDD is:", self.hdd)


l1 = Laptop("HP", "16 GB", "i5", 34)
l2 = Laptop("Dell", "32 GB", "i6", 67)
l3 = Laptop("Apple", "128 GB", "i9", 625)

print()
l1.showConfig()
print()
l2.showConfig()
print()
