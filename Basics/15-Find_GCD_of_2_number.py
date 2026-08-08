#The GCD (Greatest Common Divisor), also called the Highest Common Factor (HCF), 
# is the largest positive whole number that divides evenly into two or more numbers without leaving a remainder. 
# For example, the GCD of 12 and 18 is 6
#method01
def GCD(x,y):
    d=1
    gcd=1
    d=x if x<y else y
    for i in range(1,d+1):
        if x%i==0 and y%i==0:
            if gcd<i : gcd=i
    return gcd
num1=int(input("Enter the first no : "))
num2=int(input("Enter the second no : "))
#method02
def gcd(a,b):
    a,b=b,a%b
    return a if not b else gcd(a,b)
print(GCD(num1,num2))
print(gcd(num1,num2))

