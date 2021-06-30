import sys
input = sys.stdin.readline


N = int(input())
arr = [int(x) for x in input().split()]

dp = [0] * N
ans = 0

for i in range(N):
    cur = 0
    for j in range(i):
        if arr[i] > arr[j]:
            if cur < dp[j]:
                cur = dp[j]
    dp[i] = cur + 1
    if ans < dp[i]:
        ans = dp[i]
print(ans)