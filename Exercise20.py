class rect:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def areaRect(self):
        return self.l*self.b
    def perimeterRect(self):
        return 2*(self.l+self.b)
l=int(input("Enter length of rectangle1:"))
b=int(input("Enter breadth of rectangle1:"))
r1=rect(l,b)
area1=r1.areaRect()
print("Area of Rectangle1",area1)
l=int(input("Enter length of rectangle2:"))
b=int(input("Enter breadth of rectangle2:"))
r2=rect(l,b)
area2=r2.areaRect()
print("Area of Rectangle2",area2)
if area1>area2:
    print("Area1 is greater")
elif area1==area2:
    print("Area1 is equal to Area2")
else:
    print("Area2 is greater")
print("Perimeter of Rectangle1 is",r1.perimeterRect(),"\nPerimeter of Rectangle2 is",r2.perimeterRect())    
    
    

        
