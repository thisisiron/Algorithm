#
# From : https://programmers.co.kr/learn/challenge_codes/95
#

import operator
def strange_sort(strings, n):
    '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
    x={}
    for string in strings:
        x[string[n]] = string
    sorted_x = sorted(x.items(), key=operator.itemgetter(0))
    return [y[1] for y in sorted_x]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( strange_sort(["sun", "bed", "car"], 1) )


# 모범답안
# 
# def strange_sort(strings, n):
#     '''strings의 문자열들을 n번째 글자를 기준으로 정렬해서 return하세요'''
#     return sorted(strings, key=lambda x: x[n])

# strings = ["sun", "bed", "car"] 
# print(strange_sort(strings, 1))