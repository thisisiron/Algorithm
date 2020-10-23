import sys 
input = sys.stdin.readline


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort(reverse=True)
    B.sort(reverse=True)

    ap = 0
    bp = 0
    cnt = 0

    while True:
        if bp >= len(B) or ap >= len(A):
            break               

        if B[bp] < A[ap]:
            cnt += M - bp 
            ap += 1
        else:
            bp += 1
    
    print(cnt)