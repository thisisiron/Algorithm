#
# From : https://programmers.co.kr/learn/courses/30/lessons/12919?language=python3
#

def solution(seoul):

    for i, word in enumerate(seoul):
        if word=="Kim":
            break
    return "김서방은 " + str(i) + "에 있다"

print(solution(['Jane', 'Kim']))

# 모범 답안
# 배열 안에서 문자를 찾는 것을 index 함수를 활용하엿고
# format을 이용해서 문자열 중간에 변수를 삽입했다.
# def findKim(seoul):
#     return "김서방은 {}에 있다".format(seoul.index('Kim'))
