from collections import deque

def bfs():
    queue = deque([(0,0)])
    while queue:
        x, y = queue.popleft()
        for dx, dy in zip([0, 1, 0, -1], [1, 0, -1, 0]):
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx > n-1 or ny < 0 or ny > n-1: continue
            if (mapcnt[x][y]+int(map[nx][ny])) < mapcnt[nx][ny]:
                mapcnt[nx][ny] = mapcnt[x][y]+int(map[nx][ny])
                queue.append((nx, ny))



tc = int(input())
for t in range(tc):
    n = int(input())
    map = [list(input()) for _ in range(n)]
    mapcnt = [[10000 for _ in range(n)] for _ in range(n)]
    mapcnt[0][0] = int(map[0][0])

    bfs()
    print(f"#{t+1} {mapcnt[n-1][n-1]}")