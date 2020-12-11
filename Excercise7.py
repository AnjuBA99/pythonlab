y=int(input("Enter a year to check leap year or not"))
if y%400==0 or (y%100!=0 and y%4==0):
    print("y is aleap year")
else : 
    print("y is not a leap year")
    
