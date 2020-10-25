import sys 
input = sys.stdin.readline


def lower_bound(arr, x):
    left = 0
    right = len(arr) - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            ans = mid
            right = mid - 1
        elif arr[mid] > x: 
            right = mid - 1
        else:
            left = mid + 1
    return ans 


def upper_bound(arr, x):
    left = 0
    right = len(arr) - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            ans = mid + 1
            left = mid + 1
        elif arr[mid] > x: 
            right = mid - 1
        else:
            left = mid + 1
    return ans 


N = int(input())

A = [0] * N
B = [0] * N
C = [0] * N
D = [0] * N

for i in range(N):
    A[i], B[i], C[i], D[i] = map(int, input().split())

X = [0] * N**2
Y = [0] * N**2
for i in range(N):
    for j in range(N):
        X[i * N + j] = A[i] + B[j]
        Y[i * N + j] = C[i] + D[j]
    
Y.sort()

cnt = 0
for x in X:
    low = lower_bound(Y, -x)
    up = upper_bound(Y, -x)
    if low != -1:
        cnt += (up - low)
print(cnt)