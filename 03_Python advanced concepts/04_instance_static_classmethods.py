# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
        
#     #instance method(default)
#     def print_info(self):
#         info = f"My name is {self.name} and the salary is {self.salary}"
#         print(info)
         
# e1 = Employee("Jack", 3455)
# e2 = Employee("Jill", 34355)
# e1.print_info()
# e2.print_info()

# #STATIC METHOD - doesnt need self parameter
# #used to write utility methods like harmonic  mean, avg of two numbers, etc

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
        
#     @staticmethod
#     def sum(a, b):
#         return a+b
        
# e1 = Employee("Jack", 3455)
# e2 = Employee("Jill", 34355)
# print(e2.sum(5,23))

#CLASS METHOD:- has the cls parameter
class Employee:
    company = "HP"
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        
    def print_company(cls):
        print(cls.company)
        
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

e1 = Employee("Jack", 3455)
e2 = Employee("Jill", 34355)
print(Employee.company)
e1.change_company("Acer")
print(Employee.company)