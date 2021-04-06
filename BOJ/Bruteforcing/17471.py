import sys
from collections import deque
input = sys.stdin.readline


def bfs(area):
    q = deque()

    check = [0] * (N + 1)
    q.append(area[0])
    check[area[0]] = 1
    
    cnt, total = 1, 0
    while q:
        cur = q.popleft()

        total += people[cur]
        for nxt in graph[cur]:
            if nxt in area and not check[nxt]:
                check[nxt] = 1
                cnt += 1
                q.append(nxt)
    if cnt == len(area):
        return total
    else:
        return 0


def dfs(cnt, cur, end):
    global mn

    if cnt == end:
        area1, area2 = deque(), deque()
        for i in range(1, N + 1):
            if c[i]:
                area1.append(i)
            else:
                area2.append(i)

        num_area1 = bfs(area1)
        if not num_area1:
            return

        num_area2 = bfs(area2)
        if not num_area2:
            return
        
        mn = min(mn, abs(num_area2 - num_area1))
        return

    for i in range(cur, N + 1):
        if c[i]:
            continue
    
        c[i] = 1
        dfs(cnt + 1, i, end)
        c[i] = 0


N = int(input())
people = [0] + [int(x) for x in input().split()]

graph = {}
for i in range(1, N + 1):
    graph[i] = [int(x) for x in input().split()][1:]

mn = float('inf')
for i in range(1, N // 2 + 1 + 1):
    c = [0] * (N + 1)
    dfs(0, 1, i)

print(mn if mn != float('inf') else -1)