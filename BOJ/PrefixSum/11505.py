import sys
input = sys.stdin.readline


def init(start, end, cur):
    if start == end:
        tree[cur] = arr[start]
    else:
        mid = (start + end)//2
        tree[cur] = (init(start, mid, cur * 2) * init(mid + 1, end, cur * 2 + 1)) % 1000000007
    return tree[cur]


def update(start, end, cur, idx, val):
    if idx < start or end < idx:
        return

    if start == end:
        tree[cur] = val
        return

    mid = (start + end) // 2

    update(start, mid, cur * 2, idx, val)
    update(mid + 1, end, cur * 2 + 1, idx, val)
    tree[cur] = (tree[cur * 2] * tree[cur * 2 + 1]) % 1000000007


def mul_interval(start, end, cur, left, right):
    if right < start or end < left:
        return 1

    if left <= start and end <= right:
        return tree[cur]

    mid = (start + end) // 2
    val = mul_interval(start, mid, cur * 2, left, right) * mul_interval(mid + 1, end, cur * 2 + 1, left, right)
    return val % 1000000007


N, M, K = map(int, input().split())

arr = [int(input()) for i in range(N)]

tree = [0] * (4 * N)
init(0, N - 1, 1)

for _ in range(M + K):
    a, b, c = map(int, input().split())

    if a == 1:
        update(0, N - 1, 1, b - 1, c)
        arr[b - 1] = c
    elif a == 2:
        print(mul_interval(0, N - 1, 1, b - 1, c - 1))