#===============================================
#Problem 2 — Employee Skill Analyzer
"""
Display
Employees with Python
Employees with both Python and C
Employees with only one skill
Most common skill
Least common skill
Unique skills
Employee with maximum skills
"""
#===============================================
employees = {
"Hari":{"Python","C","SQL"},
"John":{"Java","SQL"},
"Kamal":{"Python","Java","C"},
"Alex":{"Python","HTML"}
}
print("Employees with Python :",end="")
for employee,skils in employees.items():
    if "Python" in skils:
        print(employee,end=",")
print()
print("Employees with both Python and C :",end="")
for employee,skills in employees.items():
    if "Python" in skills and "C" in skills:
        print(employee,end=",")
print()
print("Employees with only one skill :",end="")
for employee,skills in employees.items():
    if len(skills)==1:
        print(employee,end=",")
print()
skills_frequency=dict()
for skills in employees.values():
    for skill in skills:
        if skill in skills_frequency:
            skills_frequency[skill]+=1
        else:
            skills_frequency[skill]=1
print("Most common skill :",end="")
most_common_skill=""
for skill in skills_frequency:
    if most_common_skill=="" or skills_frequency[skill]>skills_frequency[most_common_skill]:
        most_common_skill=skill
print(most_common_skill)
print("Least common skill :",end="")
least_common_skill=""
for skill in skills_frequency:
    if least_common_skill=="" or skills_frequency[skill]<skills_frequency[least_common_skill]:
        least_common_skill=skill
print(least_common_skill)
print("Unique skills :",end="")
for skill in skills_frequency:
    print(skill,end=",")
print()
print("Employee with maximum skills :",end="")
HNS=0
for skills in employees.values():
    if len(skills)>HNS:
        HNS=len(skills)
for employee,skills in employees.items():
    if len(skills)==HNS:
        print(employee,end=",")
print()

