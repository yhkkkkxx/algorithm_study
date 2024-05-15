test = int(input())
for t in range(test):
    n = int(input())
    score = list(map(int, input().split()))
    scores = {0}

    for s in score:
        cpy = list(scores)
        for i in range(len(cpy)):
            scores.add(s+cpy[i])

    print(f"#{t+1} {len(scores)}")
