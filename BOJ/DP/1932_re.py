import sys
input = sys.stdin.readline


n = int(input())
arr = []
for _ in range(n):
	arr.append([int(x) for x in input().split()])

dp = [[0] * (i + 1) for i in range(1, n + 1)]
dp[0][0] = arr[0][0]

for i in range(1, n):
	for j in range(i + 1):
		dp[i][j] = dp[i -1][j] + arr[i][j] if dp[i - 1][j - 1] < dp[i -1][j] else dp[i - 1][j - 1] + arr[i][j] 
print(max(dp[-1]))