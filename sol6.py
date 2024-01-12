    # TODO: Write a function

def is_leap(year):
    leap = False
    
    if year % 4 == 0 and year % 100 != 0:   # * If the year is divided by 100 then it's not leap
        leap = True
    if year % 400 == 0:         # * But if it's divided by 400 then only it's leap no matter it's divided by 100
        leap = True
    
    return leap

year = int(input())
print(is_leap(year))