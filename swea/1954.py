tc = int(input())
for t in range(tc):
    n = int(input())

    arr = [[0 for _ in range(n+2)] for _ in range(n+2)]
    for i in range(n+2):
        for j in range(n+2):
            if i==0 or j==0 or i==n+1 or j==n+1:
                arr[i][j] = -1

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    cnt = 1
    k = 0
    x = 1
    y = 1
    while 1:
        if arr[x][y] == 0:
            arr[x][y] = cnt
            cnt+=1

        if arr[x+dx[k]][y+dy[k]] != 0:
            k+=1
            k%=4

        x += dx[k]
        y += dy[k]

        if cnt == pow(n,2)+1: break


    print(f"#{t+1}")
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(arr[i][j], end=" ")
        print("")