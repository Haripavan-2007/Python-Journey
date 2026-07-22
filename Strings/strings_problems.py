'''
Topic : Strings
Author : Haripavan
Date : 2026/07/22
Problems solved:
1. Reverse a string
2. Palindrome check
3. Count vowels and consonants
4. Character frequency
5. Remove duplicates
6. Most frequent character
7. Count words
8. Reverse sentence
9. Check anagrams
10. Password validation

'''
#---------------------------------------------------
#problem01
#---------------------------------------------------
print("\n========== Problem 01 ==========")
rev=[]
for i in "Python":
    rev.insert(0,i)
print("".join(rev))

#---------------------------------------------------
#problem02
#---------------------------------------------------
print("\n========== Problem 02 ==========")
x="madam"
if x==x[::-1]:
    print("Palindrome")
else:
    print("It's Not")
 
#---------------------------------------------------
#problem03
#---------------------------------------------------
print("\n========== Problem 03 ==========")
x=input("Enter the string")
vowels=["a","e","i","o","u"]
countV=countC=0
for i in x.lower():
    if i in vowels:
        countV+=1
    else:
        countC+=1
print(f"No of Vowels{countV}")
print(f"No of Consenants{countC}")
#it has a logical error

#---------------------------------------------------
#problem04
#---------------------------------------------------
print("\n========== Problem 04 ==========")
x="banana"
unique=[]
for i in x:
    if i not in unique:
        unique.append(i)
for j in unique:
    print(j,"=",x.count(j))

#---------------------------------------------------
#problem05
#---------------------------------------------------
print("\n========== Problem 05 ==========")
x="programming"
unique=[]
for i in x:
    if i not in unique:
        unique.append(i)
print("".join(unique))

#---------------------------------------------------
#problem06
#---------------------------------------------------
print("\n========== Problem 06 ==========")
x="mississippi"
unique=[]
mf=x[0]
for i in x:
    if i not in unique:
        unique.append(i)
for j in unique:
    if x.count(j)> x.count(mf[0]):
        mf=j
    elif x.count(j)== x.count(mf[0]):
        if mf!=j:
            mf=mf+","+j
MF=mf.split(",")
for ch in MF:
    print(ch,"=",x.count(ch))

#---------------------------------------------------
#problem07
#---------------------------------------------------
print("\n========== Problem 07 ==========")
x="I love Python programming"
words=x.split()
print(f"Number of words = {len(words)}")

#---------------------------------------------------
#problem08
#---------------------------------------------------
print("\n========== Problem 08 ==========")
x=str(input("Enter the sentece which have to be reversed - "))
words=x.split()
words.reverse()
print(" ".join(words))

#---------------------------------------------------
#problem09
#---------------------------------------------------
print("\n========== Problem 09 ==========")
#---------------------------------------------------
#method01
#---------------------------------------------------
print("\n========== method 01 ==========")

x1="silent"
x2="listen"
X1=[]
X2=[]
XT1=[]
XT2=[]
for i1 in x1:
    if i1 not in X1:
        X1.append(i1)
X1.sort()
for j1 in X1:
    XT1.append(x1.count(j1))
for i2 in x2:
    if i2 not in X2:
        X2.append(i2)
X2.sort()
for j2 in X2:
    XT2.append(x2.count(j2))
if X1==X2 and XT1==XT2:
    print("anagrams")
else:
    print("is not anagrams")
#---------------------------------------------------
#method02
#---------------------------------------------------
print("\n========== method 02 ==========")
x1="silent"
x2="listen"
if sorted(x1)==sorted(x2):
    print("anagrams")
else:
    print("is not anagrams")
#---------------------------------------------------
#problem10
#---------------------------------------------------
print("\n========== Problem 10 ==========")
pswd=input("Enter the strong password : ")
spchar=["@","#","$","%"]
digitchar=[0,1,2,3,4,5,6,7,8,9]
lnth,up,low,digit,spc=False,False,False,False,False
if len(pswd)>=8:
    lnth=True
for s in spchar:
    if s in pswd:
        spc=True
    pswd=pswd.replace(s,"")
for d in digitchar:
    if str(d) in pswd:
        digit=True
    pswd=pswd.replace(str(d),"")
for u in pswd.upper():
    if u in pswd:
        up=True
for l in pswd.lower():
    if l in pswd:
        low=True
final=lnth*up*low*digit*spc
if final:
    print("Strong Password")
else:
    print("Weak Password")
"""
Note:
These solutions are written using the concepts I have learned so far.
I intentionally avoided advanced built-in functions and modules to strengthen my problem-solving skills.
"""
