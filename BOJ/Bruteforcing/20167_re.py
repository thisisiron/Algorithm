import sys
input = sys.stdin.readline


def search(idx, s, cnt):
    global ans
    if idx == N:
        if ans < cnt:
            ans = cnt
    else:
        search(idx + 1, 0, cnt)
        if s + branch[idx] >= K:
            search(idx + 1, 0, cnt + s + branch[idx] - K)
        else:
            search(idx + 1, s + branch[idx], cnt)


N, K = map(int, input().split())
branch = [int(x) for x in input().split()]
ans = 0

search(0, 0, 0)
print(ans)