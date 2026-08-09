def printTable(n):
    for i in range(1,n+1):
        print(f"{n}x{i}={n*i}")
def main():
    number=int(input("Enter the no: "))
    printTable(number)
main()