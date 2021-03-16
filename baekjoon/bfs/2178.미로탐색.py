## https://www.acmicpc.net/problem/2178
from collections import deque

n, m = map(int,  input().split())

graph = [[]]
for i in range(n):
    row = [0] + list(map(int, input()))
    graph.append(row)


def bfs(x,y,count=0):
    queue = deque()
    queue.append((x,y))
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            newx, newy = a + dx[i], b + dy[i]
            if newx > n or newx < 1 or newy > m or newy < 1:
                continue
            if graph[newx][newy] == 1:
                graph[newx][newy] = graph[a][b] + 1
                queue.append((newx,newy))

    return graph[n][m]


print(bfs(1,1))


