import sys
from collections import deque
input = sys.stdin.readline


MAX = 100001
n, k = map(int, input().split())
arr = [0] * MAX
q = deque()
q.append(n)

while q:
    cur = q.popleft()

    if cur == k:
        print(arr[cur])
        break
    
    for nxt in (cur - 1, cur + 1, 2 * cur):
        if 0 <= nxt < MAX and not arr[nxt]:
            if nxt == 2 * cur and cur != 0:
                arr[nxt] = arr[cur]
                q.appendleft(nxt)
            else:
                arr[nxt] = arr[cur] + 1
                q.append(nxt)
