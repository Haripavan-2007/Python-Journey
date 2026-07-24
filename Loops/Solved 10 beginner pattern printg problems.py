"""
====================================================
Topic    : Python Pattern Problems
Author   : Haripavan
Date     : 24-07-2026
Language : Python 3
Concepts : for loop, nested loop, pattern printing
Difficulty : Beginner
====================================================

Problems Included
-----------------
1. Solid Square
2. Right Triangle
3. Inverted Triangle
4. Number Triangle
5. Center Pyramid
6. Floyd's Triangle
7. Diamond Pattern
8. Hollow Square
9. Butterfly Pattern
10. Binary Alternating Triangle
"""
# ==================================================
# Problem 01: Solid Square
# ==================================================
n = int(input("Enter value of n: "))
for i in range(n):
    print("* " * n)

# ==================================================
# Problem 02: Right-Angled Triangle
# ==================================================
n = int(input("Enter value of n: "))
for i in range(1, n + 1):
    print("* " * i)

# ==================================================
# Problem 03: Inverted Right-Angled Triangle
# ==================================================
n = int(input("Enter value of n: "))
for i in range(n, 0, -1):
    print("* " * i)

# ==================================================
# Problem 04: Number Triangle
# ==================================================
n = int(input("Enter value of n: "))
for i in range(1, n + 1):
    print((str(i) + " ") * i)

# ==================================================
# Problem 05: Centered Pyramid
# ==================================================
n = int(input("Enter value of n: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# ==================================================
# Problem 06: Floyd's Triangle
# ==================================================
n = int(input("Enter value of n: "))
x = 1
for i in range(1, n + 1):
    for _ in range(i):
        print(x, end=" ")
        x += 1
    print()

# ==================================================
# Problem 07: Diamond Pattern
# ==================================================
n = int(input("Enter value of n: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# ==================================================
# Problem 08: Hollow Square
# ==================================================
n = int(input("Enter value of n: "))
for i in range(n):
    if i == 0 or i == n - 1:
        print("*" * n)
    else:
        print("*" + " " * (n - 2) + "*")

# ==================================================
# Problem 09: Butterfly Pattern
# ==================================================
n = int(input("Enter value of n: "))
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
for i in range(n, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
#=================================================================
#problem10 - Binary Alternating Triangle
#=================================================================
n=int(input("Enter the number : "))
num=True
for i in range(1,n+1):
    for _ in range(i):
        if num==True:
            print(int(num),end="")
            num=False
        else:
            print(int(num),end="")
            num=True
    print()

        
 

