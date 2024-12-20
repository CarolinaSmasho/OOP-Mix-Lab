def draw(depth,long):
    if depth == 0:
        return

    draw(depth-1,long)

    for i in range(long-depth):
        print(" ",end='')

    for i in range(depth):
        print("#",end='')
    print("")

draw(10,10)