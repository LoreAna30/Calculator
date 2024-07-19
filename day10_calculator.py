from logos import calcul

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2

operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide}

def calculator():
    print(calcul)
    num1 = int(input("What is the first number? "))
    for key in operations:
        print(key)

    calculator_run = True
    while calculator_run:
        operation_symbol = input("Pick an operation: ")
        another_number = int(input("What is the next number? "))
        calculation_function = operations[operation_symbol]
        result = calculation_function(num1, another_number)
        print(f"{num1} {operation_symbol} {another_number} = {result}")
        counting = input(f"Would you like to continue with {result}? Type Y, otherwise type N to exit or type C to start new calculation: ").lower()
        if counting == "y":
            num1 = result
        if counting == "n":
            calculator_run = False
        if counting == "c":
            calculator_run = False
            calculator()


calculator()



