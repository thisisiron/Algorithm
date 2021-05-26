import sys
import bisect
input = sys.stdin.readline


N = int(input())

lines = [-1]
for l in map(int, input().split()):
    if lines[-1] < l:
        lines.append(l)
    else:
        idx = bisect.bisect_left(lines, l)
        lines[idx] = l
        
print(N - len(lines) + 1)