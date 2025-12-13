def add(a,b):
    return a+b
def substract (a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Division by zero is not allowed."
    return a/b
while True:
    print("\n---Calculator Menu ---")
    print("1.Addition")
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 5:
        print("Exiting calculator...")
        break
    if choice>=1 and choice<=4:
        x=float(input("Enter first number: "))
        y=float (input ("Enter second number: "))
        if choice == 1:
            print("result:",add(x,y))
        elif choice == 2:
            print("result:",substract(x,y))
        elif choice==3:
            print("result:",multiply(x,y))
        elif choice==4:
            print("result:",divide(x,y))
        else:
            print("invalid choice!please try again.")
        