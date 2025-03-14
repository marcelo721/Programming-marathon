def josephus(n, k):
    result = 0
    for i in range(2, n +1):
        result = (result + k) % i
    return result + 1

def encontrar(n):
    m = 1 
    while True:
        posicao = josephus(n - 1, m)
        if posicao == 12:  
            return m
        m += 1

while True:
    n = int(input())
    if n == 0:
        break

    print(encontrar(n))