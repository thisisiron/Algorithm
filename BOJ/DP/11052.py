import sys
input = sys.stdin.readline


N = int(input())
prices = [0] + list(map(int, input().split()))
dp = [0] * (N + 1)

dp[1] = prices[1]
for i in range(2, N + 1):
    for j in range(1, i + 1):
        if dp[i] < dp[i - j] + prices[j]:
            dp[i] = dp[i - j] + prices[j]

print(dp[N])