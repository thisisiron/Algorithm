import sys
input = sys.stdin.readline


N = input().rstrip().zfill(2)

init = N
N = N[1] + str(int(N[0]) + int(N[1])).zfill(2)[1]
cnt = 1
while init != N:
    N = N[1] + str(int(N[0]) + int(N[1])).zfill(2)[1]
    cnt += 1
print(cnt)