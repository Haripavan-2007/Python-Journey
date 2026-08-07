#Method01
def find_SOD(n):
    total=0
    for i in n:
        total+=int(i)
    return total
#Method02(Using sum)
def find_sod(n):
    return sum([int(i) for i in n])
num=input("Enter the number : ")
print(find_SOD(num))
print(find_sod(num))

