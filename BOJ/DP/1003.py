import sys
input = sys.stdin.readline


T = int(input())

for _ in range(T):
    n = int(input())
    if n == 0:
        print(1, 0)
        continue
    a = 0
    b = 1
    for i in range(n - 1):
        a, b = b, a + b
    print(a, b)