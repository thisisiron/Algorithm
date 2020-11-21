from math import inf
def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    color2node = {}
    for node, color in enumerate(ids, 1):
        color2node.setdefault(color, []).append(node)
        
    if len(color2node[val]) == 1:
        return -1
    # print(color2node)
    
    graph = [[inf for _ in range(graph_nodes + 1)] for _ in range(graph_nodes + 1)]
    for u, v in zip(graph_from, graph_to):
        graph[u][v] = 1
        graph[v][u] = 1
        
    for k in range(1, graph_nodes + 1):
        for i in range(1, graph_nodes + 1):
            for j in range(1, graph_nodes + 1):
                graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])
        
    mn = inf
    for i in range(len(color2node[val])):
        for j in range(i + 1, len(color2node[val])):
            if mn > graph[color2node[val][i]][color2node[val][j]]:
                mn = graph[color2node[val][i]][color2node[val][j]]
    return mn if mn != inf else -