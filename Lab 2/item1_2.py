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
    day_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
    day_sum = 0

    if is_leap(year):
        day_in_month[1] = 29

    for x in range(month-1):
        # print(day_in_month[x])
        day_sum += day_in_month[x]

    day_sum += day

    # return day_sum
    return ("day of year: %d is_leap: %r" % (day_sum, is_leap(year)))





value = input()
# value = ("1/3/2023")
value =[str(e) for e in value.split("/")]
output = day_of_year(value[0],value[1],value[2])
print(output)