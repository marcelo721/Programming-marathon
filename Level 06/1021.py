
N = float(input()) * 100

N1 = N2 = N3 = N4 = N5 = N6 = 0
M1 = M2 = M3 = M4 = M5 = M6 = 0

N1 = N // 10000
N %= 10000

N2 = N // 5000
N %= 5000

N3 = N // 2000
N %= 2000

N4 = N // 1000
N %= 1000

N5 = N // 500
N %= 500

N6 = N // 200
N %= 200

M1 = N // 100
N %= 100

M2 = N // 50
N %= 50

M3 = N // 25
N %= 25

M4 = N // 10
N %= 10

M5 = N // 5
N %= 5

M6 = N // 1
N %= 1

print("NOTAS:")
print(f"{int(N1)} nota(s) de R$ 100.00")
print(f"{int(N2)} nota(s) de R$ 50.00")
print(f"{int(N3)} nota(s) de R$ 20.00")
print(f"{int(N4)} nota(s) de R$ 10.00")
print(f"{int(N5)} nota(s) de R$ 5.00")
print(f"{int(N6)} nota(s) de R$ 2.00")

print("MOEDAS:")
print(f"{int(M1)} moeda(s) de R$ 1.00")
print(f"{int(M2)} moeda(s) de R$ 0.50")
print(f"{int(M3)} moeda(s) de R$ 0.25")
print(f"{int(M4)} moeda(s) de R$ 0.10")
print(f"{int(M5)} moeda(s) de R$ 0.05")
print(f"{int(M6)} moeda(s) de R$ 0.01")