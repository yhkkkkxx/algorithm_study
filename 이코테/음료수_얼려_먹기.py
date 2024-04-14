def dfs(x, y):
    if x > 0 and ice[x-1][y] == '0':
        ice[x-1][y] = '1'
        dfs(x-1, y)
    if y > 0 and ice[x][y-1] == '0':
        ice[x][y-1] = '1'
        dfs(x, y-1)
    if x < n-1 and ice[x+1][y] == '0':
        ice[x+1][y] = '1'
        dfs(x+1, y)
    if y < m-1 and ice[x][y+1] == '0':
        ice[x][y+1] = '1'
        dfs(x, y+1)
    return


n, m = map(int, input().split())
ice = [list(input()) for _ in range(n)]
icecream = 0

for i in range(n):
    for j in range(m):
        if ice[i][j] == '0':
            ice[i][j] = '1'
            dfs(i, j)
            icecream += 1

print(icecream)