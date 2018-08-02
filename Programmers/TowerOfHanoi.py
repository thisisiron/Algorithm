# 하노이의 타워
# From: https://programmers.co.kr/learn/courses/30/lessons/12946?language=python3
#

def solution(n):
    answer = []
    num = int((2**n) - 1)
    hanoi(answer, num, 1,2, 3)
    return answer

def hanoi(answer, num, start=1, mid=2, end=3):
    
    if num==1:
        break
    else:
        # mid = int((start + end)/2) # mid = 2
        hanoi(answer, num-1, start, end, mid)
        answer.append([start,end])
        hanoi(answer, num-1, mid, start, end)

print(solution(2))
print(solution(3))