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
    print ("day of year: %d is_leap: %r" % (day_sum, is_leap(year)))
    return day_sum

def date_diff(day1,day2):
    day1 = [str(e) for e in day1.split("-")]
    day2 = [str(e) for e in day2.split("-")]

    year_cal = int(day2[2])- int(day1[2])
    first_year=int(day1[2])
    second_year=int(day2[2])
    count1 = day_of_year(day1[0],day1[1],first_year)
    count2 = day_of_year(day2[0],day2[1],second_year)
    day_cal = count2 - count1 +1

    final_cal=day_cal
    while second_year > first_year:
        if first_year % 4 == 0:
            final_cal += 366
            first_year += 1
        else:
            final_cal += 365
            first_year += 1
    


    return final_cal



value = input()
# value = ("14-8-1905,5-1-2000")
value =[str(e) for e in value.split(",")]
output = date_diff(value[0],value[1])
print(output)