# 최댓값과 최솟값
# From: https://programmers.co.kr/learn/courses/30/lessons/12939?language=python3
#

def solution(s):
    answer = sorted([int(x) for x in s.split()])
    return str(answer[0]) + " " + str(answer[-1])

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))