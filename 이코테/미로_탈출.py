from collections import deque

def bfs(mazecnt):
    global route

    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        maze[x][y] = '0'
        for i, j in zip([1, 0, -1, 0], [0, 1, 0, -1]):
            x += i
            y += j
            if x < 0 or x > n-1 or y < 0 or y > m-1:
                x -= i
                y -= j
                continue
            if maze[x][y] == '1':
                mazecnt[x][y] = min(mazecnt[x][y], int(maze[x][y])+mazecnt[x-i][y-j])
                if x == n-1 and y == m-1: return
                queue.append((x, y))
            x -= i
            y -= j




n, m = map(int, input().split())
maze = [list(input()) for _ in range(n)]
mazecnt = [[100 for _ in range(m)] for _ in range(n)]
mazecnt[0][0] = 1
bfs(mazecnt)
print(mazecnt[n-1][m-1])