import sys
input = sys.stdin.readline


N = int(input())

flag = False
cnt = 0
while N != 0:
    if N % 5 == 0:
        cnt += 1
        N -= 5
    elif N % 3 == 0:
        cnt += 1
        N -= 3
    elif N > 5:
        cnt += 1
        N -= 5
    else:
        flag = True
        break

print(cnt if not flag else -1)