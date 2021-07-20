import sys
input = sys.stdin.readline


N, M, B = map(int, input().split())

M, B = M/100, B/100
p = [(1, 1)]
for _ in range(N):
    l = len(p)
    w, r = input().split()
    w, r = int(w) / 100, float(r)

    for c in range(l):
        (a, s) = p.pop(0)
        p.append((a * (1 + (r - 1) * M), s * w))
        if a * (1 - M) > B:
            p.append((a * (1 - M), s * (1 - w)))
print(100 * sum(s[1] for s in p if s[0] > 1))