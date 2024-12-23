def is_leap(year):
    year = int(year)
    if year % 4 == 0:
        return True
    else:
        return False

def day_of_year(day, month, year):
    day = int(day)
    month = int(month)
    year = int(year)
    day = 0

    

    day_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    for x in range(month-1):
        # print(day_in_month[x])
        day += day_in_month[x]
    return day





# value = input()
value = ("15/13/2024")
value =[str(e) for e in value.split("/")]
output = day_of_year(value[0],value[1],value[2])
print(output)