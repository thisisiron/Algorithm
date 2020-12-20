import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    N = int(input())
    L = [int(x) for x in input().split()]
    L.sort()

    a = []
    b = []
    for idx, l in enumerate(L):
        if idx % 2:
            a.append(l)
        else:
            b.append(l)
    
    mx = 0
    for idx in range(len(a) - 1):
        if mx < a[idx + 1] - a[idx]:
            mx = a[idx + 1] - a[idx]

    for idx in range(len(b) - 1):
        if mx < b[idx + 1] - b[idx]:
            mx = b[idx + 1] - b[idx]
    
    mx = max(mx, b[0] - a[0])

    print(mx)