import sys 
input = sys.stdin.readline


N = int(input())
M = int(input())
arr = list(map(int, input().split()))
arr.sort()

left = 0
right = N - 1
cnt = 0

while True:
    if left >= right:
        break

    amor = arr[left] + arr[right]

    if amor == M:
        cnt += 1
        left += 1
        right -= 1
    elif amor < M:
        left += 1
    elif amor > M:
        right -= 1

print(cnt)