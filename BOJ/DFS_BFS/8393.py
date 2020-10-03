import sys
input = sys.stdin.readline


number = int(input())
answer = 0
for i in range(number + 1):
    answer += i
print(answer)