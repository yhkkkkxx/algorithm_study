from collections import deque
import math


def solution(progresses, speeds):
    answer = []
    works = deque([])

    for p, s in zip(progresses, speeds):
        works.append(math.ceil((100 - p) / s))

    w = works.popleft()
    cnt = 1
    while works:
        if works[0] > w:
            answer.append(cnt)
            w = works.popleft()
            cnt = 1
        else:
            cnt += 1
            works.popleft()

    answer.append(cnt)

    return answer

solution([93, 30, 55], [1, 30, 5])
solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])