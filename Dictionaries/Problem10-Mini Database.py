#===============================================
#Problem 10 — Mini Database
#1 Display Employees
#2 Search by ID
#3 Search by Department
#4 Highest Salary
#5 Lowest Salary
#6 Change Salary
#7 Add Employee
#8 Delete Employee
#9 Average Salary
#9 Exit
#===============================================
print("Problem 10 — Mini Database")
employees={
101:{
"name":"Hari",
"department":"Engineering",
"salary":50000
},
102:{
"name":"John",
"department":"IT",
"salary":45000
},
103:{
"name":"Kamal",
"department":"Engineering",
"salary":60000
}
}
print("""
1 Display Employees
2 Search by ID
3 Search by Department
4 Highest Salary
5 Lowest Salary
6 Change Salary
7 Add Employee
8 Delete Employee
9 Average salary
10 Exit
""")
p=None
total=0


while p!=10:
    p=int(input("Enter the number : "))
    if p==1:
        for ID in employees:
            print(employees[ID]["name"])
    elif p==2:
        data=int(input("Enter the ID :"))
        if data in employees:
            print(employees[data]["name"])
        else:
            print("Invalid ID")
    elif p==3:
        data=input("Enter the Department :")
        for ID in employees:
            if data==employees[ID]["department"]:
                print(employees[ID]["name"])
    elif p==4:
        for ID in employees:
            high_salary_ID=""
            if high_salary_ID=="" or employees[ID]["salary"]>employees[high_salary_ID]["salary"]:
                high_salary_ID=ID
        print(employees[high_salary_ID]["name"],"is earning high salary -",employees[high_salary_ID]["salary"])
        high_salary_ID=0
    elif p==5:
        for ID in employees:
            low_salary_ID=""
            if low_salary_ID=="" or employees[ID]["salary"]<employees[low_salary_ID]["salary"]:
                low_salary_ID=ID
        print(employees[low_salary_ID]["name"],"is earning high salary -",employees[low_salary_ID]["salary"])
        low_salary_ID=0
    elif p==7:
        ID=int(input("Enter new employee's ID : "))
        n=input("Enter his name : ")
        d=input("Enter his department : ")
        s=int(input("Enter his salary : "))
        employees.update({ID:{"name":n,"department":d,"salary":s}})
        print("Employee added sucessfully")
    elif p==6:
        ID=int(input("Enter employee's ID : "))
        s=int(input("Enter his new salary : "))
        employees[ID]["salary"]=s
        print("Salary changed sucessfully")
    elif p==8:
        ID=int(input("Enter his ID : "))
        employees.pop(ID)
        print("Employee has been deleted sucessfully")
    elif p==9:
        for ID in employees:
            total+=employees[ID]["salary"]
        print("Average salray : ",total/len(employees))
        total=0
    elif p==10:
        pass
    else:
        print("You have enteres invalid number")
        print("""
1 Display Employees
2 Search by ID
3 Search by Department
4 Highest Salary
5 Average Salary
6 Change Salary
7 Add Employee
8 Delete Employee
9 Exit
""")
    
        
    
    
        
        
    
