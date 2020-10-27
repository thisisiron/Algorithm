import sys 
import heapq
input = sys.stdin.readline


M, N = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(N)]
visited = [[-1] * M for _ in range(N)]

queue = [(0, (0, 0))]
visited[0][0] = 0
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

while queue:
    cnt, (y, x) = heapq.heappop(queue)

    if x == M - 1 and y == N - 1:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and visited[ny][nx] < 0:
            visited[ny][nx] = cnt

            if maze[ny][nx] == 1:
                heapq.heappush(queue, (cnt + 1, (ny, nx)))
            else:
                heapq.heappush(queue, (cnt, (ny, nx)))

print(visited[y][x])