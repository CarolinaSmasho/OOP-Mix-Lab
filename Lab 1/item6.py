def find_max_multiply(lst):
    lst = lst.replace('[','')
    lst = lst.replace(']','')

    for x in lst.split(','):
        try:
            x = int(x)
        except ValueError:
            return "Invalid"


    lst = [int(e) for e in lst.split(',')]

    max = x
    a,b = 0,0
    for x in lst:
        a += 1
        for y in lst:
            b += 1
            if  a != b and x*y > max: 
                
                max = x*y

        b = 0

    if max == 0 or len(lst) <= 1:
        return "Invalid"

    return max


lst = input()
output = find_max_multiply(lst)
print(output)