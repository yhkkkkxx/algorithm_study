def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        x, y = i//n, i%n
        answer.append(max(x, y)+1)

    return answer


solution(3, 2, 5)
solution(4, 7, 14)