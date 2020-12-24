import sys
input = sys.stdin.readline


def find(parent, x):
    if x == parent[x]:
        return x
    parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, x, y):
    x = find(parent, x)
    y = find(parent, y)
    parent[x] = y


G = int(input())
P = int(input())
g = [int(input()) for _ in range(P)]

airport = [a for a in range(G + 1)]
cnt = 0

for i in g:
    docking = find(airport, i)
    if docking:
        union(airport, docking, docking - 1)
        cnt += 1
    else:
        break

print(cnt)