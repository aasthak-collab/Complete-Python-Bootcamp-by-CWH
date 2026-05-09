# #these three are higher order functions in Python that operates on iterables like lists, tuples.
# #1. MAPS
# numbers = [1,2,3,56,77,65]

# def square(x):
#     return x * x

# new = list(map(square,numbers))
# print(new)

# #FILTER FUNCTION - it filters the iterable based on the condition.
# def is_greater_than_9(x):
#     if x>9:
#         return True
#     else:
#         return False
# a = [1,3,5,7,98,54,23,22,4]
# new = list(filter(is_greater_than_9,a))
# print(new)

#REDUCE - has to be imported from functools module

from  functools import reduce
numbers  = [1,2,3,4,5,6]
def sum (a,b):
    return a+b
c = reduce(sum,numbers)
print(c)
