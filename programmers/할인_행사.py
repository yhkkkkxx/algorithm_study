from collections import Counter


def solution(want, number, discount):
    answer = 0

    for i in range(len(discount)-9):
        counter = Counter(discount[i:i+10])
        isPossible = True
        for j in range(len(want)):
            if counter.keys().__contains__(want[j]) and counter[want[j]] >= number[j]:
                continue
            else:
                isPossible = False
                break
        if isPossible: answer += 1
    print(answer)

    return answer






solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1], ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"])
solution(["apple"], [10], ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"])