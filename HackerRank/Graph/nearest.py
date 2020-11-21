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