import sys 
input = sys.stdin.readline


n = int(input())
arr = list(map(int, input().split()))
x = int(input())

arr.sort()

start = 0 
end = n - 1
cnt = 0

while start < end:
    result = arr[start] + arr[end]

    if result > x:
        end -= 1
    elif result < x:
        start += 1
    else:
        cnt += 1
        end -=1
        start += 1

print(cnt)