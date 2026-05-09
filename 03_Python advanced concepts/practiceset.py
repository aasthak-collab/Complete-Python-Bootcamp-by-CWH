#Q1.Write a decorator logger that prints "Function is being called" before the function runs. Use it to decorate a function say_hello() that prints "Hello!".
#ANS:
# def decorator(func):
#     def wrapper():
#         print("Function is being called")
#         func()
#     return wrapper
    
# @decorator
# def say_hello():
#     print("Hello!")
    
# say_hello()

def sum(n):
    def decorator(func):
        def wrapper():
            for i in range(1,1000000):
                func()
        return wrapper
    return decorator
@sum(n)
def the_sum_is():
    print(sum(n))

the_sum_is()
    