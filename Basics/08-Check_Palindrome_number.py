def is_palindrom(n):
    if str(n)==str(n)[::-1]:
        return True
def main():
    num=int(input("Enter the number : "))
    print(is_palindrom(num))
main()
