import sys
input = sys.stdin.readline


def dfs(u, i):
    visited[u] = 1

    for v in graph[u]:
        if not visited[v]:
            dfs(v, i)
        elif visited[v] and v == i:
            answer.append(v)


N = int(input())
arr = []
graph = {}
for a in range(1, N + 1):
    b = int(input())
    graph.setdefault(a, []).append(b)

answer = []
for i in range(1, N + 1):
    print('::', i)
    visited = [0] * (N + 1)
    dfs(i, i)

print(len(answer))
print(*answer, sep='\n')