#===============================================
#Problem 7 — Banking System
#1 - Deposit
#2 - Withdraw
#3 - Transfer
#4 - Balance
#0 - Exit
#===============================================
print("Problem 7 — Banking System")
accounts={
"Hari":25000,
"John":18000,
"Kamal":50000
}
p=None
print("""
1 - Deposit
2 - Withdraw
3 - Transfer
4 - Balance
0 - Exit
""")
while p!=0:
    p=int(input("Enter the no : "))
    if p==1:
        name=input("Enter your account name : ")
        if name in accounts:
            amount=int(input("Enter the amount to deposit : "))
            if amount>0:
                accounts[name]+=amount
                print("Deposit succes")
            else:
                print("Invalid amount")
        else:
            print("Invalid account name")
    elif p==2:
        name=input("Enter your account name : ")
        if name in accounts:
            amount=int(input("Enter the amount to withdraw : "))
            if amount>0 and amount<=accounts[name]:
                accounts[name]-=amount
                print("withdrawal succes")
            else:
                print("Invalid amount")
        else:
            print("Invalid account name")
    elif p==3:
        name=input("Enter your account name : ")
        res_name=input("Enter resievers account name : ")
        if name in accounts and res_name in accounts and name!=res_name:
            amount=int(input("Enter the amount to transfer : "))
            if amount>0 and amount<=accounts[name]:
                accounts[name]-=amount
                accounts[res_name]+=amount
                print("transaction succes")
            else:
                print("Invalid amount")
        else:
            print("Invalid account name")
    elif p==4:
        name=input("Enter your account name : ")
        if name in accounts:
            print("Your balance is : ",accounts[name],"LKR")
    elif p==0:
        pass
    else:
        print("You have entered invalid number")
        print("""
1 - Deposit
2 - Withdraw
3 - Transfer
4 - Balance
0 - Exit
""")
