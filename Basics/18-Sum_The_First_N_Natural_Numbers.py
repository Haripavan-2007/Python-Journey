#method 01
def sumOfNnatural(n):
    total=0
    for i in range(1,n+1):
        total+=i
    return total
#method 01
def sumofnnatural(n):
    return n*(n+1)//2
def main():
    n=int(input("Enter n: "))
    print(sumOfNnatural(n))
    print(sumofnnatural(n))
main()
