# 최솟값 만들기
# From : https://programmers.co.kr/learn/courses/30/lessons/12941?language=python3
#

def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)

    for x,y in zip(A,B):
        answer += x*y

    return answer

print(solution([1,2],[3,4]))


# 모범 답안
# 한 줄로 코딩하였다.

# def getMinSum(A, B):
#     return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])