def solution(s):
    answer = []
    s = s[2:-2]
    nums = s.split("},{")
    nums = sorted(nums, key=lambda x: len(x))
    arr = []

    for num in nums:
        a = []
        for n in num.split(","):
            a.append(int(n))
        arr.append(a)

    answer.append(set(arr[0]).pop())
    for i in range(1, len(arr)):
        aasdf = set(set(arr[i]) - set(arr[i - 1]))
        answer.append(aasdf.pop())

    print(answer)

    return answer


solution("{{2},{2,1},{2,1,3},{2,1,3,4}}")
solution("{{1,2,3},{2,1},{1,2,4,3},{2}}")
solution("{{20,111},{111}}")
solution("{{123}}")
solution("{{4,2,3},{3},{2,3,4,1},{2,3}}")