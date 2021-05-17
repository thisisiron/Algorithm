import sys
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))
arr.sort()
left = 0
right = N - 1
answer = [0, 0]

mn = float('inf')
while left < right:
    val = arr[left] + arr[right]
    if abs(val) < mn:
        mn = abs(val)
        answer[0] = arr[left]
        answer[1] = arr[right]

    if val > 0:
        right -= 1
    elif val < 0:
        left += 1
    else:
        break
        answer[0] = arr[left]
        answer[1] = arr[right]

print(*answer, sep=' ')