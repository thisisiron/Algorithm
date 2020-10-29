import heapq
from collections import Counter
from math import inf


def solution(n, edge):
    graph = [[] * (n + 1) for _ in range(n + 1)]
    for u, v in edge:
        graph[u].append((v, 1))
        graph[v].append((u, 1))

    start = 1
    q = []
    distances = [inf] * (n + 1)
    distances[start] = 0
    distances[0] = 0
    q.append((0, start))

    while q:
        now_d, now_n = heapq.heappop(q)
        if now_d > distances[now_n]:
            continue
        for next_n, next_d in graph[now_n]:
            new_d = now_d + next_d
            if new_d < distances[next_n]:
                distances[next_n] = new_d
                heapq.heappush(q, (new_d, next_n))

    counter = Counter(distances)
    return counter[max(counter)]


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))