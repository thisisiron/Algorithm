import sys
from bisect import insort
input = sys.stdin.readline


N = int(input())
pos = []
for i in range(N):
    x, y = map(int, input().split())
    insort(pos, (x, y))
for a in pos:
    print(*a)