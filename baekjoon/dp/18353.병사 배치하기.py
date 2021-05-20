# https://www.acmicpc.net/problem/18353

N = int(input())

array = list(map(int, input().split()))
array.reverse()

# 다이나믹 프로그래밍을 위한 1차원 DP 테이블 초기화
dp = [1] * N

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, N):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 열외해야 하는 병사의 최소 수를 출력
print(N - max(dp))