# Class and Objects

class student:
    roll_no = None
    name = None

s0 = student()
s0.roll_no = 0
s0.name = "John Doe"
print(s0.roll_no, s0.name)

s1 = student()
print(s1.roll_no, s1.name)

s2 = student()
s2.roll_no = 2
s2.name = "Jane 2 Doe"
print(s2.roll_no, s2.name)

s50 = student()
s50.name = "asmith"
print(s50.roll_no, s50.name)

# Attributes and Methods


class student:
    count =0
    def __init__(self, roll_no, name, total):
        self.roll_no = roll_no
        self.name = name
        self.total = total
        
    def display(self):
        print(self.roll_no, self.name, self.total)

    def result(self):
        if self.total > 120:
            print("pass")
        else:
            print("fail")

        
s0 = student(0, "John Doe" , 100)
s0.display()
s0.result()

s1 = student(1, "Jane Doe" , 150)
s1.display()
s1.result()

# next

i = int()
print(type(i))

s = str()
print(type(s))

l = list()
print(type(l))

d = dict()
print(type(d))

