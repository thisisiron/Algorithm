import sys
import heapq
input = sys.stdin.readline


N, M, L = map(int, input().split())
location = [int(x) for x in input().split()]
location.append(0)
location.append(L)
location.sort()

left = 0
right = L
while left <= right:
    mid = (left + right) // 2

    new = 0
    for i in range(1, len(location)):
        dist = location[i] - location[i - 1] - 1
        new += (dist // mid)

    if new > M:
        left = mid + 1
    else:
        right = mid - 1

print(left)