import sys
input = sys.stdin.readline


N, K = map(int, input().split())

bag = [[0, 0]]
for _ in range(N):
    bag.append(list(map(int, input().split())))

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        w = bag[i][0]
        if j >=  w:
            dp[i][j] = max(bag[i][1] + dp[i - 1][j - w], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]
        
print(dp[-1][-1])