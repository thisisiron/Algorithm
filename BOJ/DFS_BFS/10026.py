import sys
from collections import deque
input = sys.stdin.readline


dy = (-1, 1, 0, 0)
dx = (0, 0, 1, -1)


def bfs(y, x, is_weak=False):
	global visited
	q = deque()
	q.append((y, x))
	visited[y][x] = 1
	color = grid[y][x]
	if is_weak and color != 'B':
		color = 'RG'

	while q:
		y, x = q.popleft()

		for i in range(4):
			ny = dy[i] + y
			nx = dx[i] + x

			if ny < 0 or ny >= N or nx < 0 or nx >= N or visited[ny][nx]:
				continue

			if grid[ny][nx] in color:
				visited[ny][nx] = 1
				q.append((ny, nx))


N = int(input())
grid = [[x for x in input()] for _ in range(N)]
visited = [[0] * N for _ in range(N)]
ans = [0, 0]

for i in range(N):
	for j in range(N):
		if not visited[i][j]:
			bfs(i, j)
			ans[0] += 1

visited = [[0] * N for _ in range(N)]
for i in range(N):
	for j in range(N):
		if not visited[i][j]:
			bfs(i, j, True)
			ans[1] += 1

print(*ans, sep=' ')