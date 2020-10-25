import sys 
from collections import Counter
input = sys.stdin.readline


N = int(input())

A = []
B = []
C = []
D = []

for i in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

X = []
for a in A:
    for b in B: 
        X.append(a + b)
    
counter = Counter(X)
cnt = 0
for c in C:
    for d in D:
        if -(c + d) in counter:
            cnt += counter[-(c + d)]
print(cnt)