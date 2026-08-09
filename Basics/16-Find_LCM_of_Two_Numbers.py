#method 01
def LCM(x,y):
    x,y=min(x,y),max(x,y)
    t=1
    multiplesOfY=[y]
    while True:
        X=x*t
        if X in multiplesOfY:
            return X
        else:
            multiplesOfY.append(y*(t+1))    
        t+=1
#method 02
def lcm(x, y):
    greater = max(x, y)

    while True:
        if greater % x == 0 and greater % y == 0:
            return greater
        greater += 1
#method 03
def gcd(a,b):
    a,b=b,a%b
    return a if not b else gcd(a,b)
def lcmBYgcd(x,y):
    return (x*y)//gcd(x,y)
def main():
    num1=int(input("Enter no1 :"))
    num2=int(input("Enter no2 :"))
    print(LCM(num1,num2))
    print(lcm(num1,num2))
    print(lcmBYgcd(num1,num2))
main()


        
