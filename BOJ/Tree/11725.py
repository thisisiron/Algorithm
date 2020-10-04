import sys
from collections import deque
input = sys.stdin.readline


if __name__ == '__main__':
    num_node: int = int(input())
    adj: dict = {}

    for i in range(num_node - 1):
        u, v = map(int, input().split())
        adj.setdefault(u, []).append(v)
        adj.setdefault(v, []).append(u)

    visited: list = [0] * (num_node + 1)
    visited[1] = 1
    queue: deque = deque()
    queue.append(1)

    while queue:
        next_node = queue.popleft()

        for val in adj[next_node]:
            if visited[val] == 0:
                queue.append(val)
                visited[val] = next_node 
    
    for ans in visited[2:]:
        print(ans)