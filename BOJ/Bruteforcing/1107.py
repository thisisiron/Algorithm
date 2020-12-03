import sys
input = sys.stdin.readline


N = int(input())
M = int(input())
enable = {str(i) for i in range(10)}
if M != 0:
    enable -= set(input().rstrip().split())

min_cnt = abs(100 - N)

for num in range(1000001):
    num = str(num)
    for i in range(len(num)):
        if num[i] not in enable:
            break
        elif i == len(num) - 1:
            min_cnt = min(min_cnt, abs(N - int(num)) + len(num))

print(min_cnt)