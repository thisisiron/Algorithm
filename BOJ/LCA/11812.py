import sys
from collections import deque
input = sys.stdin.readline


N, K, Q = map(int, input().split())

for _ in range(Q):
    x, y = map(int, input().split())

    if x < y:
        x, y = y, x
    diff = x - y
    if K == 1:
        print(diff)
        continue

    cnt = 0

    while x != y:
        if x < y:
            mx = y
            y = x
        else:
            mx = x
        x = ((mx - 2) // K) + 1
        cnt += 1

    print(cnt)