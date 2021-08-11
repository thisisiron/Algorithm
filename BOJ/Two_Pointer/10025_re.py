import sys
from collections import deque
input = sys.stdin.readline


N, K = map(int, input().split())
buckets = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: x[1])
q = deque()
cur = 0
total = 0
mx = 0

for ice, pos in buckets:
    cur = max(pos - K, 0)

    total += ice
    q.append((pos, ice))

    while q[0][0] < cur - K:
        total -= q.popleft()[1]

    if mx < total:
        mx = total
print(mx)