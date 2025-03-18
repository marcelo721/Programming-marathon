while True :
    B, N = map(int, input().split())
    if B == 0 and N == 0:
        break
    
    reservas = list(map(int, input().split()))[:B]
    
    for i in range(N):
        D, C, V = map(int, input().split())
        reservas[D-1] -= V
        reservas[C-1] += V


    if any(x < 0 for x in reservas):
        print("N")
    else:
        print("S")