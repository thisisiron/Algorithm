import sys
input = sys.stdin.readline


N = int(input())
dp = [0] * (N + 1)
ans = [0] * (N + 1)

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 1
    ans[i]  = i -1
    if i % 3 == 0 and dp[i] > dp[i//3] + 1:
        dp[i] = dp[i//3] + 1
        ans[i] = i // 3
    if i % 2 == 0 and dp[i] > dp[i//2] + 1:
        dp[i] = dp[i//2] + 1
        ans[i] = i // 2

print(dp[N])
print(N, end=' ')
while N != 1:
    print(ans[N], end=' ')
    N = ans[N]