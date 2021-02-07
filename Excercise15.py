def fact(n):
    f=1
    for i in range(1,n+1):
        f=i*f
    print("factorial =%d"%(f))
n=int(input("Enter a number"))    
fact(n)    
    
