import sys
import math
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
home = []
chicken = []

for r in range(N):
    for c, p in enumerate(map(int, input().split())):
        if p == 1:
            home.append((r, c))
        elif p == 2:
            chicken.append((r, c))

mn = math.inf
for comb in combinations(chicken, M):
    dist = 0
    for h in home:
        dist += min([abs(h[0] - ch[0]) + abs(h[1] - ch[1]) for ch in comb])
        if mn <= dist:
            break
    if dist < mn:
        mn = dist
print(mn)