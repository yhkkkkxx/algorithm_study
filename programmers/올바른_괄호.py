def solution(s):
    arr = list(s)
    stack = list()
    cnt = 0

    for i in range(len(arr)):
        if cnt == 0 and arr[i] == ')': return False
        if arr[i] == '(':
            stack.append('(')
            cnt += 1
        elif arr[i] == ')':
            stack.pop()
            cnt -= 1
    if stack: return False
    return True

solution("()()")
solution("(())()")
solution(")()(")
solution("(()(")