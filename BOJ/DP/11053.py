import sys
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))

dp = [0] * N
res = 0
for i in range(len(arr)):
    cur = 0
    for j in range(0, i):
        if arr[i] > arr[j]:
            cur = max(cur, dp[j])
    dp[i] = cur + 1
    res = max(res, dp[i])
    
print(res)