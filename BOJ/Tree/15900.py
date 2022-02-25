import sys
input = sys.stdin.readline


N = int(input())

tree = {}

while True:
    try:
        a, b = map(int,input().split())
        tree.setdefault(a, []).append(b)
        tree.setdefault(b, []).append(a)
    except:
        break

cur = 1
lv = 0
stack = [(cur, lv)]
visited = [0 for _ in range(N + 1)]
visited[cur] = 1
total = 0

while stack:
    cur, lv = stack.pop()

    edge = 0
    for nxt in tree[cur]:
        if not visited[nxt]:
            stack.append((nxt, lv + 1))
            visited[nxt] = 1
            edge += 1
    
    if edge == 0:
        total += lv

print('No' if total % 2 == 0 else 'Yes')