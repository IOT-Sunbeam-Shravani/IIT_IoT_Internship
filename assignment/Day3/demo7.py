#  to find factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# to find power
def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)


# Testing the functions
num = 5
print("Factorial of", num, "is:", factorial(num))

b = 2
e = 3
print(b, "power", e, "is:", power(b, e))