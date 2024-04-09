tc = int(input())
for t in range(tc):
    n = int(input())
    score = list(map(int, input().split()))
    grade = [0 for _ in range(101)]

    for s in score: grade[s] += 1
    for i in range(100, -1, -1):
        if grade[i] == max(grade):
            print(f"#{n} {i}")
            break