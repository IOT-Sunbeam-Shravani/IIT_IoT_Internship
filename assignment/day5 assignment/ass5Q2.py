def add(a,b):
    return a+b

def substract (a,b):
    return a-b

def multiply (a,b):
    return a*b

def divide (a,b):
    if b==0:
        return "Error! Division by zero."
    return a/b


import ass5Q2

a = float(input("Enter first number: "))
b = float(input("enter second number:"))

print("Addition:", ass5Q2.add(a,b))
print("Substraction:", ass5Q2.substract(a,b))
print("Multiplication:", ass5Q2.multiply(a,b))
print("Division:", ass5Q2.divide(a,b))