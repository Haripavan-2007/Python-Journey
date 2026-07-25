#======================================================
#Problem01-University Cource Summary
'''
Display
Students taking all three subjects
Students taking only Math
Students taking Math & Physics only
Students taking exactly one subject
Students taking at least two subjects
Total unique students
Students who didn't take Programming
'''
#======================================================
math = {"Hari","John","Kamal","Alex"}
physics = {"Hari","Kamal","David"}
programming = {"Hari","John","David","Peter"}
print("Student's summary")
print("Students taking all three subjects : ",end="")
for i in math&physics&programming:
    print(i,end=",")
print()
print("Students taking only Math : ",end="")
for i in math-(physics|programming):
    print(i,end=",")
print()
print("Students taking Math & Physics only : ",end="")
for i in (math&physics)-programming:
    print(i,end=",")
print()
print("Students taking exactly one subject : ",end="")#is there any simple method for this using ^
for i in (math|physics|programming)-((math&physics)|(physics&programming)|(math&programming)):
    print(i,end=",")
print()
print("Students taking at least two subjects : ",end="")
for i in (math&physics)|(physics&programming)|(math&programming):
    print(i,end=",")
print()
print("Total unique students : ",end="")
print(math|physics|programming)
print()
print("Students who didn't take Programming : ",end="")
for i in (math|physics)-programming:
    print(i,end=",")
print()
