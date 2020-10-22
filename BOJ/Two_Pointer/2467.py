import sys 
from math import inf
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))

start = 0 
end = N - 1
mn = inf 
answer = [0, 0]

while True:
    if start == end:
        break
    result = arr[start] + arr[end]

    if abs(result) < mn:
        mn = abs(result)
        answer[0] = arr[start]
        answer[1] = arr[end]

    if result < 0:
        start += 1
    elif result > 0:
        end -= 1
    else:
        start += 1
        end -= 1

print(*answer)