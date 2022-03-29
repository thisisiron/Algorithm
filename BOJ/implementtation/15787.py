import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split())
trains = [deque([0] * 20) for _ in range(N)]

for _ in range(M):
    cmd = list(map(int, input().split()))

    if cmd[0] == 1:
        if not trains[cmd[1] - 1][cmd[2] - 1]:
            trains[cmd[1] - 1][cmd[2] - 1] = 1
        
    elif cmd[0] == 2:
        if trains[cmd[1] - 1][cmd[2] - 1]:
            trains[cmd[1] - 1][cmd[2] - 1] = 0
    
    elif cmd[0] == 3:
        if trains[cmd[1] - 1][-1]:
            trains[cmd[1] - 1][-1] = 0
        trains[cmd[1] - 1].rotate(1)
    
    elif cmd[0] == 4:
        if trains[cmd[1] - 1][0]:
            trains[cmd[1] - 1][0] = 0
        trains[cmd[1] - 1].rotate(-1)

ans = {tuple(train) for train in trains}
    
print(len(ans))