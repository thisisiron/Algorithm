from collections import deque


A, B = map(int, input().split())
cnt = 0
flag = False
queue = deque()
queue.append((A, cnt))

while queue:
    A, cnt = queue.popleft()
    if A == B:
        flag = True
        break
    elif A > B:
        continue
    queue.append((A * 2, cnt + 1))
    queue.append((int(str(A) + '1'), cnt + 1))

if flag:
    print(cnt + 1) 
else:
    print(-1)