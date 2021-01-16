import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
arr = []
graph = {}
for a in range(1, N + 1):
    b = int(input())
    graph[a] = b

while True:
    unique = set(graph.values())
    graph = {key: val for key, val in graph.items() if key in unique}
    if unique == set(graph.values()):
        break
print(len(graph))
print(*graph.keys(), sep='\n')