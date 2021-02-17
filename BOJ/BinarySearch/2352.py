import sys
import bisect
input = sys.stdin.readline


n = int(input())
target_ports = [int(x) for x in input().split()]
link = []
for target in target_ports:
    if not link or link[-1] < target:
        link.append(target)
    else:
        link[bisect.bisect(link, target)] = target 
    
print(len(link))
