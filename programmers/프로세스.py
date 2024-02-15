from collections import deque

def solution(priorities, location):
    prior = deque(priorities)
    mval = max(prior)
    rank = 1

    while prior:
        if mval == prior[0]:
            if location == 0: return rank
            prior.popleft()
            mval = max(prior)
            rank += 1
        else:
            p = prior.popleft()
            prior.append(p)

        if location == 0: location = len(prior) - 1
        else: location -= 1

solution([2,1,3,2], 2)
solution([1,1,9,1,1,1],0)