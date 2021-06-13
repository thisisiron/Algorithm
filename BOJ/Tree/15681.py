import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(cur):
	global visited, size
	for nxt in graph[cur]:
		if not visited[nxt]:
			visited[nxt] = 1
			dfs(nxt)
			size[cur] += size[nxt] 


N, R, Q = map(int, input().split())
graph = {}

for _ in range(N - 1):
	u, v = map(int, input().split())
	graph.setdefault(u, []).append(v)
	graph.setdefault(v, []).append(u)

visited = [0] * (N + 1)
visited[R] = 1
size = [1] * (N + 1)

dfs(R)

for _ in range(Q):
	print(size[int(input())])