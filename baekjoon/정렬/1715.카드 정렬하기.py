## https://www.acmicpc.net/problem/1715

import heapq

n = int(input())
h = []
for _ in range(n):
    heapq.heappush(h, int(input()))
count = 0
while len(h) > 1:
    n1= heapq.heappop(h)
    n2 = heapq.heappop(h)
    heapq.heappush(h, n1+n2)
    count += n1+n2
print(count)