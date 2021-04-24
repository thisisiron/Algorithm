import sys
input = sys.stdin.readline


N, K = map(int, input().split())
branch = [0] + [int(x) for x in input().split()]

dp = [0] * (N + 1)

j = 0
total = 0
for i in range(1, N + 1):
    total += branch[i]
    dp[i] = dp[i - 1]
    while total >= K:
        dp[i] = max(dp[i], dp[j] + total - K)
        j += 1
        total -= branch[j]

print(dp[-1])