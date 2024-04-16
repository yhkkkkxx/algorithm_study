for t in range(10):
    n = int(input())
    box = list(map(int, input().split()))
    box = sorted(box)

    for i in range(n):
        box = sorted(box)
        box[-1] -= 1
        box[0] += 1

    box = sorted(box)
    print(f"#{t+1} {max(box)-min(box)}")