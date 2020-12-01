import sys
input = sys.stdin.readline


N = int(input())
x_list = [int(x) for x in input().split()]
dp = [[0] * N for _ in range(N)]

for i in range(N):
    dp[i][i] = 1

for i in range(N - 1):
    if x_list[i] == x_list[i + 1]:
        dp[i][i + 1] = 1

for i in range(2, N):
    for j in range(2, i + 1):
        if x_list[i] == x_list[i - j] and dp[i - j + 1][i - 1]:
            dp[i - j][i] = 1

M = int(input())

for _ in range(M):
    s, e = map(int, input().split())
    print(dp[s - 1][e - 1]) 