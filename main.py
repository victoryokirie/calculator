# Calculator

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def exponential(n1, n2):
    return n1 ** n2

operations ={
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply,
    "**": exponential
}

def calculator():
    num1= int(input("What't the first number? "))

    for symbol in operations:
        print(symbol)

    should_continue=True
    
    while should_continue:

        operation_symbol= input("Pick an operation: ")

        num2= int(input("What't the next number? "))

        calculator_function= operations[operation_symbol]
        answer=calculator_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        looping_condition=input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation or type 'exit' to exit the calculator: ")
        if looping_condition == "y":
            num1=answer
        elif looping_condition == "n":
            should_continue= False
            calculator()
        else:
            should_continue= False
            print("Calculator exited")

calculator()



