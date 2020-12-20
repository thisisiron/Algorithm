# Pypy3

import sys
input = sys.stdin.readline


N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)][::-1]
cnt = 0

for coin in coins:
    while coin <= K:
        K -= coin
        cnt += 1

print(cnt)