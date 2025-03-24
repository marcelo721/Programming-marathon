import sys

def pode_organizar_vagoes(n, sequencia):
    pilha = []  
    esperado = 1  
    
    for v in sequencia:
        while esperado <= n and (not pilha or pilha[-1] != v):
            pilha.append(esperado)  
            esperado += 1
        
        if pilha[-1] == v:
            pilha.pop()  
        else:
            return "No"
    return "Yes"

while True :
    n = int(input())
    if n == 0:
        break
    while True:
        sequencia = list(map(int, input().split()))
        if sequencia[0] == 0:
            print()
            break
        print(pode_organizar_vagoes(n, sequencia))
    