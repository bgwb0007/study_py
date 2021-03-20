        ## https://www.acmicpc.net/problem/16234

N, L, R = map(int, input().split())
graph = []
for i in range(N):
    graph.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

temp = [[-1 for _ in range(N)] for _ in range(N)]
def bfs_count(x, y, check, temp):
    ## 이미 방문했는지 확인
    if temp[x][y] != -1:
        return False
    check.append((x, y))
    ##방문처리
    temp[x][y] = graph[x][y]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= N or nx < 0 or ny >= N or ny < 0:
            continue
        diff = graph[x][y] - graph[nx][ny]
        if diff < 0:
            diff = -diff
        if L <= diff and diff <= R:
            bfs_count(nx, ny, check,temp)
    move(check,temp)
    return True

def move(check, temp):
    total = 0
    for i in range(len(check)):
        total += temp[check[i][0]][check[i][1]]
    avg = (int)(total / len(check))
    for i in range(len((check))):
        temp[check[i][0]][check[i][1]] = avg

def check(x, y, graph, count, check_lists):
    if check_lists[x][y]:
        return count
    count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= N or nx < 0 or ny >= N or ny < 0:
            continue
        diff = graph[x][y] - graph[nx][ny]
        if diff < 0:
            diff = -diff
        if L > diff or diff > R:
            check(nx, ny, graph, count, check_lists)
    return count
def create_check(N):
    lists = [[False for _ in range(N)] for _ in range(N)]
    return lists

sum = 0
check_count = check(0,0,graph,0,create_check(N))
while check_count < N*N:
    temp = [[-1 for _ in range(N)] for _ in range(N)]
    check=[]
    for i in range(N):
        for j in range(N):
            bfs_count(i,j,check,temp)
    for i in range(N):
        for j in range(N):
            graph[i][j] = temp[i][j]
    sum +=1
    check_count = check(0,0,graph,0,create_check(N))
print(sum)