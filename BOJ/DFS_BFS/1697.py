import sys 
from collections import deque
input = sys.stdin.readline


N, K = map(int, input().split())
MAX = 100001

cnt = 0
queue = deque()
visited = [0] * MAX 

queue.append([N, cnt])
visited[N] = 0

while queue:
    cur, cnt = queue.popleft()

    if cur == K:
        break
    
    if cur + 1 < MAX and visited[cur + 1] == 0:
        queue.append([cur + 1, cnt + 1])
        visited[cur + 1] = 1
    if  cur - 1 >= 0 and visited[cur - 1] == 0:
        queue.append([cur - 1, cnt + 1])
        visited[cur - 1] = 1
    if  cur * 2 < MAX and visited[cur * 2] == 0:
        queue.append([cur * 2, cnt + 1])
        visited[cur * 2] = 1

print(cnt)