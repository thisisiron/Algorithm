import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
q = deque()
for i in range(N):
    oper = input().split()
    if len(oper) == 2:
        cmd, num = oper
        if cmd == 'push':
            q.append(num)
    else:
        cmd = oper[0]
        if cmd == 'size':
            print(len(q))
        elif cmd == 'front':
            print(q[0] if len(q) else -1)
        elif cmd == 'back':
            print(q[-1] if len(q) else -1)
        elif cmd == 'empty':
            print(0 if len(q) else 1)
        elif cmd == 'pop':
            x = q.popleft() if len(q) else -1
            print(x)