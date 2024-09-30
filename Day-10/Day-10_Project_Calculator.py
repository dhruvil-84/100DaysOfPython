from replit import clear

def addition(num1, num2):
    '''Takes two numbers(float or int) as input and returns their sum.'''
    return num1 + num2

def subtraction(num1, num2):
    '''Takes two numbers(float or int) as input and returns their difference.'''
    return num1 - num2

def multiplication(num1, num2):
    '''Takes two numbers(float or int) as input and returns their product.'''
    return num1 * num2

def division(num1, num2):
    '''Takes two numbers(float or int) as input and returns their Quotient.'''
    return num1 / num2

operations = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}

def calculator():
    """performs all the basic arithmetic operations."""
    num1 = float(input("What's the first number?: "))
    result = 0

    discontinue = False
    # while discontinue == False: #--> when executed gives bugs sometimes. (bugs like when entered anything else instead of 'y' or 'n' it executes instead of exitting the code.)
    while not discontinue:

        for symbols in operations:
            print(symbols)
        operation = input("Pick an operation: ").strip()
        num2 = float(input("What's the next number?: "))

        if operation in operations:
            result = operations[operation](num1 = num1, num2 = num2)
            print(f"{num1} {operation} {num2} = {result}")
        else:
            print("Invalid operation.")

        temp = input(f"Type 'y' to continue calculating with {result}, or type 'n' to make a new calculation, or type 'quit' to exit from the calculator: ").strip().lower()
        if temp == 'y':
            num1 = result
        elif temp == 'n':
            clear()
            discontinue = True
            calculator()
        else:
            discontinue = True

clear()
print("""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
""")
calculator()