#
# From : https://programmers.co.kr/learn/courses/30/lessons/12922?language=python3
#

def solution(n):
    answer = '수박'
    result = ""
    for i in range(n):
        result += answer[i%len(answer)]
    return result

print(3)
print(4)

# 모범 답안
# 파이썬에서 []을 잘 이용한 답안
# def water_melon(n):
#     s = "수박" * n
#     return s[:n]