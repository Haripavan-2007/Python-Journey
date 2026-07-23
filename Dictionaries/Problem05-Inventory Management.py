#===============================================
#Problem 6 — Library System
#1 - Borrow
#2 - Return
#3 - Check availability
#4 - Display all books
#0 - Exit
#===============================================
print("Problem 6 — Library System")
books={
"Python":3,
"Java":2,
"C++":5
}
p=None
print("""
1 - Borrow
2 - Return
3 - Check availability
4 - Display all books
0 - Exit
""")
while p!=0:
    p=int(input("Enter the no : "))
    if p==1:
        print("you can borrow one book at a time")
        book=input("Enter book's name : ")
        if book in books and books[book]!=0:
            books[book]-=1
            print("Book has been borrowed sucessfully")
        else:
            print("check availablity")
    elif p==2:
        print("you can return one book at a time")
        book=input("Enter book's name : ")
        books[book]+=1
        print("Book has been returned sucessfully")
    elif p==3:
        book=input("Enter book's name : ")
        if book not in books :
            print("It's currently unavailable")
	elif books[book]>0:
		print("Book not found")
	else :
		print("Available")
    elif p==4:
        for book,count in books.items():
            print(book,"-",count)
    elif p==0:
        pass
    else:
        print("you have entered invalid no")
        print("""
1 - Borrow
2 - Return
3 - Check availability
4 - Display all books
0 - Exit
""")
