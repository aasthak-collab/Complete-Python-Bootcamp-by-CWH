class Employee:
    
    def __init__(self, salary, name, bond):
        self.salary = salary #creating an instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond
    
    def get_info(self):
        print(f"The name of the employee is {self.name}. \nThe salary is {self.salary}.\nAnd the bond is for {self.bond} years.")
    
e1 = Employee(34000, "John Doe", 5)
e1.get_info()