import sys
from collections import deque
input = sys.stdin.readline


def bfs(start, end):
    q = deque()
    visited_station = [0] * (N + 1)
    visited_route = [0] * L

    for station in stations[start]:
        visited_route[station] = 1

        for v in route[station]:
            q.append((v, 0))
            visited_station[v] = 1

    while q:
        u, cnt = q.popleft()
        if v == end:
            return cnt

        for station in stations[u]:
            print('st', station)
            if visited_route[station]:
                continue
            visited_route = 1

            for v in route[station]:
                if visited_station[v]:
                    continue
                q.append((v, cnt + 1))
                visited_station[v] = 1

    return -1


N, L = map(int, input().split())
stations = [[] for _ in range(N + 1)]
route = [[] for _ in range(L)]

for i in range(L):
    for v in map(int, input().split()):
        if v == -1:
            break
        route[i].append(v)
        stations[v].append(i)

print(stations)
print(route)
start, end = map(int, input().split())
bfs(start, end)
