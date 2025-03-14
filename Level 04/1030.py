def josephus(n, k):
    result = 0  
    for i in range(2, n + 1):  
        result = (result + k) % i 
    return result + 1  

NC = int(input())

for case in range(1, NC + 1):
    n, k = map(int, input().split())
    
    survivor = josephus(n, k)
    
    print(f"Case {case}: {survivor}")
