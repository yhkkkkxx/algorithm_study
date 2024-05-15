test = int(input())
for t in range(test):
    matrix = [list(map(str, input().split())) for _ in range(4)]
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    nums = set()

    def dfs(l, i, j, number):
        if l == 7:
            nums.add(number)
            return

        for x, y in zip(dx, dy):
            if 0 <= i+x < 4 and 0 <= j+y < 4:
                dfs(l+1, i+x, j+y, number+matrix[i][j])

    for i in range(4):
        for j in range(4):
            dfs(0, i, j, '')

    print(f"#{t+1} {len(nums)}")