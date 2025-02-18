import os
def add (a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
operations_dict={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    number1 = float(input("enter the first number: "))
    for symbol in operations_dict:
        print(symbol)
    continue_flag = True
    while continue_flag:

        op_symbol = input("pick an operations: : ")
        number2 = float(input("enter the second number: "))
        calculator_function = operations_dict[op_symbol]
        output = calculator_function(number1, number2)
        print(f"{number1} {op_symbol} {number2} = {output}")
        should_continue = input(
            f"enter 'y' to continue calculator with {output} or enter 'n' to start new calculator or enter 'x' to exit:")
        if should_continue == 'y':
            number1 = output
        elif should_continue == 'n':
            continue_flag = False
            os.system('cls')
            calculator()
        else:
            continue_flag=False
            print("bye")
calculator()


