#===============================================
#Problem 9 — University Result System
#Results(Pass/Fail)
#Class Average
#Topper
#Failed Students
#Passed Students
#===============================================
print("Problem 9 — University Result System")
students={
"Hari":{"Math":90,"Physics":85,"Programming":95},
"John":{"Math":35,"Physics":75,"Programming":65},
"Kamal":{"Math":88,"Physics":92,"Programming":91},
"Alex":{"Math":40,"Physics":38,"Programming":42}
}
rep=0
clz_avg_total=0
std_avg=0
topper=""
top_avg=0
pass_sub=0
results={}
for name in students:
    rep+=1
    for sub in students[name]:
        if students[name][sub]<40:
            pass_sub-=1
        else:
            pass_sub+=1
    if pass_sub==3:
        print(name,"-","Pass")
        results.update({name:"Pass"})
    else:
        print(name,"-","Fail")
        results.update({name:"Fail"})
    pass_sub=0
    std_avg=sum(students[name].values())/len(students[name])
    if std_avg>top_avg:
        top_avg=std_avg
        topper=name
    clz_avg_total=clz_avg_total+std_avg
    std_avg=0
print("Class average : ",clz_avg_total/len(students))
print("Class Topper : ",topper)
print("Failed students : ",end=" ")
for i in results:
    if results[i]=="Fail":
        print(i,end=",")
print()
print("Passed students : ",end=" ")
for i in results:
    if results[i]=="Pass":
        print(i,end=",")
