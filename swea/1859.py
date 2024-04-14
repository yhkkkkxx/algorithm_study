tc = int(input())
for t in range(tc):
    n = int(input())
    prices = list(map(int, input().split()))

    buy = 0
    total = 0

    while prices:
        maxvalue = max(prices)
        idx = prices.index(maxvalue)
        total += idx * prices[idx] - sum(prices[:idx])
        prices = prices[idx+1:]

    print(f"#{t+1} {total}")