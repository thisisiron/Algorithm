import sys
from collections import deque
input = sys.stdin.readline
    

N = int(input())

if N >= 1023:
    print(-1)
elif N == 0:
    print(0)
else:
    q = deque()

    for i in range(1, 10):
        q.append(i)
    
    while q:
        num = q.popleft()
        N -= 1

        if N == 0:
            print(num)
            break
        
        last = num % 10
        for i in range(last):
            q.append(num * 10 + i)