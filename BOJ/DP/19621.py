import sys
input = sys.stdin.readline


N = int(input())
booked = []

for _ in range(N):
    booked.append(list(map(int, input().split())))

dp = [0] * N
dp[0] = booked[0][2]
res = dp[0]
if N > 1:
    dp[1] = booked[1][2]
    res = max(dp[0], dp[1])

for i in range(1, N):
    for j in range(0, i - 1):
        dp[i] = max(dp[i], dp[j] + booked[i][2])
    res = max(res, dp[i])

print(res)