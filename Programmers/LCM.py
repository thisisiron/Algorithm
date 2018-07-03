# N개의 최소공배수
# From: https://programmers.co.kr/learn/courses/30/lessons/12953?language=python3
#

def gcd(a,b):
    r = 0
    while(b!=0):
        r = a % b
        a = b
        b = r
    return a

def lcm(a,b):
    return a*b/gcd(a,b)

def solution(arr):
    answer = 1
    for x in arr:
        answer = lcm(answer,x)
    return int(answer)

# 168
print(solution([2,6,8,14]))
# 6
print(solution([1,2,3]))
