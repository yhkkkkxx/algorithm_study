for t in range(10):
    n = int(input())
    buildings = list(map(int, input().split()))

    jomang = 0
    for i in range(2, len(buildings)-2):

        side = max(buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2])
        if buildings[i] > side:
            jomang += buildings[i] - side

    print(f"#{t+1} {jomang}")
