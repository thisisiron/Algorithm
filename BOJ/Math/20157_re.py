import sys
import math
input = sys.stdin.readline


N = int(input())
arrow = {}
for _ in range(N):
    x, y = map(int, input().split())
    g = math.gcd(x, y)
    arrow.setdefault((x//g, y//g), 0)
    arrow[(x//g, y//g)] += 1

print(max(arrow.values()))