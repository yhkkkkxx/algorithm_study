from collections import deque


def bfs(x, visited, graph):
    queue = deque([])
    queue.append(x)

    while queue:
        q = queue.popleft();
        visited[q] = True

        for g in graph[q]:
            if not visited[g]: queue.append(g)


def solution(n, computers):
    cnt = 0
    graph = [[] for _ in range(n)]
    visited = [False for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if computers[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)

    for i in range(n):
        if not visited[i]:
            bfs(i, visited, graph)
            cnt += 1

    return cnt


solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])