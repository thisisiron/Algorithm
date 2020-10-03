# 직사각형 별찍기
# From : https://programmers.co.kr/learn/courses/30/lessons/12969?language=python3
#

a, b = map(int, input().strip().split(' '))
# print(a + b)
for i in range(b):
    for j in range(a):
        print('*', end="")
    print()

# 모범 답안
# 파이써닉하게 풀었다. 
# a, b = map(int, input().strip().split(' '))
# answer = ('*'*a +'\n')*b
# print(answer)
