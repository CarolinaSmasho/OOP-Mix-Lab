def cal(value):
    max = 0
    if not value.isascii() or not value.isdigit() or not 2 <= int(value) <= 3:
        return "Invalid"
    
    if 2 <= int(value) <= 3:
        strformat = '9'*int(value)
        num = int(strformat)

        for x in range(1,num+1):
            for y in range(1,num):
                palindome = (str(x*y) == str(x*y)[::-1])
                if x*y > max and palindome == True:
                    max = x*y

        return max
    
    return "Invalid"


value = input()
output = cal(value)
print(output)
