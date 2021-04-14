import sys
from itertools import combinations
input = sys.stdin.readline


N, M = map(int, input().split())
arr = [int(x) for x in input().split()]
comb = combinations(arr, 3)
mx = 0
for c in comb:
    res = sum(c)
    if res > M:
        continue
    elif res == M:
        mx = res
        break
    else:
        if res > mx:
            mx = res
print(mx)