import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())

line = []

for _ in range(N):
    line.append(input().rstrip())

atoi = defaultdict(lambda: 0)

for s in line:
    for i in range(len(s)):
        atoi[s[i]] += 10 ** (len(s) - i)

alpha2num = {} 
i = 9
for k, v in sorted(atoi.items(), key=lambda x: x[1], reverse=True):
    alpha2num[k] = i
    i -= 1

total = 0
for s in line:
    total += int(''.join(str(alpha2num[a]) for a in s))
print(total)