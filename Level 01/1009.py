name = str(input())
salary = float(input())
vendas = float(input())

total = salary + (0.15 * vendas)

print(f"TOTAL = R$ {total:.2f}")