def calc(x,y,op):
    match op:
        case "+":
            return(x+y)
        case "-":
            return(x-y)
        case "*":
            return(x*y)
        case "/":
            if y!=0: return (x/y) 
num1=int(input("Enter the first number : "))
num2=int(input("Enter the second number : "))
operator=input("Enter the operator : ")
print(calc(num1,num2,operator))