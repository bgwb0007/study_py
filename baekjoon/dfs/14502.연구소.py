## https://www.acmicpc.net/problem/14502

N, M = map(int, input().split())
graph = []
temp = [[0]*M for i in range(N)]
for i in range(N):
    graph.append(list(map(int, input().split())))

answer = 0

virus = []
box = []
for i in range(N):
    for j in range(M):
        if graph[i][j]==2:
            virus.append((i,j))
        if graph[i][j]==0:
            box.append((i,j))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def virus_dfs(x,y,data):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if data[nx][ny] == 0:
            data[nx][ny] = 2
            virus_dfs(nx, ny,data)

def box_count(data):
    count = 0
    for i in data:
        for j in i:
            if j == 0:
                count += 1
    return count

def graph_copy(A,B):
    for idx_row,i in enumerate(A):
        for idx_column, j in enumerate(i):
            B[idx_row][idx_column] = j
    return B

for i in range(len(box)-2):
    for j in range(i+1,len(box)-1):
        for k in range(j+1, len(box)):
            check = graph_copy(graph,temp)
            b1, b2, b3 = box[i], box[j], box[k]
            check[b1[0]][b1[1]] = 1
            check[b2[0]][b2[1]] = 1
            check[b3[0]][b3[1]] = 1

            for v in virus:
                virus_dfs(v[0],v[1],check)
            answer = max(answer, box_count(check))

print(answer)