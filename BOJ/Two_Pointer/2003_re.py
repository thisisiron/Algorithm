import sys 
input = sys.stdin.readline


N, M= map(int, input().split())
x_list = [int(x) for x in input().split()]

start = 0
end = 0
result = 0 
cnt = 0

while True:
    if M <= result:
        result -= x_list[start]
        start += 1
    elif end == len(x_list):
        break
    else:
        result += x_list[end]
        end += 1

    if M == result:
        cnt += 1

print(cnt)