def count(puzzle):
    cnt = 0
    for i in range(n):
        length = 0
        for j in range(n):
            if puzzle[i][j] == '1':
                length += 1
                if length == k and j == n-1:
                    cnt += 1
                    length = 0
            if puzzle[i][j] == '0':
                if length == k:
                    cnt += 1
                length = 0
    return cnt


test = int(input())
for t in range(test):
    n, k = map(int, input().split())
    puzzle = [list(map(str, input().split())) for _ in range(n)]

    cnt = 0
    cnt += count(puzzle)
    puzzle = list(zip(*puzzle[::-1]))
    cnt += count(puzzle)

    print(f"#{t+1} {cnt}")