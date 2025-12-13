str = input("Enter string : ")
len = 0
for ch in str:
    len+=1
    
    print(f"length = {len}")
    
def strlen(str):
       len=0
       for ch in str:
           len+=1
           return len
       str= input("enter string : ")
       len=0
       for ch in str:
           len+=1
           return len
       str=input("enter string:")
       len=strlen(str)
       print(f"length={len}")