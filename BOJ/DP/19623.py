import sys
import bisect
input = sys.stdin.readline


N = int(input())
adj = []
booked = []

for _ in range(N):
    s, e, c = map(int, input().split())
    adj.append([s, e, c])
    booked.append(e)

adj.sort(key=lambda x: x[1])
booked.sort()

dp = [0] * N
dp[0] = adj[0][2]

for i in range(1, N):
    s = adj[i][0]
    bs = bisect.bisect(booked, s)
    if bs == 0:
        dp[i] = max(dp[i - 1], adj[i][2])
    else:
        dp[i] = max(dp[i - 1], dp[bs - 1] + adj[i][2])

print(dp[-1])