import sys 
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(i, j):
    if dp[i][j] < 0:
        dp[i][j] = 0
        for mi, mj in zip(dy, dx):
            ni = i + mi
            nj = j + mj
            if 0 <= ni < n and 0 <= nj < n and bamboos[i][j] < bamboos[ni][nj]:
                dp[i][j] = max(dp[i][j], dfs(ni, nj)) 
        dp[i][j] += 1
    return dp[i][j]


dy = [-1, 1, 0, 0]
dx = [0, 0, 1, -1]

n = int(input())
bamboos = [[int(t) for t in map(int, input().split())] for _ in range(n)]
print(len(bamboos))
print(len(bamboos[0]))
dp = [[-1] * n for _ in range(n)] 
max_val = 0

for i in range(n):
    for j in range(n):
        tmp = dfs(i, j)
        if max_val < tmp:
            max_val = tmp

print(max_val)