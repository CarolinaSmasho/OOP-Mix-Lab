def toll_calculate(value):
    for e in value.split():
        if e.isnumeric() == False:
            return "Invalid"
    h1,m1,h2,m2 = [int(e) for e in value.split()]
    entry = (h1 * 60)+m1
    exit = (h2 * 60) + m2
    minute = exit - entry
    Hourtoll = int(minute/60)

    if (h1<7 or h1>23) or (m1<0 or m1>59) or (h2<7 or h2>23) or (m2<0 or m2>59):
        return "Invalid"

    if minute%60 != 0:
        Hourtoll+=1

    if entry<420:
        return "Invalid"
    elif exit>23*60:
        return "Invalid"

    if minute <= 15:
        toll = 0
    elif Hourtoll<3:
        toll = Hourtoll*10
    elif Hourtoll<6:
        toll = 30 + (Hourtoll-3)*20
    elif Hourtoll>=6:
        toll = 200
    if minute< 0:
        return "Invalid"

    return toll
    
value = input()
output = toll_calculate(value)
print (output)