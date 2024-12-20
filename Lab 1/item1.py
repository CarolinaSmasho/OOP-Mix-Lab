def cal(value):
    if value.isnumeric() == False or int(value) > 9:
        return "Invalid"
    value1 = int(value)
    value2 = int(value * 2)
    value3 = int(value *3)
    value4 = int(value*4)
    return value1 + value2 + value3 +value4

value = input()
output = cal(value)
print(output)