import math

N = int(input())
resp = N
N1 = 0
N2 = 0
N3 = 0
N4 = 0
N5 = 0
N6 = 0
N7 = 0

while N > 0:
    if N >= 100:
        N1 = math.floor(N / 100)
        N %= 100  
    if N >= 50:
        N2 = math.floor(N / 50)
        N %= 50
    if N >= 20:
        N3 = math.floor(N / 20)
        N %= 20
    if N >= 10:
        N4 = math.floor(N / 10)
        N %= 10
    if N >= 5:
        N5 = math.floor(N / 5)
        N %= 5
    if N >= 2:
        N6 = math.floor(N / 2)
        N %= 2
    if N >= 1:
        N7 = math.floor(N / 1)
        N %= 1  
print(resp)
print(f"{N1} nota(s) de R$ 100,00")
print(f"{N2} nota(s) de R$ 50,00")
print(f"{N3} nota(s) de R$ 20,00")
print(f"{N4} nota(s) de R$ 10,00")
print(f"{N5} nota(s) de R$ 5,00")
print(f"{N6} nota(s) de R$ 2,00")
print(f"{N7} nota(s) de R$ 1,00")
