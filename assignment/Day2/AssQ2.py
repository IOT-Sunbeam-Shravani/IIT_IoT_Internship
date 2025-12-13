num=input("enter a 5 digit number:")
if num.isdigit() and len(num)==5:
    if num==num[::-1]:
        print(f"{num} is a polindrome")
    else:
        print(f"{num} is not a polindrome")
else:
        print(f"please enter a valid 5 digit number")
        