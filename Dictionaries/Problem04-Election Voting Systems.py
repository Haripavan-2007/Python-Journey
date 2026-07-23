#===============================================
#Problem 4 — Election Voting System
#===============================================
print("Problem 4 — Election Voting System")
votes=[
"Hari",
"John",
"Hari",
"Kamal",
"Hari",
"John",
"Kamal",
"Kamal",
"Kamal"
]
count={}
winner=""
x=0
for cand in votes:
    if cand in count:
        count[cand]+=1
    else:
        count[cand]=1
for name,num in count.items():
    print(name,"-",num)
    if num>x:
        winner=name
	x=num
print("Winner - ",winner)
