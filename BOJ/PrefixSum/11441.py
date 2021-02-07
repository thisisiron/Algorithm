import sys
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))
M = int(input())

dp = [0] * (N + 1)
dp[1] = arr[0]
for i in range(2, N + 1):
    dp[i] = arr[i - 1] + dp[i - 1]

for _ in range(M):
    s, e = map(int, input().split())
    print(dp[e] - dp[s - 1])