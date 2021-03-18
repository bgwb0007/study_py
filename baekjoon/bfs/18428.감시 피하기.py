## https://www.acmicpc.net/problem/18428

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(input().split()))
temp = [['X']*N for _ in range(N)]

student = []
teacher = []
box = []

check = False

for i in range(N):
    for j in range(N):
        if graph[i][j] == 'X':
            box.append((i,j))
        elif graph[i][j] == 'T':
            teacher.append((i,j))
        else:
            student.append((i,j))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
def overview(x,y):
    for i in range(4):
        if i == 0:
            while x <= N :
                if


def dfs(n):
    global check
    if n == 3:
        for i in range(N):
            for j in range(N):
                temp[i][j] = graph[i][j]

        for i in range(4):
            for t in teacher:
                overview(t[0],t[1],i)
        count = 0
        for i in range(N):
            for j in range(N):
                if temp[i][j] == 'S':
                    count +=1
                    if count == 3:
                        return count



    else:
        for i in range(N):
            for j in range(N):
                if graph[i][j] == 'X':
                    graph[i][j] = 'O'
                    n += 1
                    dfs(n)
                    graph[i][j] = 'X'
                    n -= 1
if dfs(0) == 3:
    print('YES')
else:
    print("NO")