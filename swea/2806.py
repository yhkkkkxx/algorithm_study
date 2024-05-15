test = int(input())
for t in range(test):
    n = int(input())
    queen = [-1] * n
    others = [i for i in range(n)]
    cnt = 0

    def dfs(x, queen, others):
        global cnt
        if x == n:
            cnt += 1
            return

        for o in others:
            can = True
            for i in range(x):
                if abs(x-i) == abs(queen[i] - o):
                    can = False
                    break
            if x == 0 or (queen.count(o) == 0 and abs(queen[x-1] - o) != 1 and can):
                queen[x] = o
                dfs(x+1, queen, others)
                queen[x] = -1

    dfs(0, queen, others)

    print(f"#{t+1} {cnt}")