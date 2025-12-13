def fabonnaci(n):
    a,b=0,1
    print("fabonnaci series:")
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
        n=int(input("\nenter the number of terms:"))
        fabonnaci(n)
       
   