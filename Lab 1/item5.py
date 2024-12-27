def sort_num (List):
    
    List =[int(e) for e in List.split()]
    sort= []
    smallest =10
    while(len(List)>0):
        for i in range(len(List)):
            if List[i] < 0 or List[i] > 9:
                return "Invalid" 

            if List[i]<=smallest:
                smallest=List[i]
                smallestind=i
                
        sort.append(List[smallestind])
        del List[smallestind]
        smallest = 10
    return handle_zero(sort)

def handle_zero(List):
    if len(List) > 10:
        return "Invalid"
    zeronum = 0
    for num in List:
        if num == 0:
            zeronum +=1

    if zeronum == len(List):
        return "Invalid"


    temp = List[0]
    List[0] = List[zeronum]
    List[zeronum] = temp
    text = "".join(str(x) for x in List)
    return text
    

List = input()
try:
    output = sort_num(List)
except:
    print ("Invalid")
else:
    print(output)

