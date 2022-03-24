import sys
input = sys.stdin.readline


N, Q = map(int, input().split())
tree = [0 for _ in range(N + 1)]

for _ in range(Q):
    x = int(input())

    cur = x
    flag = False
    while cur > 1:
        if tree[cur]:
            flag = True
            first = cur

        cur //= 2

        if cur == 1:
            if flag:
                print(first)
            else:
                print(0)
                tree[x] = 1