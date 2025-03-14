
while True:
    A,B = map(int, input().split())
    if A == 0 and B == 0:
        break

    listA = list(map(int, input().split()))[:A]
    listB = list(map(int, input().split()))[:B]
 
    setA = set(listA)
    setB = set(listB)
    
    setC = setA.intersection(setB)
    
    result = 0
    if len(setA) < len(setB):
        result = abs(len(setA) - len(setC))
    else:
        result = abs(len(setB) - len(setC))

    print(result)
        
    