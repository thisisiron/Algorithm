from collections import deque
from math import inf
def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    color = {}
    for u in range(1, graph_nodes + 1):
        color[u] = ids[u - 1]
    
    graph = [[] * (graph_nodes + 1) for _ in range(graph_nodes + 1)]
    for u, v in zip(graph_from, graph_to):
        graph[u].append(v)
        graph[v].append(u)
        
    mn = inf
    for i in range(1, graph_nodes + 1):
        if color[i] != val:
            continue
        start = i
        queue = deque()
        dist = 0
        visited = [0] * (graph_nodes + 1)
        queue.append(start)
        visited[start] = 1
        
        while queue:
            cur = queue.popleft()
            dist += 1
            
            for nxt in graph[cur]:
                if not visited[nxt]:
                    if ids[nxt - 1] == val:
                        print(dist)
                        mn = min(dist, mn)
                    queue.append(nxt)
                    visited[nxt] = 1
    return mn if mn != inf else -1