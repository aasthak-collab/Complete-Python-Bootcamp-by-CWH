#Decorator is a function, it creates a new function inside its body(wrapper). Then it returns that new function.
#we use decorator function to change the functionality of the function
def decorator(func):
    def wrapper():
        print("I am about to execute a function...")
        func()
        print("I have executed the function...")
    return wrapper
@decorator
def say_hello():
    print("Hello!")
    
say_hello()