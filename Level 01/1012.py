a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

PI =  3.14159

a1 = (a * c) /2
a2 = PI *c*c
a3 = ((a + b)*c)/2
a4 = b * b
a5 = a * b

print(f"TRIANGULO: {a1:.3f}")
print(f"CIRCULO: {a2:.3f}")
print(f"TRAPEZIO: {a3:.3f}")
print(f"QUADRADO: {a4:.3f}")
print(f"RETANGULO: {a5:.3f}")

