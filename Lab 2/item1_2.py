def day_of_year(day, mont, year):
    return 0





def is_leap(year):
    year = int(year)
    if year % 4 == 0:
        return True
    else:
        return False


value = input()
output = is_leap(value)
print(output)