import sys
input = sys.stdin.readline


def check(mid):
    prev = 0
    cnt = 0
    for i in range(len(S)):
        if S[i] - prev >= mid:
            cnt += 1
            prev = S[i]
    return cnt > q


N, M, L = map(int, input().split())
S = [int(input()) for _ in range(M)]
S.append(L)

for _ in range(N):
    mx = 0
    q = int(input())

    left = 0
    right = L

    while left <= right:
        mid = (left + right) // 2
        
        if check(mid):
            left = mid + 1
            if mx < mid:
                mx = mid
        else:
            right = mid - 1
    print(mx)