import sys
input = sys.stdin.readline


n = int(input())

dp = [0, 1, 3] + [0] * (n - 2)

if n > 2:
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + 2 * dp[i - 2]
print(dp[n] % 10007)