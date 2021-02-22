import sys
input = sys.stdin.readline


N = int(input())
k = int(input())

start, end = 1, k
while start <= end:
    mid = (start + end) // 2

    # cnt = N * (mid // N)
    # for i in range(mid // N + 1, N + 1):
    #     cnt += mid // i

    cnt = 0
    for i in range(1, N + 1):
        cnt += min(mid // i, N)

    if cnt < k:
        start = mid + 1
    else:
        end = mid - 1

print(start)