class bank:
     def __init__(self,name,acc,type,bal):
         self.name=name
         self.acc_no=acc
         self.acc_type=type
         self.balence=bal
     def deposit(self,amt):
         self.balence+=amt
         print(amt,"credited.Account balence is",self.balence)
     def withdraw(self,amt):
         if(self.balence>amt):
             self.balence-=amt
             print(amt,"deducted.Account balence is",self.balence)
         else:
             print("Not enough balence in account")
     def display(self):
          print("Name:",self.name)
          print("Account Number:",self.acc_no)
          print("Account balence:",self.balence)
          print("Account type:",self.acc_type)
n=input("Enter the name of account holder")        
t=input("Enter the type of account")
no=int(input("Enter account number"))
bal=int(input("Enter account balence"))
print("Menu\n1.Deposit Cash\n2.Withdraw Cash\n3.Display Details\n4.Exit\n")
b=bank(n,no,t,bal)
while(True):
    choice=int(input("Enter choice"))
    if choice==1:
        amt=int(input("Enter amount to be deposited:"))
        b.deposit(amt)
    elif choice==2:
        amt=int(input("Enter amount to be withdrawn:"))
        b.withdraw(amt)
    elif choice==3:
        b.display()
    elif choice==4:
          break
    else:
        print("Wrong choice")
