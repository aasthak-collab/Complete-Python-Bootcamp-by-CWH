#typecasting in python
# a = 34
# b = "34"
# print(a)
# print(type(a))
# print(b)
# print(type(b))
#now we'll convert the string "34" to int
# c = int(b)
# print(c)
# print(type(c))

#taking user input 
# a = int(input("Enter a number: "))
# print(a)
# b = int(input("Enter a number: "))
# print(b)
# print(a+b)

# if else conditions
# age = int(input("Enter your age: "))
# if (age>18):
#     print("You can drive")
#     print("Drive safely!")
# else:
#     print("Your are not eligibile to drive")

# if elif else
# age = int(input("Enter your age: "))
# if(age>18):
#     print("You can drive!")
# elif(age==18):
#     print("You need to take the parental guidance")
# else:
#     print("Sorry you cannot drive!")


#using match case statements
a = int(input("Enter a number between 1 to 10:"))
match a:
    case 1:
        print("You won $10")
    case 4:
        print("You  won a camera")
    case 7:
        print("You won a gift card")
    case _:
        print("Better luck next time")