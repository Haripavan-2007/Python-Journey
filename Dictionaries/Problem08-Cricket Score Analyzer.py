#===============================================
#Problem 8 — Cricket Score Analyzer
#Highest scorer
#Lowest score
#Average
#Players above average
#Players below average
#===============================================
print("Problem 8 — Cricket Score Analyzer")
runs={
"Virat":80,
"Rohit":45,
"Gill":102,
"Rahul":30,
"Hardik":67
}
H_scorer=""
L_scorer=""
avg=sum(runs.values())/len(runs)
above_avg=[]
below_avg=[]
for player in runs:
    if H_scorer=="" or runs[H_scorer]<runs[player]:
        H_scorer=player
    if L_scorer=="" or runs[L_scorer]>runs[player]:
        L_scorer=player
    if runs[player]>avg:
        above_avg.append(player)
    else:
        below_avg.append(player)
print("Highest scorer : ",H_scorer)
print("Lowest scorer : ",L_scorer)
print("Average runs : ",avg)
print("Above average players : ",end="")
for i in above_avg:
    print(i,end=",")
print()
print("Below average players : ",end="")
for i in below_avg:
    print(i,end=",")
print()
