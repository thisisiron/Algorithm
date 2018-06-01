# JadenCase 문자열 만들기
# From: https://programmers.co.kr/learn/courses/30/lessons/12951?language=python3
#

def solution(s):
    return " ".join([word[0].upper()+word[1:].lower() if len(word)>=1 else word for word in s.split(" ")])

print(solution("3people unFollowed me"))
# 공백 2개도 고려해야 한다.
print(solution("heLlo  woRld"))