from person import person

class student(person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.marks = marks
        
    def display(self):
        super().display()
        print( self.marks)