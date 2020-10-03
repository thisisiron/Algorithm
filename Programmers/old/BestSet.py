# 최고의 집합
# From: https://programmers.co.kr/learn/courses/30/lessons/12938?language=python3
#
from math import ceil

def solution(n,s):
    if n>s:
        return [-1]
    answer = []
    mid = ceil(s/n)
    answer.append(mid)
    if n == 1:
        return answer
    else:
        answer.extend(solution(n-1, s-mid))
    return sorted(answer)

# [4,5]
print(solution(2,9))
print(solution(3,10))
print(solution(4,14))
print('-----------------------')

# 다른 사람 풀이
def bestSet(n, s):
    if n > s:
        return [-1]
    portion, remainder = divmod(s, n)
    print("portion:",portion, "reminder:",remainder)
    li = [portion] * n
    for i in range(remainder):
        li[i] += 1

    return sorted(li)

print(bestSet(2,9))
print(bestSet(3,10))
print(bestSet(4,14))