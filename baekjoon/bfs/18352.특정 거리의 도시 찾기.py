## https://www.acmicpc.net/problem/18352
from collections import deque

N, M, K, X = map(int, input().split())
lists = [[] for i in range(N+1)]
for i in range(M):
    x, y = map(int, input().split())
    lists[x].append(y)
dist = [-1 for i in range(N+1)]
dist[X] = 0

queue = deque()
queue.append(X)
while queue:
    now = queue.popleft()

    for i in lists[now]:
        if dist[i] == -1:
            dist[i] = dist[now] + 1
            queue.append(i)

count=0
for idx, val in enumerate(dist):
    if val == K:
        print(idx)
        count +=1
if count == 0:
    print(-1)

