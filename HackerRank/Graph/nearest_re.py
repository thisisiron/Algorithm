from collections import deque
from math import inf
def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    color2node = {}
    for node, color in enumerate(ids, 1):
        color2node.setdefault(color, []).append(node)

    if val not in color2node or len(color2node[val]) == 1:  # 찾아야할 색이 그래프 내에 없는 경우도 고려
        return -1
    
    graph = [[] * (graph_nodes + 1) for _ in range(graph_nodes + 1)]
    for u, v in zip(graph_from, graph_to):
        graph[u].append(v)
        graph[v].append(u)
        
    mn = inf
    for start in color2node[val]:
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


if __name__ == '__main__':
    with open('test.txt', 'r') as file:
        lines = file.readlines()

    graph_nodes, graph_edges = map(int, lines[0].split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, lines[i + 1].split())

    ids = list(map(int, lines[i + 2].rstrip().split()))

    val = int(lines[i + 3])

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)
    print(ans)