import sys
from collections import deque
input = sys.stdin.readline


d = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))

M, N, H = map(int, input().split())
num_tomato = 0
boxes = []
q = deque()
for h in range(H):
    box = []
    for n in range(N):
        row = [int(x) for x in input().split()]
        for m in range(M):
            if row[m] == 0:
                num_tomato += 1
            elif row[m] == 1:
                q.append((h, n, m))
        box.append(row)
    boxes.append(box)

num_day = 0
while q: 
    if num_tomato == 0:
        break
    new_q = deque()
    while q:
        z, y, x = q.popleft()

        for i in range(6):
            nz = z + d[i][0]
            ny = y + d[i][1]
            nx = x + d[i][2]

            if nz < 0 or nz >= H or ny < 0 or ny >= N or nx < 0 or nx >= M or boxes[nz][ny][nx] == -1:
                continue
            
            if boxes[z][y][x] == 1 and boxes[nz][ny][nx] == 0:
                boxes[nz][ny][nx] = 1
                new_q.append((nz, ny, nx))
                num_tomato -= 1
    num_day += 1
    q = new_q

print(num_day if num_tomato == 0 else -1)