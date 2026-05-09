a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print("What kind of operation do you want to perform.\nPress + for addition \nPress - for subtration\nPress / for division\nPress * for multiplication")

o = input("Enter operation:")
match o:
    case "+":
        print("The result is {a+b}")
    case "-":
        print("The result is {a-b}")
    case "/":
        print("The result is {a/b}")
    case "*":
        print("The result is {a*b}")
    case default:
        print("There was an error")
        