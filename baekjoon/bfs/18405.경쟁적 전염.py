# https://www.acmicpc.net/problem/18405
from collections import deque

N, K = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
S, x, y = map(int, input().split())

answer = 0
virus = {}
for i in range(1, K + 1):
    virus[i] = deque([])

for i, row in enumerate(graph):
    for j, num in enumerate(row):
        if num != 0:
            virus[num].append((i, j))


def bfs(x, y, temp, virus_num):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(4):
        new_x, new_y = x + dx, y + dy
        if new_x < 0 or new_x >= N or new_y < 0 or new_y >= N:
            continue
        if graph(new_x, new_y) == 0:
            graph[new_x][new_y] = virus_num
            temp[virus_num].append((new_x, new_y))

for _ in range(S):
    for i in range(1,K+1):
        temp = virus[i]
        for j in temp:
            x,y = j
            bfs(x,y,temp,i)
        virus[i] = temp