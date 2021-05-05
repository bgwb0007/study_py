## https://www.acmicpc.net/problem/1932

n = int(input())
tri = {}
for i in range(n):
    temp = list(map(int,input().split()))
    tri[i] = temp

for i in range(1, len(tri)):
    temp_list =[]
    for j in range(len(tri[i])):
        temp = 0
        if j == 0:
            temp = tri[i-1][0] + tri[i][j]
        elif j == len(tri[i])-1:
            temp = tri[i-1][-1] + tri[i][j]
        else:
            temp = max(tri[i-1][j-1], tri[i-1][j]) + tri[i][j]
        temp_list.append(temp)
    tri[i] = temp_list
print(max(tri[n-1]))