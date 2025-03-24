list1 = list(map(float, input().split()))
list1.sort(reverse=True)  

A, B, C = list1  

if A >= (B + C):
    print("NAO FORMA TRIANGULO")
else:
    if A**2 == (B**2 + C**2):
        print("TRIANGULO RETANGULO")
    if A**2 > (B**2 + C**2):
        print("TRIANGULO OBTUSANGULO")
    if A**2 < (B**2 + C**2):
        print("TRIANGULO ACUTANGULO")
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    elif A == B or B == C or A == C:
        print("TRIANGULO ISOSCELES")
