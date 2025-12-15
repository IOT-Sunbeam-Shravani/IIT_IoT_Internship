def add(a,b):
    return a+b

def substract(a,b):
    return a-b

def Multiply(a,b):
    return a*b

def Divide(a,b):
    if b == 0:
        return "Error! Division by zero"
    return a/b

while True:
    
    print("\n---Menu ---")    
    print("1.addition")                                                  
    print("2.Substraction")
    print("3.Multiplication")
    print("4.Divison")
    print("5.Exit")
            
#main program

   
    choice = int(input("Enter your choice (1-5): "))
    if choice == 5:
        print("program terminated")
        break
    
    if choice >= 1 and choice <= 4:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        
        if choice == 1:
            print("result:",add(a,b))
            
        elif choice == 2:
            print("result:",substract(a,b))


        elif choice == 3:
            print("result:",Multiply(a,b))


        elif choice == 4:
            print("result:",Divide(a,b))
        else:
            print("Invalid choice!please try again")


