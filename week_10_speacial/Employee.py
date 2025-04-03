from person import person

class Employee(person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
        
    def display(self):
        print(self.name, self.age, self.salary)