# #ARGS
# def sum(*args):
#     #args tuple ke form mein data display krta hai
#     total = 0
#     for item in args:
#         total += item
#     return total

# print(sum(342,2,7,9))

# #KWARGS
# def marks(**kwargs):
#     #kwargs is a dictiionary with all the key value pairs which were passed to marks
#     for item in kwargs.keys():
#         print(f"The marks of {item} is {kwargs[item]}")
        
# marks(shubham = 34, vikrant = 56, marie = 76, chloe = 60)

#ARGS AND KWARGS(always args will come first then kwargs)
def func1(*args, **kwargs):
    print(args)
    print(kwargs)
func1(1,2,3,4, jack = 45, jill = 56, chloe = 76)