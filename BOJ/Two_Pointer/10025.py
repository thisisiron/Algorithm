import sys
input = sys.stdin.readline


N, K = map(int, input().split())

buckets = {}
max_right = 0
min_left = 1000001
for i in range(N):
    g, x = map(int, input().split())
    buckets[x] = g
    if min_left > x:
        min_left = x
    if max_right < x:
        max_right = x

right = min_left
cur = 0
mx = 0
for left in range(min_left, max_right + 1):
    while right < max_right + 1 and right - left <= K * 2:
        if right not in buckets:
            right += 1
            continue
        cur += buckets[right]
        right += 1
    if mx < cur:
        mx = cur
    if left in buckets:
        cur -= buckets[left]
print(mx)