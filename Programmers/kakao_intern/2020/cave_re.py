from collections import deque
import sys
sys.setrecursionlimit(10**9)


def solution(n, path, order):
    graph = [[] for _ in range(n + 1)]
    for u, v in path:
        graph[u].append(v)
        graph[v].append(u)

    start = 0
    visited = [0] * (n + 1)
    queue = deque()
    tree = [[] for _ in range(n + 1)]

    queue.append(start)
    visited[start] = 1
    while queue:
        cur = queue.popleft()    
        
        for nxt in graph[cur]:
            if not visited[nxt]:
                queue.append(nxt)
                tree[cur].append(nxt)
                visited[nxt] = 1
    
    # keypoint!!!
    for u, v in order:
        tree[u].append(v)

    visited = [0] * (n + 1)
    checked = [0] * (n + 1)

    is_cycle = check_cycle(tree, visited, checked, start)

    return not is_cycle 

def check_cycle(tree, visited, checked, start):
    visited[start] = 1
    checked[start] = 1

    for nxt in tree[start]:
        if not checked[nxt]:
            if check_cycle(tree, visited, checked, nxt):
                return True
        if visited[nxt]:
            return True
    visited[start] = 0
    return False
            


print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]))
print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]]))