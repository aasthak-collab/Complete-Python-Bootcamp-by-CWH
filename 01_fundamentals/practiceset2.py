#Q1. Write a program that asks the user for a number and prints whether it is positive, negative, or zero.
# a = int(input("Enter a number:"))
# if a == 0:
#     print("It is a whole number")
# elif a>0:
#     print("It is a positive number")
# else :
#     print("It is a negative  number")
#Q2. Create a program that checks if a person is eligible to vote (age >= 18).
# age = int(input("Enter your age:"))
# if age>=18:
#     print("You are eligible to vote!")
# else:
#     print("You are not eligible to vote!")
#Q3. Write a program that takes a number from the user and prints "Even" if it is even, otherwise "Odd".
# a = int(input("Enter a number:"))
# if a%2==0:
#     print("It is an even number!")
# else:
#     print("It is an odd number!")
#Q4.Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case.
# a = int(input("Enter the day no.:"))
# match a:
#     case 1:
#         print("Its a monday!")
#     case 2:
#         print("Its a tuesday!")
#     case 3:
#         print("Its a Wednesday!")
#     case 4:
#         print("Its a Thursday!")
#     case 5:
#         print("Its a Friday!")
#     case 6:
#         print("Its a Saturday!")
#     case 7:
#         print("Its a Sunday!")
#Q5. Write a program using match case that simulates a simple calculator.
# x = float(input("Enter first number:"))
# y = float(input("Enter second number:"))
# op = input("Enter operation (+,-,*,/):")
# match op:
#     case '+':
#         result = x+y
#     case '-':
#         result = x-y
#     case '*':
#         result = x*y
#     case '/':
#         if y!=0:
#             result = x/y
#         else:
#             result = "Error: Division by zero is not allowed."
#     case _:
#         result = "Error: Invalid operation"
# print("Result:",result)

 