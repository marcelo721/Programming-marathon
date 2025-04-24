bits = list(map(int, input().split()))
boool = True

for i in range(7):
    if bits[i] == 9:
        boool = False
        break 
     
if boool == True:
    print("S")
else:
    print("F")
        
        