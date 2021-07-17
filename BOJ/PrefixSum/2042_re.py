import sys
input = sys.stdin.readline


def init(start, end, cur):
    if start == end:
        tree[cur] = arr[start]
        return tree[cur]

    mid = (start + end) // 2

    tree[cur] = init(start, mid, cur * 2) + init(mid + 1, end, cur * 2 + 1)
    return tree[cur]


def update(start, end, cur, idx, val):
    if idx < start or idx > end:
        return

    tree[cur] += val

    if start == end:
        return

    mid = (start + end) // 2

    update(start, mid, cur * 2, idx, val)
    update(mid + 1, end, cur * 2 + 1, idx, val)


def sum_interval(start, end, cur, left, right):
    if left > end or right < start:
        return 0

    if left <= start and end <= right:
        return tree[cur]

    mid = (start + end) // 2
    return sum_interval(start, mid, cur * 2, left, right) + sum_interval(mid + 1, end, cur * 2 + 1, left, right)


N, M, K = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(int(input()))

tree = [0] * 4 * N
init(0, N - 1, 1)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        update(0, N - 1, 1, b - 1, c - arr[b - 1])
        arr[b - 1] = c
    elif a == 2:
        print(sum_interval(0, N - 1, 1, b - 1, c - 1))