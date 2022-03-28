import sys
input = sys.stdin.readline


N = int(input())
B = [int(x) for x in input().split()]
A = [0 for _ in range(N)]

cnt = 0

while A != B:
    flag = False
    for i in range(N):
        if B[i] % 2 == 1:
            flag = True
            B[i] -= 1
            cnt += 1
            break

    if not flag:
        B = [b // 2 for b in B]
        cnt += 1
print(cnt)