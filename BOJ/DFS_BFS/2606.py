import sys 
from collections import deque
input = sys.stdin.readline


num_computer = int(input())
num_connect = int(input())

graph = [[] for _ in range(num_computer + 1)]

for _ in range(num_connect):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
visited = [0] * (num_computer + 1)

queue.append(1)
visited[1] = 1

cnt = 0
while queue:
    cur = queue.popleft()

    for nxt in graph[cur]:
        if not visited[nxt]:
            queue.append(nxt)
            visited[nxt] = 1
            cnt += 1
    
print(cnt)