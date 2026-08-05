num=int(input("Enter the number : "))
is_prime=True
if num==1: is_prime=False
for i in range(2,num//2+1):
    if not num%i :
        is_prime= False
        break
print("Prime number") if is_prime else print("Not a Prime number")
