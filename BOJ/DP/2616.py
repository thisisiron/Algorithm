from re import M
import sys
input = sys.stdin.readline


N = int(input())
arr = [0]
for i, n in enumerate(map(int, input().split()), 1):
    arr.append(n + arr[i - 1])

M = int(input())

dp = [[0] * (N + 1) for _ in range(4)]

for i in range(1, 4):
    for j in range(i * M, N + 1):
        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - M] + arr[j] - arr[j - M])

print(dp[3][N])