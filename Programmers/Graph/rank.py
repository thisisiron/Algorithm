from math import inf


def solution(n, results):
    answer = 0
    graph = [[inf] * (n + 1) for _ in range(n + 1)]
    for a, b in results:
        graph[a][b] = 1

    floyd_warshall(graph)

    for i in range(1, len(graph)):
        possible = True
        for j in range(1, len(graph[0])):
            if i != j and (graph[i][j] == inf and graph[j][i] == inf):
                possible = False
                break
        if possible:
            answer += 1

    return answer


def floyd_warshall(graph):
    for k in range(1, len(graph)):
        for i in range(1, len(graph)):
            for j in range(1, len(graph)):
                graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])



print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))