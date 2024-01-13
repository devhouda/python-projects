def add(value1, value2):
    return value1 + value2

def sub(value1, value2):
    return value1 - value2

def mul(value1, value2):
    return value1 * value2

def div(value1, value2):
    return value1 / value2

print("Welcome to my calculator")
while True:
    operation = input("Choose the operation (+ , -, *, /) or (e to exit): ")
    if operation == "e" or operation == "E":
        print("Program Ended.")
        quit()
    value1 = int(input("Enter First Value: "))
    value2 = int(input("Enter Second Value: "))

    if operation == "+":
        print(f"{value1} + {value2} = {add(value1, value2)}")
    elif operation == "-":
        print(f"{value1} - {value2} = {sub(value1, value2)}")
    elif operation == "*":
        print(f"{value1} * {value2} = {mul(value1, value2)}")
    elif operation == "/":
        if value2 == 0:
            print("ZeroDivisionError! You can't devide by zero.")
        else:
            print(f"{value1} / {value2} = {div(value1, value2)}")
    else:
        print("Operation unknown.")
