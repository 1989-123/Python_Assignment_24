"""
WRT 7th Question, create 3 Laptop objects and add them 
to the list in the sorted order based on the ram size.
"""

class Laptop:
    

    def __init__(self, brand, ram, cpu, hdd):
        self.brand = brand
        self.ram = ram
        self.cpu = cpu
        self.hdd = hdd

    def showConfig(l1, l2, l3):
        for i in l1, l2, l3:
            l4.append(i.ram)
        print(sorted(l4))


l4 = []
l1 = Laptop("HP", 128, "i5", 34)
l2 = Laptop("Dell", 16, "i6" ,67)
l3 = Laptop("Apple", 32, "i9", 625)

print()
l1.showConfig(l2, l3)
print()
