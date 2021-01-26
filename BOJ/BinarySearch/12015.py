import sys
import bisect
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))

temp = []

for a in arr:
    if len(temp) == 0 or temp[-1] < a:
        temp.append(a)
    else:
        idx = bisect.bisect_left(temp, a)
        temp[idx] = a

print(len(temp))