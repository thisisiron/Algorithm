import sys
input = sys.stdin.readline

N, M = map(int, input().split())
country = []
for _ in range(N):
    country.append(list(map(int, input().split())))

dp = [[0] * M for _ in range(N)]
dp[0][0] = country[0][0]
for i in range(1, N):
    dp[i][0] = country[i][0] + dp[i - 1][0]
for i in range(1, M):
    dp[0][i] = country[0][i] + dp[0][i - 1]
for row in range(1, N):
    for col in range(1, M):
        dp[row][col] = country[row][col] + dp[row - 1][col] + dp[row][col - 1] - dp[row - 1][col - 1]

T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == 1 and y1 == 1:
        print(dp[x2 - 1][y2 - 1])
    elif x1 > 1 and y1 == 1:
        print(dp[x2 - 1][y2 - 1] - dp[x1 -1 - 1][y2 - 1])
    elif x1 == 1 and y1 > 1:
        print(dp[x2 - 1][y2 - 1] - dp[x2 - 1][y1 - 1 - 1])
    elif x1 > 1 and y1 > 1:
        print(dp[x2 - 1][y2 - 1] - dp[x1 - 1 - 1][y2 - 1] - dp[x2 - 1][y1 -1 - 1] + dp[x1 - 1 - 1][y1 - 1 - 1])