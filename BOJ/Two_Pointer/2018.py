import sys 
input = sys.stdin.readline


N = int(input())

start = 1
end =  1
result = 0
cnt = 0

while True:
    if start > N:
        break

    if result >= N:
        if result == N:
            cnt += 1
        result -= start 
        start += 1
    else:
        result += end 
        end += 1

print(cnt)