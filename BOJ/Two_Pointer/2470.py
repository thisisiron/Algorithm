import sys 
from math import inf
input = sys.stdin.readline


N = int(input())
arr = list(map(int, input().split()))
arr.sort()

left = 0
right = len(arr) - 1
mn = inf
answer = [left, right]

while left < right:
    mix = arr[right] + arr[left]
    if mn > abs(mix):
        mn = abs(mix)
        answer[0] = arr[left]
        answer[1] = arr[right]

    if mix > 0:
        right -= 1
    elif mix < 0:
        left += 1
    else:
        answer[0] = arr[left]
        answer[1] = arr[right]
        break

print(answer[0], answer[1])