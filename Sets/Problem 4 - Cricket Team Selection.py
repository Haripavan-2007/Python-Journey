#===============================================
#Problem 4 — Cricket Team Selection
"""
All-rounders
Only batsmen
Only bowlers
At least two skills
Complete squad
Missing fielders
"""
#===============================================
batting={...}
bowling={...}
fielding={...}
#01
print("All-rounders : ",end="")
for player in batting&bowling&fielding:
    print(player,end="")
print()
#02
print("Only batsmen : ",end="")
for player in (batting|bowling|fielding)-(bowling|fielding):
    print(player,end="")
print()
#03
print("Only bowlers : ",end="")
for player in (batting|bowling|fielding)-(batting|fielding):
    print(player,end="")
print()
#04
print("At least two skills : ",end="")
for player in (batting&bowling)|(bowling&fielding)|(batting&fielding):
    print(player,end="")
print()
#05
print("Complete squad : ",end="")
for player in batting|bowling|fielding:
    print(player,end="")
print()
#06
print("Missing fielders : ",end="")
if len(batting|bowling)-fielding:
    print(11-len(batting|bowling|fielding),end="")
print()
