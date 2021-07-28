import sys
ipnut = sys.stdin.readline


def init(start, end, cur):
    if start == end:
        tree[cur] = arr[start]
        return tree[cur]
    mid = (start + end) // 2
    tree[cur] = min(init(start, mid, cur * 2), init(mid + 1, end, cur * 2 + 1))
    return tree[cur]


def find(start, end, cur, left, right):
    if left > end or right < start:
        return 1000000001

    if left <= start and end <= right:
        return tree[cur]

    mid = (start + end) // 2
    return min(find(start, mid, cur * 2, left, right), find(mid + 1, end, cur * 2 + 1, left, right))


N, M = map(int, input().split())

arr = [int(input()) for _ in range(N)]
tree = [0] * 4 * N
init(0, N - 1, 1)

for i in range(M):
    a, b = map(int, input().split())
    print(find(0, N - 1, 1, a - 1, b - 1))
