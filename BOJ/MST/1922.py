import sys
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if parent[x] < parent[y]:
        parent[x] = y
    else:
        parent[y] = x


N = int(input())
M = int(input())

computers = []
for _ in range(M):
    a, b, c = map(int, input().split())
    computers.append((c, a, b))

parent = [i for i in range(N + 1)]
computers.sort()
E = 0
ans = 0
while E < N - 1:
    c, a, b = computers.pop(0) 
    if find(a) != find(b):
        union(a, b)
        E += 1
        ans += c

print(ans)