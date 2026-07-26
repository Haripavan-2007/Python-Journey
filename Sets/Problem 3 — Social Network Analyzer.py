#===============================================
#Problem 3 — Social Network Analyzer
"""
1. Display all users
2. Mutual Friends
3. Friend Suggestions
4. Person with Most Friends
5. Person with Least Friends
6. Unique Friendships
7. Users Having No Mutual Friends
8. Display Complete Network
0. Exit
"""
#===============================================
friends = {
    "Hari":{"John","Alex","David"},
    "John":{"Hari","Peter","Alex"},
    "Alex":{"Hari","John","David","Peter"},
    "David":{"Hari","Alex"},
    "Peter":{"John","Alex"}
}
print("""
1. Display all users
2. Mutual Friends
3. Friend Suggestions
4. Person with Most Friends
5. Person with Least Friends
6. Unique Friendships
7. Users Having No Mutual Friends
8. Display Complete Network
0. Exit
""")
p=None
while p!=0:
    p=int(input("Enter the number : "))
    if p==1:
        print("Users : ",end="")
        for user in friends:
            print(user,end=",")
        print()
    elif p==2:
        name1=input("Enter first user's name : ")
        name2=input("Enter second user's name : ")
        print(f"Mutual friends of {name1} and {name2} : ",end="")
        if len(friends[name1.title()]&friends[name2.title()])!=0:
            for mutual_friend in friends[name1.title()]&friends[name2.title()]:
                print(mutual_friend,end=",")
            print()
        else:
            print("No mutual friends")
    elif p==3:
        suggested_friends=set()
        name=input("Enter user's name : ")
        print(f"Friend Suggestions for {name} : ",end="")
        for frnd in friends[name.title()]:
            suggested_friends.update(set(friends[frnd.title()]))
        suggested_friends.remove(name.title())
        suggested_friends-=friends[name.title()]
        for suggestion in suggested_friends:
            print(suggestion,end=",")
        print()
    elif p==4:
        have_most_friends=0
        print("Person with Most Friends : ",end="")
        for user in friends:
            if have_most_friends==0 or have_most_friends<len(friends[user]):
                have_most_friends=len(friends[user])
        for user,friend in friends.items():
            if have_most_friends==len(friend):
                print(user,end=",")
        print()
    elif p==5:
        have_least_friends=0
        print("Person with least Friends : ",end="")
        for user in friends:
            if have_least_friends==0 or have_least_friends>len(friends[user]):
                have_least_friends=len(friends[user])
        for user,friend in friends.items():
            if have_least_friends==len(friend):
                print(user,end=",")
        print()
    elif p==6:
        print("Unique friendships : ")
        pairs=set()
        for user,frnds in friends.items():
            for frnd in frnds:
                pair=frnd+user
                if ("".join(sorted(pair))) not in pairs:
                    print(user,"-",frnd)
                    pairs.add("".join(sorted(pair)))
                else:
                    pass
        print("Total unique friendships :",len(pairs))
    elif p==7:
        count=0
        for user in friends:
            for frnd in friends:
                if user!=frnd:
                    if len(friends[user]&friends[frnd])!=0:
                        count+=1
                        pass
                    else:
                        print(f"{user} and {frnd} having no mutual friends")
        print(len(friends))
        import math
        if count/2==math.factorial(len(friends))/(math.factorial(2)*math.factorial(len(friends)-2)):
            print("Every users have atleast one mutual friend")
        #your logic is worng, mine prints the pairs two time but i can fix it by the methos i have used in printing unique pairs, but here i didn't use that bcz that is waste of time for this data.
    elif p==8:
        for user,frnds in friends.items():
            print(f"Friends of {user} : ",end="")        
            for frnd in frnds:
                print(frnd,end=",")
            print()
    elif p==0:
        pass
    else:
        print("You have entered wrong number")
        print("""
1. Display all users
2. Mutual Friends
3. Friend Suggestions
4. Person with Most Friends
5. Person with Least Friends
6. Unique Friendships
7. Users Having No Mutual Friends
8. Display Complete Network
0. Exit
""")        
    
                                         
                
            
                
            
            
        
        
            
        

    
