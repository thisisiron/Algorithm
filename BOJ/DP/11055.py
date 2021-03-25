import sys
input = sys.stdin.readline


N = int(input())
arr = [int(x) for x in input().split()]

dp = arr[:] 

for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            if dp[i] < dp[j] + arr[i]:
                dp[i] = dp[j] + arr[i]

print(max(dp))