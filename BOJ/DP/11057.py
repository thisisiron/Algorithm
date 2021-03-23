import sys
input = sys.stdin.readline


N = int(input())

dp = [[0] * 10 for _ in range(1001)]

for i in range(10):
    dp[1][i] = 1

for i in range(2, N + 1):
    for j in range(9, -1, -1):
        if j == 9:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i][j + 1] + dp[i - 1][j]

print(sum(dp[N]) % 10007)