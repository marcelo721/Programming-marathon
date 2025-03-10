p1Code, p1Amount, p1Price = input().split()
p1Code = int(p1Code)
p1Amount = int(p1Amount)
p1Price = float(p1Price)

p2Code, p2Amount, p2Price = input().split()
p2Code = int(p2Code)
p2Amount = int(p2Amount)
p2Price = float(p2Price)

totalValue = (p1Amount * p1Price) + (p2Amount * p2Price)

print(f"VALOR A PAGAR: R$ {totalValue:.2f}")
