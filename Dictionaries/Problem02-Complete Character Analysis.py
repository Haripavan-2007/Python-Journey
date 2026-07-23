#===============================================
#Problem 2 — Complete Character Analysis
#Frequency of each character
#Most frequent character
#Least frequent character
#First repeating character
#First non-repeating character
#All unique characters
#I think this is long way
#===============================================
print("Problem 2 — Complete Character Analysis")
x="engineering"
seen={}
freq={}
higst_freq=""
lowst_freq=""
for ch in x:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
for i in freq:
    print(f"Frequency of {i} - ",freq[i])
    if higst_freq=="" or freq[higst_freq]<freq[i]:
        higst_freq=i
    if lowst_freq=="" or freq[lowst_freq]>freq[i]:
        lowst_freq=i
print("Most frequent character - ",higst_freq)
print("Least frequent character - ",lowst_freq)
for j in x:
    if j in seen:
        print(f'First repeating character - {j}')
        break
    else:
        seen.update({j:0})
for k in x:
    if freq[k]==1:
        print(f"First non repeating character - {k}")
        break
print("Unique characters - ",end="")
for l in freq:
    print(l,end=",")
