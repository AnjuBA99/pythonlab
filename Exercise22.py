class Rectangle:
    __length=0
    __width=0
    def __init__(self,l,b):
        self.__length=l
        self.__width=b
    def areaRect(self):
        return self.__length*self.__width
    def __lt__(self,rect2):
        area1=self.areaRect()
        area2=rect2.areaRect()
        if area1<area2:
            return True
        else:
            return False
l=int(input("Enter l of rectangle1:"))
b=int(input("Enter b of rectangle1:"))
r1=Rectangle(l,b)
l=int(input("Enter l of rectangle2:"))
b=int(input("Enter b of rectangle2:"))
r2=Rectangle(l,b)

if r1<r2:
    print("Rectangle1 is of lesser area than rectangle2")
else:
    print("Rectangle1 is of equal or greater than area than rectangle2")
    
    
        
