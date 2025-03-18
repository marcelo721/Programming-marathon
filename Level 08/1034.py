
def blocos(valores, n, m):
    if m % valores[n - 1] == 0:
        return m // valores[n - 1]
    
    pd = [float('inf')] * (m + 1)
    pd[0] = 0
    
    for k in valores:
        for j in range(k, m + 1):
            pd[j] = min(pd[j], pd[j - k] + 1)
    
    return pd[m]


t = int(input())
for i in range(t):
    n, m = map(int,input().split())
    valores = list(map(int, input().split()))
    valores.sort()
    print(blocos(valores, n, m))
