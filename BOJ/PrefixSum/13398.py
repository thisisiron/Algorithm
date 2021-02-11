import sys
input = sys.stdin.readline


N  = int(input())
arr = [int(x) for x in input().split()]

dp = [[0, 0] for _ in range(N)]
dp[0][0] = arr[0]

mx = -float('inf')

if N == 1:
    print(dp[0][0])
else:
    for i in range(1, N):
        dp[i][0] = max(dp[i - 1][0] + arr[i], arr[i])
        dp[i][1] = max(dp[i - 1][0], dp[i - 1][1] + arr[i])
        mx = max(mx, dp[i][0], dp[i][1])
    print(mx)