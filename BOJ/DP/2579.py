import sys
input = sys.stdin.readline


N = int(input())
step = [int(input()) for _ in range(N)]
dp = [0] * (N + 1)
dp[1] = step[0]
if N > 1:
    dp[2] = step[0] + step[1]

    for i in range(3, N + 1):
        dp[i] = max(dp[i - 2] + step[i - 1], dp[i - 3] + step[i - 2] + step[i - 1])

print(dp[-1])