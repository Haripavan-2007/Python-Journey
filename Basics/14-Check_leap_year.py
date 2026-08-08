#Normal_check
def check_leap(y):
    return True if not y%4 else False
year=int(input("Enter the year : "))
print(check_leap(year))
#Precise_check
def check_leap_p(y):
    if y%4==0:
        if y%100==0:
            if y%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
year=int(input("Enter the year : "))
print(check_leap(year))
print(check_leap_p(year))