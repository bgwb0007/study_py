## https://www.acmicpc.net/problem/16234

N, L, R = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

check = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs_count(x,y):
    check.append((x,y))
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= N or nx < 0 or ny >= N or ny < 0:
            continue
        diff = graph[x][y] - graph[nx][ny]
        if diff < 0:
            diff = -diff
        if L <= diff and diff <= R:
            bfs_count(nx,ny)


