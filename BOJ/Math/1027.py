import sys
input = sys.stdin.readline


N = int(input())
b = [int(x) for x in input().split()]

visible = [0] * N
for i in range(N - 1):
    visible[i] += 1
    visible[i + 1] += 1  # 바로 옆 건물은 보임
    grad = b[i + 1] - b[i]  # / (i + 1 - i)는 어차피 1이기때문에 생략
    for j in range(i + 2, N):
        nxt_grad = (b[j] - b[i]) / (j - i)
        if nxt_grad <= grad:  # i건물에서 j건물을 보기 위해서는 grad보다 기울기가 커야함
            continue
        grad = nxt_grad
        visible[i] += 1
        visible[j] += 1

print(max(visible))

