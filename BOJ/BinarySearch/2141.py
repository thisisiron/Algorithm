import sys
input = sys.stdin.readline


N = int(input())
arr = []
num_people = 0
for _ in range(N):
    x, a = map(int, input().split())
    arr.append((x, a))
    num_people += a

arr.sort()
num_people /= 2
tmp = 0
for i in range(N):
    tmp += arr[i][1]
    if tmp >= num_people:
        print(arr[i][0])
        break
