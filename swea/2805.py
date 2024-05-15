test = int(input())
for t in range(test):
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]
    revenue = 0

    for i in range(0, int(n/2)+1):
        for j in range(int(n/2)-i, int(n/2)+i+1): revenue += farm[i][j]
    for i in range(int(n/2)+1, n):
        for j in range(int(n/2)-(n-i-1), int(n/2)+(n-i-1)+1): revenue += farm[i][j]

    print(f"#{t+1} {revenue}")