# 타겟 넘버
# From : https://programmers.co.kr/learn/courses/30/lessons/43165
#

def solution(numbers, target):
    print(numbers, target)
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])


print(solution([1, 1, 1, 1, 1],3))