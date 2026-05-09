# try:
#     a = int(input("Enter number 1:"))
#     b = int(input("Enter number 2:"))
#     print("The division is ", a/b)

# except ValueError:
#     print("Please dont perform bad typecasts")
    
# except ZeroDivisionError:
#     print("Hey dont divide by 0")
# except Exception as e: #here we used e to demonstrate error in a bit depth like if there are this character not a int value like this
#     print("An error occured", e)

#USING raise ERROR
a = int(input("Enter number 1:"))
b = int(input("Enter number 2:"))
if b==0:
    raise ValueError("Please dont divide by 0")

print("The division is" , a/b)