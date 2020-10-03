from collections import deque
import sys


if __name__ == '__main__':

    n: int
    m: int
    k: int
    start: int
    n, m, k, start = map(int, sys.stdin.readline().rstrip().split())
    start -= 1

    adj: dict = {}
    for i in range(m):
        s, e = map(int, sys.stdin.readline().rstrip().split())
        adj.setdefault(s - 1, deque()).append(e - 1)

    queue: deque = deque()
    visited: list = [False] * n
    visited[start] = True 
    cnt: int = 0
    queue.append([start, cnt])
    answer: list = []

    while queue:
        start, cnt = queue.popleft() 
        
        if cnt == k + 1:
            break
        elif cnt == k:
            answer.append(start + 1)
            continue

        if start not in adj.keys():
            continue
        
        cnt += 1
        for v in adj[start]:
            if visited[v] == False:
                queue.append([v, cnt])
                visited[v] = True 
    if answer:        
        answer.sort()
        for a in answer:
            print(a)
    else:
        print(-1)