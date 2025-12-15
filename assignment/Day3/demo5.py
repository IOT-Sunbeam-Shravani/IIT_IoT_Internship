#Default parameter

def gret(name="User"):
    print("Hello",name)
    
gret("Shravani")
gret()

# keyword arguments

def student_info(name,age,course):
    print("Name:",name)
    print("Age:",age)
    print("Course:",course)
                                                     
    student_info(age=20,course ="python",name ="Shravani")
    
# Default+Keyword Argument Together

def power(base,exponent=2):
    return base ** exponent

print(power(5))
print(power(base=2, exponent=3))

#passing function to another function
# demo 1
def add(a,b):
    return a+b
def operates(func,x,y):
    return func(x,y)

result = operates(add,10,20)
print("Result:",result)

#demo2
def add(a,b):
    return a+b
def multiply(a,b):
    return a*b

def calculate(operation, a, b):
    
    print(calculate(add,5,3))
    print(calculate(multiply,5,3))


    