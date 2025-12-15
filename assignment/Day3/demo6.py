# Arithmetic operation functions
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


# Calculate function (takes a function as argument)
def calculate(op1, op2, operation):
    return operation(op1, op2)


# Testing the calculate function
print("Addition:", calculate(10, 5, add))
print("Subtraction:", calculate(10, 5, subtract))
print("Multiplication:", calculate(10, 5, multiply))
print("Division:", calculate(10, 5, divide))

print("Addition:", calculate(7, 3, add))
print("Multiplication:", calculate(4, 6, multiply))
print("Division:", calculate(8, 0, divide))