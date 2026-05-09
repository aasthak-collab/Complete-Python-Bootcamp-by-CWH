#Class: is a blue[rint or a template. eg: form of an exam containing name,age,class
#Object: Specific instace created from the template(class). eg: Form which contains the data of John Doe

class Employee:
    company = "HP"
    
    def get_salary(self): #any object if we are creating we can refer it as self and it is mandatory to give 1st parameter ALWAYS to self when we are are defining inside a class
        print(self)
        return 34000

e = Employee() #An object of class Employeee is created here 
print(e.get_salary()) #Employee e's get salary method is called here

e2 = Employee()
print(e2.get_salary())
print(e2.company)