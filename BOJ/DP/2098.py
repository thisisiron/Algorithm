import sys
input = sys.stdin.readline


def TSP(cur, visited):
    if visited == (1 << N) - 1:
        return W[cur][start] if W[cur][start] else float('inf')
    ret = dp[cur][visited]
    if ret != -1:
        return ret

    ret = float('inf')
    for i in range(N):
        if visited & (1 << i):
            continue
        if W[cur][i] == 0:
            continue
        ret = min(ret, TSP(i, visited | (1 << i)) + W[cur][i])
    dp[cur][visited] = ret
    return ret


start = 0
N = int(input())
dp = [[-1] * (1 << N) for _ in range(N)]
W = []
for i in range(N):
    W.append([int(x) for x in input().split()])

print(TSP(0, 1))