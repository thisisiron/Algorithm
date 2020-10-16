import sys 
input = sys.stdin.readline


N, S = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
total = 0
answer = 123456 

while True:
    if total >= S:
        if answer > end - start:
            answer = end - start
        total -= arr[start]
        start += 1
    elif end == N:
        break
    elif total < S:
        total += arr[end]
        end += 1

if answer == 123456:
    print(0)
else:
    print(answer)