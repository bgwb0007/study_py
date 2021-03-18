# https://www.acmicpc.net/problem/18405
from collections import deque

N, K = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))
S, x, y = map(int, input().split())

answer = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]



def virus_go(x,y, graph):
    go_q = deque()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph):
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y]
            go_q.append((nx,ny))
    return go_q



def virus_bfs(q, s):
    if s > S:
        return
    if graph[x-1][y-1] != 0:
        return
    next_queue = deque()
    while q:
        a, b = q.popleft()
        next_queue += virus_go(a, b, graph)

    virus_bfs(next_queue,s+1)

queue = deque()
for virus in range(1, K + 1):
    for a in range(len(graph)):
        for b in range(len(graph)):
            if graph[a][b] == virus:
                queue.append((a, b))

virus_bfs(queue, 1)

print(graph[x-1][y-1])