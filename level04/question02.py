def calcular(x1, y1, x2, y2):
    if(x1 == x2 and y1 == y2):
        return 0 
    elif(x1 == y1 and x2 == y2):
        return 1
    elif(x1 == x2 or y1 == y2):
        return 1
    else:
        var = False
        while var == False:
            if(x1 < x2 and y1 > y2):
                x1 += 1
                y1 -= 1
                if(x1 == x2 and y1 == y2):
                    return 1
            elif(x1 < x2 and y1 < y2):
                x1 += 1
                y1 += 1
                if(x1 == x2 and y1 == y2):
                    return 1
            elif(x1 > x2 and y1 > y2):
                x1 -= 1
                y1 -= 1
                if(x1 == x2 and y1 == y2):
                    return 1
            elif(x1 > x2 and y1 < y2):
                x1 -= 1
                y1 += 1
                if(x1 == x2 and y1 == y2):
                    return 1
            else:
                return 2

while True:
    x1, y1, x2, y2 = map(int, input().split())
    if(x1 == 0 and x2 == 0 and y1 == 0 and y2 == 0):
        break

    print(calcular(x1, y1, x2, y2))
