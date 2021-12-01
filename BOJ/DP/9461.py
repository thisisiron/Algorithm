import sys
input = sys.stdin.readline


T = int(input())
dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for _ in range(T):
    N = int(input())
    if len(dp) > N:
        print(dp[N - 1])
        continue
    i = len(dp) - 1
    while N - len(dp) > 0:
        dp.append(dp[i] + dp[i - 4])
        i += 1
    print(dp[-1])