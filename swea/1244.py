mval = 0
def dfs(x, i, j, cardlist):
    global mval
    if x == n:
        result = int(''.join(c for c in cardlist))
        if mval < result: mval = result
        return

    cardlist[i], cardlist[j] = cardlist[j], cardlist[i]
    for k in range(len(cardlist)-1):
        for l in range(k+1, len(cardlist)):
            dfs(x+1, k, l, cardlist)

    cardlist[i], cardlist[j] = cardlist[j], cardlist[i]
    return

tc = int(input())
for t in range(tc):
    mval = 0
    card, n = map(int, input().split())
    n = min(n, 4)
    card = list(str(card))

    for i in range(len(card)-1):
        for j in range(i+1, len(card)):
            cardlist = card[:]
            dfs(0, i, j, cardlist)

    print(f"#{t+1} {mval}")