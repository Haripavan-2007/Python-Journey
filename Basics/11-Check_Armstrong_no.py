# An Armstrong number is a number that equals the sum of its own digits, 
# where each digit is raised to a power equal to the total number of digits. 
# Common examples include 153, 371, and 1634.
def is_AmstrongNo(n):
    pwer=len(n)
    SP=[int(i)**pwer for i in str(n)]
    print(SP)
    return int(n)==sum(SP)
num=input("Enter the number :")
print(is_AmstrongNo(num))