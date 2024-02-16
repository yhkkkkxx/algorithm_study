ops = ["+", "-"]
cnt = 0


def calc(op, nums, t):
    global cnt
    sum = 0
    for i in range(len(nums)):
        if op[i] == "+": sum += nums[i]
        elif op[i] == "-": sum -= nums[i]

    if sum == t: cnt += 1


def dfs(x, op, nums, t):
    if x == len(op):
        calc(op, nums, t)
        return

    for o in ops:
        op[x] = o
        dfs(x + 1, op, nums, t)


def solution(numbers, target):
    op = ["" for _ in range(len(numbers))]
    op = dfs(0, op, numbers, target)
    return cnt

solution([1,1,1,1,1],3)
solution([4,1,2,1],4)