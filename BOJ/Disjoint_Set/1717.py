import sys
input = sys.stdin.readline


def find(x):
    if x != node[x]:
        x = find(node[x])
    return x


def union(x, y):

    x = find(x)
    y = find(y)

    if x == y:
        return x
    
    if rank[x] < rank[y]:
        node[x] = y
    else:
        node[y] = x

        if rank[x] == rank[y]:
            rank[x] += 1


n, m = map(int, input().split())
node = [i for i in range(n + 1)]
rank = [1 for i in range(n + 1)]

for _ in range(m):
    ops, a, b = map(int, input().split())
    if ops == 0:
        union(a, b)
    else:
        print('YES' if find(a) == find(b) else 'NO')