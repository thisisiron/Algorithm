import sys
from collections import deque
input = sys.stdin.readline


def bfs(start, x):
	q = deque()
	q.append((start, 0))
	visited = [0] * (N + 1)
	visited[start] = 1
	ans = [0, 0]

	while q:
		cur_n, cur_w = q.popleft()

		if cur_w > ans[1]: 
			ans[1] = cur_w
			ans[0] = cur_n

		for nxt_n, nxt_w in tree[cur_n]:
			if not visited[nxt_n]:
				q.append((nxt_n, cur_w + nxt_w))
				visited[nxt_n] = 1

	return ans[x]


N = int(input())
tree = {}
for i in range(N):
	tmp = [int(x) for x in input().split()]
	for j in range(1, len(tmp), 2):
		if tmp[j] == -1:
			break
		tree.setdefault(tmp[0], []).append((tmp[j], tmp[j + 1]))

print(bfs(bfs(1, 0), 1))