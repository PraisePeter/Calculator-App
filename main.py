def add (a, b):
    return a + b

def sub (a, b):
    return a - b

def mul (a, b):
    return a * b

def div (a, b):
    return a / b

def calculator ():
    print("=== Simple Calculator ===")
    print("Operations: + | - | * | /")
    print("Type 'quit' to exit\n")
    #CREATE A WHILE LOOP INSIDE THE CALCULATOR APP
    while True:
        try:
            num1 = input("Enter a number")
            if num1.lower() == "quit":
                break

            operator = input("Enter an operator, +, -, /, or *")
            if operator not in ("+", "-", "*", "/"):
                print("Invalid operator. Please use +, -, *, or /", "\n")
                continue

            num2 = input("Enter another number")
            if num2.lower() == "quit":
                break

            a = float(num1)
            b = float(num2)
        except ValueError:
            print("Invalid Input. Please enter a numeric value. \n")

        if operator == "+":
            result = add(a, b)
        elif operator == "-":
            result = sub(a, b)
        elif operator == "*":
            result = mul(a, b)
        elif operator == "/":
            result = div(a, b)

#this print statement is called anF STRING
        print(f"\nResult: {a} {operator} {b} = {result}\n")


calculator()

#REMIND BRIGHT TO TEACH ME THE TRY LOOP


