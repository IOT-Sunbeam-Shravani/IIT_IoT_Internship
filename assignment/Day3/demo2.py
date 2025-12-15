#user input
a = input("enter a string")
print("First 3 character: ",a[0:3])
print("Characters from index 2 to a:",a[2:6])

# Slicing without start or end
a = input("enter a string: ")
print("From beginning to index 4:", a[:5])
print("From index 3 to end:",a[3:])

#negative index slicing
a = input("enter a string: ")
print("last 4 characters"),a[-4:]
print("String without last character:",a[:-1])

#step value in slicing
a = input("enter a string: ")
print("reverse string:",a[::-1])

#extract middle part
a = input("enter a string: ")
mid = len(a) //2
print("Middle character:", a[mid])



