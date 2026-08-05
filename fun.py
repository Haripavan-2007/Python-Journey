import math as something

print(f"hey pi is {something.pi}")
input("Press enter to continue")
a = int(input("Enter a number: "))
if a < 0 or a > 1:
    print("Invalid input")
else:
    a = 1 - a**2
    print(f"The result is {something.sqrt(a)}")

title = input("Enter a good title for this program: ")