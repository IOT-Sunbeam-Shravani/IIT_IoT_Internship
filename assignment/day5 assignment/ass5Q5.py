# __init__.py
# This file makes 'operations' a package


# arithmetic.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b


# string_ops.py

def to_upper(text):
    return text.upper()

def to_lower(text):
    return text.lower()

from ass5Q5.arithmetic import add, subtract
from ass5Q5.string_ops import to_upper, to_lower

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

text = input("Enter a string: ")

print("Addition:", add(a, b))
print("Subtraction:", subtract(a, b))
print("Uppercase:", to_upper(text))
print("Lowercase:", to_lower(text))

