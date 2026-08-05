#The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. 
# Starting from zero and one, the sequence begins:
#  0, 1, 1, 2, 3, 5, 8, 13, 21, 34, and continues infinitely.
#Method 01 -(first try)
limit=int(input("Enter the number : "))
sequence=[0,1]
print(0,end=",")
print(1,end=",")
x=1
count=1
while count<=limit-2:
    x=sequence[-1]+sequence[-2]
    print(x,end=",")
    sequence.append(x)
    count+=1
print("....")
#Method 02 - improved
def fibonacci(n):
    x,y=0,1
    for _ in range(n):
        print(x,end=",")
        x,y=y,x+y
    print("....")
fibonacci(limit)
