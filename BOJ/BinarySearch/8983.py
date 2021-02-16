import sys
import bisect
input = sys.stdin.readline


M, N, L = map(int, input().split())
squad = [int(x) for x in input().split()]
squad.sort()

cnt = 0
for _ in range(N):
    x, y = map(int, input().split())
    if y <= L:
        idx = bisect.bisect(squad, x)

        if idx > 0 and abs(squad[idx - 1] - x) + y <= L:
            cnt += 1
        elif idx < M and abs(squad[idx] - x) + y <= L:
            cnt += 1
print(cnt)