def gcd(a,b):
    if(a==0):
        return b
    if(b==0):
        return a
    if(a==b):
        return a
    if(a>b):
        return gcd(a-b,b)
    
    return gcd(a,b-a)
a=int(input("Enter first number"))
b=int(input("Enter second number"))
if(gcd(a,b)):
    print("Gcd of ",a,"and",b,"=",gcd(a,b))
else:
     print("not found")
    
        
