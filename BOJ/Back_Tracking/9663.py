import sys 
input = sys.stdin.readline


N = int(input())
a, b, c = [False]*N, [False]*(2*N-1), [False]*(2*N-1)
cnt = 0


def search(i):
    global cnt
    if i == N:
        cnt += 1
        return
    for j in range(N):
        if (not a[j] and not b[i + j] and not c[i - j + N - 1]) :
            a[j] = b[i+j] = c[i-j+N-1] = True
            search(i + 1)
            a[j] = b[i+j] = c[i-j+N-1] = False


search(0)
print(cnt)