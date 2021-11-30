import sys
input = sys.stdin.readline


max = lambda x, y: x if x > y else y


T = int(input())
for _ in range(T):
    N = int(input())
    a = []
    a.append([0] + [int(x) for x in input().split()])
    a.append([0] + [int(x) for x in input().split()])

    dp = [[0] * (N + 1) for _ in range(2)]

    dp[0][1] = a[0][1]
    dp[1][1] = a[1][1]

    for i in range(2, N + 1):
        dp[0][i] = max(dp[1][i - 1], dp[1][i - 2]) + a[0][i]
        dp[1][i] = max(dp[0][i - 1], dp[0][i - 2]) + a[1][i]
    
    print(max(dp[0][-1], dp[1][-1]))