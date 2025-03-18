import math

try:
    while True:
        r1, x1, y1, r2, x2, y2 = map(int, input().split())  
        area_c = math.pi * r1 * r1
        area_f = math.pi * r2 * r2

        if area_c >= area_f and (math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) + r2 <= r1):
            print('RICO')
        else:
            print('MORTO')
except EOFError:
    pass 
