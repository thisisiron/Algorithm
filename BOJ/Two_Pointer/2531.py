import sys 
from collections import deque
input = sys.stdin.readline


N, d, k, c = map(int, input().split())
sushis = [] 
for _ in range(N):
    sushis.append(int(input()))

mx = 0 
ate = [] 
start = 0
end = k

while True:
    if start == len(sushis):
        break

    if len(ate) == k:
        if mx <= len(set(ate)):
            mx = len(set(ate))
            if c not in ate:
                mx += 1
        ate.pop(0)
        start += 1
        end += 1
        if end >= len(sushis):
            end %= len(sushis)
    if start < end:
        ate = sushis[start:end]
    else:
        ate = sushis[start:] + sushis[:end]

    if mx == k + 1:
        break

print(mx)