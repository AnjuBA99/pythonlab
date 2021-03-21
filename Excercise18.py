a=int(input("Enter the side of a square"))
areasquare=lambda x:x**2
print("Area of square is %d" %areasquare(a))
l,b=[int(i) for i in input("Enter length and breadth of a rectangle").split()]
areaRect=lambda x,y:x*y
print("area of rectangle is %d"%areaRect(l,b))
b,h=[int(i) for i in input("enter base and height of a triangle").split()]
areaTriangle=lambda x,y:x*y*0.5
print("area of triangle is %d"%areaTriangle(b,h))













      
