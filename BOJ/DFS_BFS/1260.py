from collections import deque
from collections import defaultdict
import bisect


def dfs(adj: dict, start: int, n: int) -> list:

    visited: list = [start]
    stack: deque = deque()
    stack.append(start)

    while stack:
        cur: int = stack.pop()
        if cur not in visited:
            visited.append(cur)
        # print(cur, end=" ")
        if len(visited) == n:
            break
        for v in adj[cur][::-1]:
            if v in visited:
                continue
            stack.append(v)
    return visited


def bfs(adj: dict, start: int, n: int) -> list:
    visited: list = [start]
    queue: deque = deque()
    queue.append(start)

    while queue:
        cur = queue.popleft()
        if cur not in visited:
            visited.append(cur)
        # print(cur, end=" ")
        if len(visited) == n:
            break
        for v in adj[cur]:
            if v in visited:
                continue
            queue.append(v)
    return visited


if __name__ == '__main__':
    n: int
    m: int
    start: int
    n, m, start = map(int, input().split())
    adj: defaultdict = defaultdict(list) 

    for _ in range(m):
        a: int
        b: int
        a, b = map(int, input().split())

        if a in adj.keys():
            bisect.insort(adj[a], b)
        else:
            adj.setdefault(a, []).append(b)

        if b in adj.keys():
            bisect.insort(adj[b], a)
        else:
            adj.setdefault(b, []).append(a)
    
    print(" ".join(map(str, dfs(adj, start, n))))
    print(" ".join(map(str, bfs(adj, start, n))))