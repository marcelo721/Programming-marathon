X = int(input())

for i in range(1, X + 1):
    n1, p1, n2, p2, n3, p3, n4 = input().split()
    n1, n2, n3, n4 = map(int, [n1, n2, n3, n4])

    # Operações com frações
    if p2 == '/':
        numerador = n1 * n4
        denominador = n2 * n3
    elif p2 == '*':
        numerador = n1 * n3
        denominador = n2 * n4
    elif p2 == '+':
        numerador = n3 * n2 + n1 * n4
        denominador = n2 * n4
    elif p2 == '-':
        numerador = n1 * n4 - n3 * n2
        denominador = n2 * n4  

    a, b = abs(numerador), abs(denominador)  
    while b != 0:
        a, b = b, a % b
    mdc = a

    num_simplificado = numerador // mdc
    den_simplificado = denominador // mdc

    print(f'{numerador}/{denominador} = {num_simplificado}/{den_simplificado}')
