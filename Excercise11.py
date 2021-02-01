string=input("Enter string:")
string=string.lower()
str=list(string.split(" "))
st=list(set(str))
print(st)
for word in st:
    print(word,"=",st.count(word))
