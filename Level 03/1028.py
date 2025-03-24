N = int(input())

for i in range (N):
    R, V = map(int, input().split())
    a, b = abs(R), abs(V)  
    while b != 0:
        a, b = b, a % b
    mdc = a


    print(a)
