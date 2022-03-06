import sys
input = sys.stdin.readline


N, K = map(int, input().split())
S = [int(x) for x in input().split()]

k = 0
right = 0
count = 0
mx = 0
for left in range(N):
    while k <= K and right < N:
        if S[right] % 2 == 1:  # odd
            k += 1
        else:  # even
            count += 1
        right += 1

        if left == 0 and right == N:  # max
            mx = count

    if k == K + 1 and mx < count:
        mx = count

    if S[left] % 2 == 0:
        count -= 1
    else:
        k -= 1

print(mx)