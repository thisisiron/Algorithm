import sys
from math import inf
input = sys.stdin.readline


N, K = map(int, input().split())
arr = list(map(int, input().split()))

start = 0 
end = K
result = sum(arr[start:end])
mx = -inf 

while True:
    if mx < result:
        mx = result
    
    if end == len(arr):
        break

    result -= arr[start]
    start += 1
    result += arr[end]
    end += 1
    
print(mx)