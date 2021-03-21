f=open('numbers.txt','r')
f1=open('odd.txt','w')
f2=open('even.txt','w')
li=[i for i in f.readline().split()]
for i in li:
    if int(i)%2==0:
        f2.write(str(i)+" ")
    else:
        f1.write(str(i)+" ")
       
f.close()
f1.close()
f2.close()
