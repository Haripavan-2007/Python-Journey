#Method01(First try)
def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
def main():
    num=int(input("Enter the number : "))
    print(factorial(num))
main()
#Method(using recursion)
num=int(input("Enter the number : "))
def factorial1(n):
    return 1 if n==0 else n*factorial1(n-1) 
print(factorial1(num))



