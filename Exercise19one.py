import graphics
from graphics import circle,rect
from graphics.threeD import sphere,cuboid
l,b=[int(i) for i in input("Enter length and breadth of a rectangle").split()]
r=int(input("Enter radius of circle"))
print("Area of rectangle is ",rect.area(l,b))
print("Perimeter of rectangle is",rect.perimeter(l,b))
print("Area of circlr is",circle.area(r))
print("perimeter of circle is",int(circle.perimeter(r)))
l,b,h=[int(i) for i in input("Enter length breadth and height of a cuboid").split()]
r=int(input("Enter radius of sphere"))
print("area of cuboid is",cuboid.area(l,b,h))
print("Volume of cuboid is",cuboid.volume(l,b,h))
print("Area of sphere is",sphere.area(r))
print("Volume of sphere is",sphere.volume(r))

      
