import sys
input = sys.stdin.readline


def init(start, end, cur):
    if start == end:
        tree[cur][0] = arr[start]
        tree[cur][1] = arr[start]
        return tree[cur]

    mid = (start + end) // 2

    left = init(start, mid, cur * 2)
    right = init(mid + 1, end, cur * 2 + 1)
    tree[cur][0], tree[cur][1] = min(left[0], right[0]), max(left[1], right[1])
    return tree[cur]


def find(start, end, cur, left, right):
    if left > end or right < start:
        return 1000000001, 0

    if left <= start and end <= right:
        return tree[cur]

    mid = (start + end) // 2
    l = find(start, mid, cur * 2, left, right)
    r = find(mid + 1, end, cur * 2 + 1, left, right)
    return (min(l[0], r[0]), max(l[1], r[1]))


N, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]
tree = [[0, 0] for _ in range(4 * N)]  # min / max
init(0, N - 1, 1)
for _ in range(M):
    a, b = map(int, input().split())
    print(*find(0, N - 1, 1, a - 1, b - 1))
