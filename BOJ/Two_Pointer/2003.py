import sys 
input = sys.stdin.readline


N, M= map(int, input().split())
x_list = [int(x) for x in input().split()]

start = 0
end = 0
result = 0 
cnt = 0

while end != len(x_list):
    if M <= result:
        result -= x_list[start]
        start += 1
    else:
        result += x_list[end]
        end += 1

    if M == result:
        cnt += 1
    print(f'{start} ~ {end}: {result}')

print(cnt)