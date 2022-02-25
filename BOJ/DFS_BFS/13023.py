import sys
from xml.dom.pulldom import START_DOCUMENT
input = sys.stdin.readline


def dfs(cur, step):
    if step == 4:
        return True
    else:
        if cur in f:
            for nxt in f[cur]:
                if not visited[nxt]:
                    visited[nxt] = 1
                    flag = dfs(nxt, step + 1)
                    if flag:
                        return flag
                    visited[nxt] = 0


N, M = map(int, input().split())

f = {}
for _ in range(M):
    a, b = map(int, input().split())
    f.setdefault(a, []).append(b)
    f.setdefault(b, []).append(a)

visited = [0 for _ in range(N)]

for start in range(N):
    visited[start] = 1
    flag = dfs(start, 0)
    visited[start] = 0
    if flag:
        break
print(1 if flag else 0)