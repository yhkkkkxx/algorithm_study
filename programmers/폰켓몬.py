def solution(nums):
    answer = 0
    length = len(nums)
    nums = set(nums)

    answer = min(length // 2, len(nums))

    return answer


solution([3, 1, 2, 3])
solution([3, 3, 3, 2, 2, 4])
solution([3, 3, 3, 2, 2, 2])