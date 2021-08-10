import sys
input = sys.stdin.readline
MAX_NUM = 10001

N = int(input())
b = [0] * MAX_NUM
for i in range(N):
    b[int(input())] += 1
for i in range(MAX_NUM):
    if b[i] != 0:
        for j in range(b[i]):
            print(i)