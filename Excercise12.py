diction={ }
n=int(input("Enter the number of elements in dictionary"))
for i in range(n):
    diction[i]=input("Enter element")
asc=sorted(diction.values())
print(asc)
asc.reverse()
print(asc)
