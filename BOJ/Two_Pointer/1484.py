import sys
input = sys.stdin.readline


G = int(input())

now, past = 1, 1
flag = False
while True:
    res = now ** 2 - past ** 2
    if res == G:
        print(now)
        flag = True
    
    if now - past == 1 and res > G:
        break 

    if res > G:
        past += 1
    else:
        now += 1

if not flag:
    print(-1)