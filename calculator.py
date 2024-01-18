from art import logo

# Adds numbers.
def add(n1, n2):
    return n1 + n2

# Subtract numbers.
def subtract(n1, n2):
    return n1 - n2

# Multiplies numbers.
def multiply(n1, n2):
    return n1 * n2

# Divides numbers.
def divide(n1, n2):
    return n1 / n2

# Maps symbols with functions.
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Calculates operation for numbers.
def calculate(operation_symbol, first_number, second_number):
    calculation_function = operations[operation_symbol]
    result = calculation_function(first_number, second_number)
    return result

# Takes user's inputs an calls the calculation. Controls flow.
def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    should_continue = True

    while should_continue == True:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the list list above: ")
        num2 = float(input("What's the next number?: "))

        # Gets the calculation result.
        result = calculate(operation_symbol, num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")

        # Determines whether current calculation continues.
        continue_calculation = input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit.: ")
        if continue_calculation == "y":
            num1 = result
        elif continue_calculation == "n":
            should_continue = False
    
    # Restarts calculation.
    calculator()

calculator()
