#
# From : https://programmers.co.kr/learn/courses/30/lessons/12932?language=python3
#

def solution(n):
    answer = [int(x) for x in str(n)]
    answer.reverse()
    return answer


# 입력 : 437
# 출력 : 734
print(solution(437))


# 모범 답안 1

# def digit_reverse(n):
#     return list(map(int, reversed(str(n))))

# 모범 답안 2

# def digit_reverse(n):
#     return [int(x) for x in str(n)][::-1]