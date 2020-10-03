from collections import deque
import sys


sys.setrecursionlimit(10**9)


class Tree(object):
    def __init__(self):
        self.adj: dict = {}
    
    def add(self, node1: int, node2: int):
        self.adj.setdefault(node1, []).append(node2)
        self.adj.setdefault(node2, []).append(node1)


def solution(n: int, path: list, order: list) -> bool:
    answer = True

    tree = Tree()
    visited: list = [False] * n 

    for node1, node2 in path:
        tree.add(node1, node2)

    directed: dict = bfs(0, tree, visited)
    for node1, node2 in order:
        directed.setdefault(node1, []).append(node2)
    # print(directed)
    visited: list = [False] * n 
    checked: list = [False] * n 
    is_cycle: bool = check_cycle(0, directed, visited, checked)

    return False if is_cycle else True 


def check_cycle(start: int, directed: dict, visited: list, checked: list):
    visited[start] = True
    checked[start] = True

    try:
        for next_node in directed[start]:
            if not checked[next_node]:
                if check_cycle(next_node, directed, visited, checked):
                    return True
            if visited[next_node]:
                return True
    except KeyError as e:
        pass
    visited[start] = False
    # print(start, visited)
    return False


def bfs(start: int, tree: Tree, visited: list) -> dict:
    queue: deque = deque()
    queue.append(start)

    directed: dict = {}
    
    while queue:
        cur: int = queue.popleft()

        for node in tree.adj[cur]:
            if not visited[node]:
                visited[cur] = True
                queue.append(node)
                directed.setdefault(cur, []).append(node)
    return directed


if __name__ == '__main__':
    print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[8,5],[6,7],[4,1]]))
    print(solution(9, [[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]], [[4,1],[8,7],[6,5]]))


