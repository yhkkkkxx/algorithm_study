tc = int(input())
for t in range(tc):
    n, m = map(int, input().split())
    fly = [list(map(int, input().split())) for _ in range(n)]
    flysum = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            flysum[i][j] = flysum[i-1][j] + flysum[i][j-1] + fly[i-1][j-1] -flysum[i-1][j-1]
    maxfly = 0
    for i in range(m, n+1):
        for j in range(m, n+1):
            died = flysum[i][j] - flysum[i-m][j] - flysum[i][j-m] + flysum[i-m][j-m]
            if died > maxfly: maxfly = died

    print(f"#{t+1} {maxfly}")