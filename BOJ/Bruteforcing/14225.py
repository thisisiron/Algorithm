import sys
from itertools import combinations
input = sys.stdin.readline


N = int(input())
S = list(map(int, input().split()))
A = set(S)

for i in range(1, len(S) + 1):
    for x in combinations(S, i):
        A.add(sum(x))

for i in range(1, 100000 * 20):
    if i not in A:
        print(i)
        break