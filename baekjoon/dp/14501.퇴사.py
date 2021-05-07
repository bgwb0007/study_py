## https://www.acmicpc.net/problem/14501

N = int(input())
graph = [[0]]
for _ in range(N):
    graph.append(tuple(map(int,input().split())))

days = [i for i in range(1,N+1)]
pays = [0 for _ in range(N)]
max_profit = dict(zip(days, pays))

for i in range(N, 0, -1):
    T, P = graph[i][0], graph[i][1]
    if i == N:
        max_profit[i] = 0 if T > 1 else P
        continue
    if i + T > N + 1 :
        max_profit[i] = max_profit[i+1]
    elif i+T == N + 1:
        max_profit[i] = max(max_profit[i+1], P)
    else:
        max_profit[i] = max(max_profit[i+1], P + max_profit[i+T])
print(max_profit[1])
