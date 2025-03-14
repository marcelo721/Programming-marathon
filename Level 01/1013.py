a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

maior = (a + b + abs(a -b))/2
if maior == a:
    maior = (a + c + abs(a - c))/2
    if maior == a:
        maior = a
elif maior == b:
    maior = (b + c + abs(b - c))/2
    if maior == b:
        maior = b
else:
    maior = c

maior = int(maior)
print(f"{maior} eh o maior")
